from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationTabularInline
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.html import format_html

from .media import parse_video
from .models import (Case, CaseImage, CaseVideo, Client, Industry, IndustryImage, IndustryVideo, Lead, MemberImage,
                     MemberVideo, Partner, Presentation, ServiceVideo,
                     Service, SiteSettings, Stat, Step, TeamMember, Value, WhyCard)

admin.site.index_template = 'admin/finora_index.html'

# Guruhlar (Groups) bu loyihada kerak emas — menyuni soddalashtiramiz
import django.contrib.auth.admin  # noqa: E402,F401  (avval auth admin ro'yxatdan o'tsin)
from django.contrib.auth.models import Group  # noqa: E402
admin.site.unregister(Group)


def thumb(field, label='Rasm', white=True):
    def _thumb(model_admin, obj):
        f = getattr(obj, field, None)
        if not f:
            return '—'
        bg = 'background:#fff;' if white else ''
        return format_html("<img src='{}' style='height:40px;max-width:90px;object-fit:contain;border-radius:6px;{}padding:2px'>", f.url, bg)
    _thumb.short_description = label
    return _thumb


class FsAdmin(admin.ModelAdmin):
    """Ro'yxat sahifasi sarlavhasi: "Select … to change" o'rniga bo'lim nomi."""

    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': self.model._meta.verbose_name_plural, **(extra_context or {})}
        return super().changelist_view(request, extra_context)


class OrderedAdmin(FsAdmin):
    """Tartib raqami va "saytda ko'rsatish" belgisini ro'yxatning o'zida o'zgartirish mumkin."""
    list_editable = ('active', 'sort')
    list_filter = ('active',)
    list_per_page = 50


class TrOrderedAdmin(TabbedTranslationAdmin, OrderedAdmin):
    """Matn maydonlari UZ / EN / RU yorliqlari bilan."""


# ---------------------------------------------------------------- Arizalar

@admin.register(Lead)
class LeadAdmin(FsAdmin):
    list_display = ('name', 'phone_link', 'service', 'source_label', 'lang', 'status', 'created_at')
    list_display_links = ('name',)
    list_editable = ('status',)
    list_filter = ('status', 'source', 'lang', 'created_at')
    search_fields = ('name', 'phone', 'service', 'message')
    readonly_fields = ('name', 'phone_link', 'service', 'message', 'source_label', 'page', 'lang', 'created_at')
    fieldsets = (
        ('Ariza', {'fields': ('name', 'phone_link', 'service', 'message', 'source_label', 'page', 'lang', 'created_at')}),
        ('Ishlov berish', {'fields': ('status', 'note')}),
    )
    date_hierarchy = 'created_at'

    @admin.display(description='Telefon')
    def phone_link(self, obj):
        return format_html("<a href='tel:{}'>{}</a>", obj.phone.replace(' ', ''), obj.phone)

    @admin.display(description='Manba')
    def source_label(self, obj):
        return obj.source_label

    def has_add_permission(self, request):
        return False  # arizalar faqat saytdan keladi


# ---------------------------------------------------------------- Kontent

@admin.register(Service)
class ServiceAdmin(TrOrderedAdmin):
    list_display = ('title', 'subtitle', 'in_footer', 'active', 'sort')
    search_fields = ('title',)
    fieldsets = ((None, {'fields': ('title', 'subtitle', 'items', ('in_footer', 'active'), 'sort')}),)


@admin.register(Industry)
class IndustryAdmin(TrOrderedAdmin):
    list_display = ('title', 'image_thumb', 'on_home', 'in_footer', 'active', 'sort')
    image_thumb = thumb('image')
    search_fields = ('title',)
    fieldsets = (
        (None, {'fields': ('title', 'label', 'short', ('mock', 'image'), ('on_home', 'in_footer', 'active'), 'sort')}),
        ('Soha sahifasi — batafsil', {'fields': ('description', 'pains', 'solutions', 'ai', 'web')}),
    )


class VideoInline(TranslationTabularInline):
    extra = 0
    fields = ('title', 'url', 'file', 'cover', 'preview', 'sort')
    readonly_fields = ('preview',)

    @admin.display(description="Ko'rish")
    def preview(self, obj):
        v = parse_video(obj.src) if obj and obj.pk else None
        if not v:
            return '—'
        if v['kind'] == 'youtube':
            return format_html("<a href='https://youtu.be/{0}' target='_blank'><img src='https://i.ytimg.com/vi/{0}/mqdefault.jpg' style='height:54px;border-radius:6px'></a>", v['id'])
        if v['kind'] == 'instagram':
            return format_html("<a href='{}' target='_blank' style='display:inline-block;padding:6px 10px;border-radius:8px;"
                               "background:linear-gradient(45deg,#fd5949,#d6249f,#285aeb);color:#fff;font-weight:700'>▶ Instagram</a>",
                               obj.url)
        if v['kind'] == 'file':
            return format_html("<video src='{}' style='height:54px;border-radius:6px' controls preload='metadata'></video>", v['src'])
        return format_html("<a href='{}' target='_blank'>Vimeo</a>", obj.url)


class ImageInline(admin.TabularInline):
    extra = 0
    fields = ('image', 'preview', 'sort')
    readonly_fields = ('preview',)

    @admin.display(description="Ko'rish")
    def preview(self, obj):
        return format_html("<img src='{}' style='height:54px;border-radius:6px'>", obj.image.url) if obj and obj.image else '—'


class CaseVideoInline(VideoInline):
    model = CaseVideo


class CaseImageInline(ImageInline):
    model = CaseImage


class IndustryVideoInline(VideoInline):
    model = IndustryVideo


class IndustryImageInline(ImageInline):
    model = IndustryImage


class PresentationInline(TranslationTabularInline):
    model = Presentation
    extra = 0
    fields = ('title', 'file', 'url', 'sort')


class ServiceVideoInline(VideoInline):
    model = ServiceVideo


IndustryAdmin.inlines = [IndustryVideoInline, IndustryImageInline]
ServiceAdmin.inlines = [PresentationInline, ServiceVideoInline]


@admin.register(Presentation)
class PresentationAdmin(TabbedTranslationAdmin, FsAdmin):
    """Barcha taqdimotlar bitta ro'yxatda (xizmatga biriktirilmaganlari ham ko'rinadi)."""
    list_display = ('title', 'service', 'kind', 'sort')
    list_editable = ('service', 'sort')
    list_filter = ('service',)
    fields = ('title', 'service', 'file', 'url', 'sort')

    @admin.display(description='Turi')
    def kind(self, obj):
        return obj.ext or 'Havola'


class MemberVideoInline(VideoInline):
    model = MemberVideo


class MemberImageInline(ImageInline):
    model = MemberImage


@admin.register(Case)
class CaseAdmin(TrOrderedAdmin):
    list_display = ('title', 'logo_thumb', 'client', 'on_home', 'active', 'sort')
    logo_thumb = thumb('logo', 'Logo')
    search_fields = ('title', 'client')
    list_filter = ('active', 'on_home', 'direction')
    inlines = [CaseVideoInline, CaseImageInline]
    fieldsets = (
        ('Asosiy', {'fields': ('title', ('client', 'logo'), 'description', 'industry', ('direction', 'year', 'duration'),
                               'tags', 'result', ('mock', 'image'), ('on_home', 'active'), 'sort')}),
        ('Keys sahifasi — batafsil', {'fields': ('challenge', 'solution', 'works', 'metrics')}),
        ('Mijoz fikri (otziv)', {'fields': ('t_text', ('t_author', 't_role'), 't_photo', 't_video_url', 't_video_file')}),
    )


@admin.register(TeamMember)
class TeamMemberAdmin(TrOrderedAdmin):
    list_display = ('name', 'photo_thumb', 'role', 'on_home', 'active', 'sort')
    photo_thumb = thumb('photo', 'Foto', white=False)
    search_fields = ('name', 'role')
    inlines = [MemberVideoInline, MemberImageInline]
    fieldsets = (
        ('Asosiy', {'fields': ('name', 'role', 'photo', ('on_home', 'active'), 'sort')}),
        ("A'zo sahifasi — batafsil", {'fields': ('intro', 'bio', 'skills', 'experience', 'education', 'achievements')}),
        ('Aloqa', {'fields': ('telegram', 'linkedin', 'instagram', 'email')}),
    )


@admin.register(Client)
class ClientAdmin(OrderedAdmin):
    list_display = ('name', 'logo_thumb', 'row', 'dark', 'active', 'sort')
    logo_thumb = thumb('logo', 'Logo')
    list_filter = ('active', 'row')


@admin.register(Partner)
class PartnerAdmin(OrderedAdmin):
    list_display = ('name', 'logo_thumb', 'active', 'sort')
    logo_thumb = thumb('logo', 'Logo')


@admin.register(Stat)
class StatAdmin(TrOrderedAdmin):
    list_display = ('value', 'label', 'highlight', 'active', 'sort')


@admin.register(WhyCard)
class WhyCardAdmin(TrOrderedAdmin):
    list_display = ('title', 'active', 'sort')


@admin.register(Step)
class StepAdmin(TrOrderedAdmin):
    list_display = ('title', 'active', 'sort')


@admin.register(Value)
class ValueAdmin(TrOrderedAdmin):
    list_display = ('title', 'active', 'sort')


# ---------------------------------------------------------------- Sozlamalar

@admin.register(SiteSettings)
class SiteSettingsAdmin(TabbedTranslationAdmin):
    fieldsets = (
        ('Umumiy', {'fields': ('site_name', 'logo', 'meta_description', 'phone', 'email', 'address', 'telegram_username')}),
        ('Ijtimoiy tarmoqlar', {'fields': ('social_telegram', 'social_instagram', 'social_linkedin', 'social_youtube', 'social_facebook')}),
        ('Bosh sahifa', {'fields': ('hero_tag', 'hero_title', 'hero_lead', 'partners_label')}),
        ("Bo'lim sarlavhalari", {'classes': ('collapse',), 'fields': (
            'why_title', 'why_sub', 'ind_title', 'ind_sub', 'cases_title', 'clients_title', 'clients_sub',
            'steps_title', 'steps_sub', 'team_title', 'team_sub')}),
        ('Ariza bloki', {'fields': ('cta_title', 'cta_text')}),
        ('Asoschi (Jamoa sahifasi)', {'classes': ('collapse',), 'fields': (
            'founder_name', 'founder_bio', 'founder_education', 'founder_experience', 'founder_expertise')}),
        ('Footer', {'fields': ('footer_about', 'footer_bottom')}),
        ('Telegram bildirishnoma', {'fields': ('tg_bot_token', 'tg_chat_id')}),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        # Ro'yxat o'rniga to'g'ridan-to'g'ri tahrirlash sahifasi
        obj = SiteSettings.load()
        return redirect(reverse('admin:core_sitesettings_change', args=[obj.pk]))
