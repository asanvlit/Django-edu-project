from django.contrib import admin

from web.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'art_type', 'hours_spent', 'used_material', 'description', 'created_at', 'updated_at')


admin.site.register(Post, PostAdmin)
