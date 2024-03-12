from django.contrib import admin
from django.utils.html import mark_safe

from courses.models import Course, Category

class MyCourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date', 'update_date', 'active']
    search_fields = ['id', 'name']
    list_filter = ['created_date', 'name']
    readonly_fields = ['my_image']

    def my_image(self, course):
        if course.img:
            return mark_safe(f"<img src=' /static/{course.img.name}' width='200' >")

admin.site.register(Category)
admin.site.register(Course, MyCourseAdmin)