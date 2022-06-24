from django.db import models


class Hobby(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    img = models.URLField()

    def __str__(self):
        return self.title


class MilestoneManager(models.Manager):
    # Always prefect_related tags to reduce DB calls
    def get_queryset(self):
        return super().get_queryset().prefetch_related("tags")


class Milestone(models.Model):
    class TypeChoices(models.TextChoices):
        JOB = "job", "Job"
        ROLE = "role", "Role"
        CERT = "cert", "Certification"
        EDU = "edu", "Education"
        PROJ = "proj", "Project"

    title = models.CharField(max_length=64)
    description = models.TextField()
    type = models.CharField(max_length=4, choices=TypeChoices.choices)
    tags = models.ManyToManyField("tag", blank=True)
    start_date = models.DateField()
    end_date = models.DateField()

    objects = MilestoneManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["start_date"]


class Tag(models.Model):
    tag = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.tag
