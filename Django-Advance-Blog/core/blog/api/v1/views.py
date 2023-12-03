from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Postserializers 
from blog.models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view()  
def PostList(request):
    posts = Post.objects.filter(status=True)
    serializer = Postserializers(posts,many=True)
    return Response(serializer.data)

@api_view()  
def PostDetail(request,id):
    post = get_object_or_404(Post,pk=id,status=True)
    serializer = Postserializers(post)
    return Response(serializer.data)
