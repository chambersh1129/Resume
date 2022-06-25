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
        return super().get_queryset().prefetch_related("tags")


class Milestone(models.Model):
    class TypeChoices(models.TextChoices):
        JOB = "job", "Job"
        ROLE = "role", "Role"
        CERT = "cert", "Certification"
        EDU = "edu", "Education"
        PROJ = "proj", "Project"

    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
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


class Profile(models.Model):
    fullname = models.CharField(max_length=64)
    email = models.EmailField()
    bio = models.TextField()

    def __str__(self):
        return self.fullname

    @property
    def title(self):
        most_recent_role = self.milestone_set.filter(type="role").order_by("-start_date").first()
        most_recent_job = self.milestone_set.filter(type="job").order_by("-start_date").first()

        if not most_recent_role or not most_recent_role:
            return "n/a"

        return f"{most_recent_role} at {most_recent_job}"
