from django.conf import settings
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from tasks.api.permissions import IsCreatorOrReadOnly
from tasks.api.serializer import TaskGroupSerializer
from tasks.models import TaskGroup


class TaskGroupViewSet(viewsets.ModelViewSet):
    queryset = TaskGroup.objects.all()
    lookup_field = 'slug'
    serializer_class = TaskGroupSerializer
    permission_classes = [IsCreatorOrReadOnly, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
