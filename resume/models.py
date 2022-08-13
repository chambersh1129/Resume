from datetime import datetime

from django.db import models


class AboutMe(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    bio = models.TextField()
    email = models.EmailField(null=True)
    github = models.URLField(null=True)
    linkedin = models.URLField(null=True)

    class Meta:
        verbose_name = "About Me"
        verbose_name_plural = "About Me"

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def title(self):
        most_recent_role = WorkHistory.objects.order_by("-start_date").first()

        if most_recent_role.end_date:
            return "Currently seeking new opportunities"

        return f"{most_recent_role}"

    @property
    def html_bio(self):
        return "<br>".join(self.bio.split("\n"))


class Hobby(models.Model):
    hobby = models.CharField(max_length=64)
    description = models.TextField()
    img = models.CharField(max_length=64)

    class Meta:
        ordering = ["hobby"]
        verbose_name = "Hobby"
        verbose_name_plural = "Hobbies"

    def __str__(self):
        return self.hobby

    @property
    def html_description(self):
        return "<br>".join(self.description.split("\n"))


class MilestoneManager(models.Manager):
    # Always prefect_related tags to reduce DB calls
    def get_queryset(self):
        return super().get_queryset().prefetch_related("tag")


class Milestone(models.Model):
    class TypeChoices(models.TextChoices):
        CERT = "cert", "Certification"
        CONF = "conf", "Conference"
        EDU = "edu", "Education"
        PROJ = "proj", "Project"

    name = models.CharField(max_length=64)
    description = models.TextField()
    type = models.CharField(max_length=4, choices=TypeChoices.choices)
    tag = models.ManyToManyField("tag", blank=True)

    objects = MilestoneManager()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    @property
    def type_label(self):
        return Milestone.TypeChoices(self.type).label

    @property
    def html_description(self):
        return "<br>".join(self.description.split("\n"))

    def tags(self):
        return [str(tag) for tag in self.tag.all()]


class Tag(models.Model):
    tag = models.CharField(max_length=32, unique=True)

    class Meta:
        ordering = ["tag"]

    def __str__(self):
        return self.tag


class WorkHistory(models.Model):
    company = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    description = models.TextField()
    img = models.URLField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ["-start_date"]
        verbose_name = "Work History"
        verbose_name_plural = "Work History"

    def __str__(self):
        return f"{self.title} at {self.company}"

    @property
    def total_time(self):
        if not self.start_date:
            return "n/a"

        total_time = (self.end_date or datetime.now().date()) - self.start_date
        return f"{round(total_time.days / 365, 2)} years"

    @property
    def html_description(self):
        return "<br>".join(self.description.split("\n"))
