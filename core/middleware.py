from django.utils import translation


class AdminUzbekMiddleware:
    """Admin panel har doim o'zbek tilida (brauzer tilidan qat'i nazar)."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/'):
            translation.activate('uz')
            request.LANGUAGE_CODE = 'uz'
        return self.get_response(request)
