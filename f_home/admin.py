from django.contrib import admin
from .models import Post, CompanySize, LanguageStack

# Register your models here.
admin.site.register(LanguageStack)
admin.site.register(Post),
admin.site.register(CompanySize)