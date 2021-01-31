from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, CommentSerializer, PostSerializer
from . import models
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request):
        serializer = PostSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True) #check all fields is valid
        serializer.save(user=request.user)
        return Response(serializer.data)

    @action(detail=False, methods=['POST','GET'])
    def comment(self, request, pk):
        post = models.Post.objects.get(pk=pk)
        self.serializer_class = CommentSerializer
        queryset = models.Comment.objects.filter(post=post)

        if request.method == "GET":
            serializer = CommentSerializer(queryset, many=True,context={'request':request})
        else:
            serializer = CommentSerializer(data=request.data,context={'request':request})
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user,post=post)
        return Response(serializer.data)

    @action(detail=False, methods=['DELETE',])
    def remove_comment(self, request, pk, comment):
        comment = models.Comment.objects.get(pk=comment)
        if comment.delete():
            return Response({'message': "Comment deleted"})
        else:
            return Response({'message':  "Unable to delete comment"})
