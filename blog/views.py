from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, CommentSerializer, PostSerializer
from . import models
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes


# Create your views here.
