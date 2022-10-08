from django.db import models


# Create your models here.
class AnonymousLogs(models.Model):
    path = models.CharField(max_length=128)
    user_agent = models.CharField(max_length=128, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Anonymous Logs"
        verbose_name_plural = "Anonymous Logs"
        ordering = ["-timestamp"]

    def __str__(self):
        return f"{self.path}"
