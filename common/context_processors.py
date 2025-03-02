from django.conf import settings
def get_languages(request):
    return settings.LANGUAGES
        