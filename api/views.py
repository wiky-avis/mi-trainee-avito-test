from rest_framework import mixins, viewsets



class CreatePollViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    pass


class PollViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet):

    pass


class GetResultViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    pass
