from django.contrib import admin
from.models import *

# Register your models here.
admin.site.register(Contact)
admin.site.register(Blog)
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'image')