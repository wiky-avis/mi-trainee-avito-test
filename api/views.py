from django.shortcuts import get_object_or_404
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from polls.models import Choice, Poll

from .serializers import (PollListPageSerializer, PollResultPageSerializer,
                          VoteSerializer)


class CreatePollViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    queryset = Poll.objects.all()
    serializer_class = PollListPageSerializer


class PollViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet):

    queryset = Poll.objects.all()
    serializer_class = PollListPageSerializer

    def update(self, request, *args, **kwargs):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        serializer = VoteSerializer(data=request.data)
        if serializer.is_valid():
            choice = get_object_or_404(
                Choice,
                pk=serializer.validated_data['choice_id'],
                poll=poll)
            choice.votes += 1
            choice.save()
            return Response('Ваш голос принят.')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetResultViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    queryset = Poll.objects.all()
    serializer_class = PollResultPageSerializer
