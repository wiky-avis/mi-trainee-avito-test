from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CreatePollViewSet, GetResultViewSet, PollViewSet

v1_router = DefaultRouter()
v1_router.register('createPoll', CreatePollViewSet, basename='create_poll')
v1_router.register('poll', PollViewSet, basename='vote_poll')
v1_router.register('getResult', GetResultViewSet, basename='get_result')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
