"""Dogsting."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Dogsting Task."""

    class Meta:
        """Dogstring m."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
