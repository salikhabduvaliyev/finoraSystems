"""Qaysi maydonlar 3 tilda (uz/en/ru) saqlanishi — django-modeltranslation."""
from modeltranslation.translator import TranslationOptions, register

from .models import Case, Industry, Presentation, Service, SiteSettings, Stat, Step, TeamMember, Value, WhyCard


@register(Service)
class ServiceTR(TranslationOptions):
    fields = ('title', 'subtitle', 'items')


@register(Industry)
class IndustryTR(TranslationOptions):
    fields = ('title', 'label', 'short', 'pains', 'solutions', 'ai', 'web', 'description')


@register(Case)
class CaseTR(TranslationOptions):
    fields = ('title', 'client', 'description', 'direction', 'tags', 'duration', 'result',
              'challenge', 'solution', 'works', 'metrics', 't_text', 't_role')


@register(TeamMember)
class TeamMemberTR(TranslationOptions):
    fields = ('role', 'intro', 'bio', 'skills', 'experience', 'education', 'achievements')


@register(Stat)
class StatTR(TranslationOptions):
    fields = ('value', 'label')


@register(WhyCard)
class WhyCardTR(TranslationOptions):
    fields = ('title', 'text')


@register(Step)
class StepTR(TranslationOptions):
    fields = ('title', 'text')


@register(Value)
class ValueTR(TranslationOptions):
    fields = ('title', 'text')


@register(SiteSettings)
class SiteSettingsTR(TranslationOptions):
    fields = ('meta_description', 'address', 'hero_tag', 'hero_title', 'hero_lead', 'partners_label',
              'why_title', 'why_sub', 'ind_title', 'ind_sub', 'cases_title', 'clients_title', 'clients_sub',
              'steps_title', 'steps_sub', 'team_title', 'team_sub', 'cta_title', 'cta_text',
              'founder_bio', 'founder_education', 'founder_experience', 'founder_expertise',
              'footer_about', 'footer_bottom')


@register(Presentation)
class PresentationTR(TranslationOptions):
    fields = ('title',)
