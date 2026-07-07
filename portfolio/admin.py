from django.contrib import admin

from .models import ChatLog


@admin.register(ChatLog)
class ChatLogAdmin(admin.ModelAdmin):
    list_display = ("created_at", "message", "reply", "error")
    readonly_fields = ("created_at",)
    search_fields = ("message", "reply")
