from os import read
from rest_framework import serializers

from .models import (
    Hint,
    Project,
    Member,
    Article,
    AccessRequest,
)


class AccessRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccessRequest
        fields = ['id', 'link', 'template_content']


class ResourceSerializer(serializers.ModelSerializer):
    access_request = AccessRequestSerializer(many=False, read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'name', 'link', 'type', 'access_request']


class MemberSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Member
        fields = ['id', 'name', 'specialization', 'telegram', 'mail', 'phone']


class ProjectSerializer(serializers.ModelSerializer):
    members = MemberSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'purpose', 'issue', 'managment_info',
            'calendar_info', 'result_info', 'members',
        ]


class HintSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hint
        fields = ['target', 'name', 'comment']


class ArticleSerializer(serializers.ModelSerializer):
    source_hints = HintSerializer(many=True, read_only=True)

    prev_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    next_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Article
        fields = [
            'id', 'title', 'content', 'resource_link', 'video_link',
            'prev_id', 'next_id', 'source_hints',
        ]
