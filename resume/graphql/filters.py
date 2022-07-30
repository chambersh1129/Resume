from datetime import datetime

import django_filters
from django.core.validators import MaxValueValidator
from django.db.models import Q

from resume.models import Hobby, Milestone, Tag, WorkHistory


class HobbyFilter(django_filters.FilterSet):
    class Meta:
        model = Hobby
        fields = ["id", "hobby", "description"]


class MilestoneFilter(django_filters.FilterSet):
    type = django_filters.ChoiceFilter(choices=Milestone.TypeChoices.choices)
    tag = django_filters.ModelMultipleChoiceFilter(
        field_name="tag__tag", to_field_name="tag", queryset=Tag.objects.all()
    )

    class Meta:
        model = Milestone
        fields = ["id", "name", "description", "type", "tag"]


class TagFilter(django_filters.FilterSet):
    class Meta:
        model = Tag
        fields = ["id", "tag"]


class WorkHistoryYearFilter(django_filters.NumberFilter):
    def get_max_validator(self):
        """
        Return a MaxValueValidator for the field, or None to disable.
        """
        return MaxValueValidator(datetime.now().year + 1)


class WorkHistoryFilter(django_filters.FilterSet):
    year = WorkHistoryYearFilter(method="year_of_employment")

    class Meta:
        model = WorkHistory
        fields = ["id", "company", "title", "description"]

    def year_of_employment(self, queryset, name, value):
        return queryset.filter(start_date__year__lte=value).filter(
            Q(end_date__year__gte=value) | Q(end_date__year__isnull=True)
        )
