from django.contrib import admin
from .models import Gallery
from .form import GalleryForm

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    """ Gallery Admin """
    form = GalleryForm

