from django.db import models


class ChatLog(models.Model):
    message = models.TextField()
    reply = models.TextField(blank=True, null=True)
    error = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.created_at:%Y-%m-%d %H:%M} - {self.message[:40]}"
