from django.contrib import admin

from web.models import Post, PostTag


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'art_type', 'user', 'hours_spent', 'used_material', 'description', 'created_at', 'updated_at')
    search_fields = ('id', 'art_type')
    list_filter = ('created_at', 'updated_at', 'user')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')


class PostTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user')
    search_fields = ('id', 'title')
    list_filter = ('user',)


admin.site.register(Post, PostAdmin)
admin.site.register(PostTag, PostTagAdmin)
