from django.urls import include, path
from rest_framework.routers import DefaultRouter
from tasks.api import views as v

router = DefaultRouter()
router.register(r"taskgroups", v.TaskGroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('taskgroups/<slug:slug>/tasks/',
         v.TaskListAPIView.as_view(), name='task-list'),
    path('taskgroups/<slug:slug>/task/',
         v.TaskCreateAPIView.as_view(), name='task-create'),
    path('task/<int:pk>/',
         v.TaskRUDAPIView.as_view(), name='task-detail')
]
