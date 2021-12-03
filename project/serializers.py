from rest_framework import serializers

from .models import (
    Project,
    Member,
    Resource,
    AccessRequest,
)


class AccessRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccessRequest
        fields = ['id', 'link', 'template_content']


class ResourceSerializer(serializers.ModelSerializer):
    access_request = AccessRequestSerializer(many=False, read_only=True)

    class Meta:
        model = Resource
        fields = ['id', 'name', 'link', 'type', 'access_request']


class MemberSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Member
        fields = ['id', 'name', 'specialization', 'telegram', 'mail', 'phone']


class ProjectSerializer(serializers.ModelSerializer):
    members = MemberSerializer(many=True, read_only=True)
    resources = ResourceSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'purpose', 'issue', 'managment_info',
            'calendar_info', 'result_info', 'members', 'resources'
        ]
