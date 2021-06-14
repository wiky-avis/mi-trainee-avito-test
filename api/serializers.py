from polls.models import Choice, Poll
from rest_framework import serializers


class VoteSerializer(serializers.Serializer):
    choice_id = serializers.IntegerField()


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ('id', 'choice_text', 'votes')


class PollListPageSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, write_only=True)

    class Meta:
        model = Poll
        fields = ('id', 'title', 'description', 'pub_date', 'choices')

    def create(self, validated_data):
        choices = validated_data.pop('choices', [])
        poll = Poll.objects.create(**validated_data)
        for choice_dict in choices:
            choice_dict['poll'] = poll
            Choice.objects.create(**choice_dict)
        return poll
