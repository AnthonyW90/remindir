from rest_framework import serializers

from tasks.models import Task, TaskGroup


class TaskSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    completed = serializers.BooleanField()
    group_slug = serializers.SerializerMethodField()

    class Meta:
        model = Task
        exclude = ['taskgroup', 'updated_at']

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

    def get_group_slug(self, instance):
        return instance.taskgroup.slug


class TaskGroupSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)
    task_count = serializers.SerializerMethodField()

    class Meta:
        model = TaskGroup
        exclude = ['updated_at']

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

    def get_task_count(self, instance):
        return instance.tasks.count()
