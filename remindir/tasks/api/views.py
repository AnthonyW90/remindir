from django.conf import settings
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from tasks.api.permissions import IsCreatorOrReadOnly
from tasks.api.serializer import TaskGroupSerializer, TaskSerializer
from tasks.models import TaskGroup, Task


class TaskGroupViewSet(viewsets.ModelViewSet):
    queryset = TaskGroup.objects.all()
    lookup_field = 'slug'
    serializer_class = TaskGroupSerializer
    permission_classes = [IsCreatorOrReadOnly, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        return self.request.user.taskgroups.all().order_by('created_at')


class TaskCreateAPIView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        kwarg_slug = self.kwargs.get('slug')
        taskgroup = get_object_or_404(TaskGroup, slug=kwarg_slug)
        serializer.save(created_by=self.request.user, taskgroup=taskgroup)


class TaskListAPIView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get('slug')
        return Task.objects.filter(taskgroup__slug=kwarg_slug).order_by('created_at')


class TaskRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsCreatorOrReadOnly]
