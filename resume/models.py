from datetime import datetime

from django.db import models


class Hobby(models.Model):
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.TextField()
    img = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class MilestoneManager(models.Manager):
    # Always prefect_related tags to reduce DB calls
    def get_queryset(self):
        return super().get_queryset().prefetch_related("tag")


class Milestone(models.Model):
    class TypeChoices(models.TextChoices):
        ROLE = "role", "Role"
        CERT = "cert", "Certification"
        EDU = "edu", "Education"
        PROJ = "proj", "Project"

    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.TextField()
    type = models.CharField(max_length=4, choices=TypeChoices.choices)
    tag = models.ManyToManyField("tag", blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True)

    objects = MilestoneManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-start_date"]

    def tags(self):
        return [str(tag) for tag in self.tag.all()]

    @property
    def total_time(self):
        total_time = (self.end_date or datetime.now()) - self.start_date
        return f"{total_time.days} days"


class Tag(models.Model):
    tag = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.tag


class Profile(models.Model):
    fullname = models.CharField(max_length=64)
    email = models.EmailField(null=True)
    bio = models.TextField()
    github = models.URLField(null=True)
    linkedin = models.URLField(null=True)

    def __str__(self):
        return self.fullname

    @property
    def title(self):
        most_recent_role = self.milestone_set.filter(type="role").order_by("-start_date").first()

        if most_recent_role.end_date:
            return "Currently seeking new opportunities"

        return f"{most_recent_role}"
