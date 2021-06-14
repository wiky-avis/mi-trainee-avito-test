from polls.models import Poll
from rest_framework import mixins, viewsets

from .serializers import PollListPageSerializer


class CreatePollViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    queryset = Poll.objects.all()
    serializer_class = PollListPageSerializer


class PollViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet):

    pass


class GetResultViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    pass
