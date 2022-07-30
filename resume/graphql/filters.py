import django_filters

from resume.models import Hobby, Milestone, Tag, WorkHistory


class HobbyFilter(django_filters.FilterSet):
    hobby = django_filters.CharFilter(lookup_expr="icontains")
    description = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Hobby
        fields = ["id", "hobby", "description"]


class MilestoneFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    description = django_filters.CharFilter(lookup_expr="icontains")
    type = django_filters.ChoiceFilter(
        choices=Milestone.TypeChoices.choices, lookup_expr="icontains", label="this is a test"
    )
    tag = django_filters.ModelMultipleChoiceFilter(
        field_name="tag__tag", to_field_name="tag__icontains", queryset=Tag.objects.all()
    )

    class Meta:
        model = Milestone
        fields = ["id", "description", "type", "tag"]


class TagFilter(django_filters.FilterSet):
    tag = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Tag
        fields = ["id", "tag"]


class WorkHistoryFilter(django_filters.FilterSet):
    company = django_filters.CharFilter(lookup_expr="icontains")
    title = django_filters.CharFilter(lookup_expr="icontains")
    description = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = WorkHistory
        fields = ["id", "company", "title", "description", "start_date", "end_date"]
