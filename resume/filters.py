from rest_framework.compat import coreapi, coreschema
from rest_framework.filters import BaseFilterBackend

from .models import Milestone


class MilestoneFilterSet(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        params = request.query_params

        if "milestone" in params:
            queryset = queryset.filter(name__icontains=params.get("milestone"))

        if "description" in params:
            queryset = queryset.filter(description__icontains=params.get("desc"))

        if "type" in params:
            queryset = queryset.filter(type__icontains=params.get("type"))

        if "tag" in params:
            queryset = queryset.filter(tag__tag__icontains=params.get("tag"))

        return queryset

    def get_schema_fields(self, view):
        assert coreapi is not None
        assert coreschema is not None
        return [
            coreapi.Field(
                name="milestone",
                required=False,
                location="query",
                schema=coreschema.String(description="Filter by the name of the Milestone."),
            ),
            coreapi.Field(
                name="description",
                required=False,
                location="query",
                schema=coreschema.String(description="Search within the Milestone description."),
            ),
            coreapi.Field(
                name="tag",
                required=False,
                location="query",
                schema=coreschema.String(description="Filter by Milestone tag."),
            ),
            coreapi.Field(
                name="type",
                required=False,
                location="query",
                schema=coreschema.String(
                    description=f"Filter by Milestone type.  Valid choices: {', '.join(Milestone.TypeChoices.values)}"
                ),
            ),
        ]


class WorkHistoryFilterSet(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        params = request.query_params

        if "company" in params:
            queryset = queryset.filter(company__icontains=params.get("company"))

        if "title" in params:
            queryset = queryset.filter(title__icontains=params.get("title"))

        if "description" in params:
            queryset = queryset.filter(description__icontains=params.get("description"))

        if "year" in params:
            queryset = queryset.filter(start_date__year__lte=params.get("year"), end_date__year__gte=params.get("year"))

        return queryset

    def get_schema_fields(self, view):
        assert coreapi is not None
        assert coreschema is not None
        return [
            coreapi.Field(
                name="company",
                required=False,
                location="query",
                schema=coreschema.String(description="Filter by the company."),
            ),
            coreapi.Field(
                name="title",
                required=False,
                location="query",
                schema=coreschema.String(description="Filter by the job title."),
            ),
            coreapi.Field(
                name="description",
                required=False,
                location="query",
                schema=coreschema.String(description="Search within the description."),
            ),
            coreapi.Field(
                name="year",
                required=False,
                location="query",
                schema=coreschema.Integer(description="Filter by the year."),
            ),
        ]


class TagFilterSet(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        params = request.query_params

        if "tag" in params:
            queryset = queryset.filter(tag__icontains=params.get("tag"))

        return queryset

    def get_schema_fields(self, view):
        assert coreapi is not None
        assert coreschema is not None
        return [
            coreapi.Field(
                name="tag",
                required=False,
                location="query",
                schema=coreschema.String(description="Search tag names."),
            ),
        ]
