from .production import *


INSTALLED_APPS = [
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.contrib.simple_translation",
    "django.contrib.sitemaps",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail.locales",
    "wagtail",
    "modelcluster",
    "taggit",
    "wagtailcodeblock",
    "thoth.home",
] + INSTALLED_APPS

MIDDLEWARE = MIDDLEWARE + [
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

TEMPLATES[0]["OPTIONS"]["context_processors"] += [
    "wagtail.contrib.settings.context_processors.settings",
]

WAGTAIL_SITE_NAME = env("WAGTAIL_SITE_NAME", default="Thoth Site")
WAGTAILADMIN_BASE_URL = env("WAGTAILADMIN_BASE_URL", default="https://example.com")
WAGTAIL_CMS_URL = env("WAGTAIL_CMS_URL", default="cms/")
WAGTAILEMBEDS_RESPONSIVE_HTML = True
WAGTAILDOCS_EXTENSIONS = [
    "csv",
    "docx",
    "key",
    "odt",
    "pdf",
    "pptx",
    "rtf",
    "txt",
    "xlsx",
    "zip",
]

WAGTAIL_I18N_ENABLED = True


WAGTAIL_CONTENT_LANGUAGES = LANGUAGES = [
    ('en', "English"),
    ('ru', "Russian"),
]