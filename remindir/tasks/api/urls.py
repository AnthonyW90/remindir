from django.urls import include, path
from rest_framework.routers import DefaultRouter
from tasks.api import views as v

router = DefaultRouter()
router.register(r"taskgroups", v.TaskGroupViewSet)

urlpatterns = [
    path('', include(router.urls))
]
