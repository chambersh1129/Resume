from datetime import datetime

from django.db import models


class TimeRangeAbstractModel(models.Model):
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    class Meta:
        abstract = True

    @property
    def total_time(self):
        if not self.start_date:
            return "n/a"

        total_time = (self.end_date or datetime.now()) - self.start_date
        return f"{total_time.days} days"


class AboutMe(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    bio = models.TextField()
    email = models.EmailField(null=True)
    github = models.URLField(null=True)
    linkedin = models.URLField(null=True)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def title(self):
        most_recent_role = JobRole.objects.order_by("-start_date").first()

        if most_recent_role.end_date:
            return "Currently seeking new opportunities"

        return f"{most_recent_role}"


class Hobby(models.Model):
    hobby = models.CharField(max_length=64)
    description = models.TextField()
    img = models.URLField()

    def __str__(self):
        return self.title


class JobRole(TimeRangeAbstractModel):
    company = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    description = models.TextField()
    img = models.URLField()

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        return f"{self.title} at {self.company}"


class MilestoneManager(models.Manager):
    # Always prefect_related tags to reduce DB calls
    def get_queryset(self):
        return super().get_queryset().prefetch_related("tag")


class Milestone(TimeRangeAbstractModel):
    class TypeChoices(models.TextChoices):
        ROLE = "role", "Role"
        CERT = "cert", "Certification"
        EDU = "edu", "Education"
        PROJ = "proj", "Project"

    name = models.CharField(max_length=64)
    description = models.TextField()
    type = models.CharField(max_length=4, choices=TypeChoices.choices)
    tag = models.ManyToManyField("tag", blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True)

    objects = MilestoneManager()

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        return self.title

    def tags(self):
        return [str(tag) for tag in self.tag.all()]


class Tag(models.Model):
    tag = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.tag
