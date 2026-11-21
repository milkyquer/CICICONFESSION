from django.contrib import admin
from .models import AnonymousPost
from .models import PostReport


@admin.register(AnonymousPost)
class AnonymousPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'status', 'created_at')
    list_filter = ('category', 'status', 'created_at')
    search_fields = ('message',)
    list_editable = ('status',)
    ordering = ('-created_at',)


@admin.register(PostReport)
class PostReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'reason', 'created_at')
    list_filter = ('reason', 'created_at')