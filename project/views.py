from django.db.models import query
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from django.http import JsonResponse

from .serializers import ArticleSerializer, HintSerializer, ProjectSerializer
from .models import Article, Hint, Project

# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all().select_related()


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all().select_related()


class HintViewSet(viewsets.ModelViewSet):
    serializer_class = HintSerializer
    queryset = Hint.objects.all().select_related()


def articles(request):
    current_article = Article.objects.filter(pk=1).first().get_json()
    other_articles = [a.get_json() for a in Article.objects.all()]
    return JsonResponse({
        "current_article": current_article,
        "other_articles": other_articles,
    }, status=200)
