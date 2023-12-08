from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework.response import Response
from .serializers import Postserializers 
from blog.models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
 
    
''' 
class PostList(APIView):
    permission_classes =[IsAuthenticated]
    serializer_class = Postserializers
    def get(self,request):
        posts = Post.objects.filter(status=True)
        serializer = Postserializers(posts,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = Postserializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response(serializer.data)'''
class PostDetail(APIView):
    permission_classes =[IsAuthenticated]
    serializer_class = Postserializers
    def setup(self, request, *args, **kwargs):
        self.instance_post = get_object_or_404(Post,pk=kwargs['id'],status=True)
        return super().setup(request, *args, **kwargs)
    
    def get(self,request,*args, **kwargs):
        serializer = Postserializers(self.instance_post)
        return Response(serializer.data)
    def put(self,request,*args, **kwargs):
        serializer = Postserializers(self.instance_post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self,request,*args, **kwargs):
        self.instance_post.delete()
        return Response({'detail':"Item removed successfully"},status=status.HTTP_204_NO_CONTENT)

'''   
@api_view(["GET","POST"])  
@permission_classes([IsAuthenticatedOrReadOnly]) 
def PostList(request):
    if request.method =="GET":
        posts = Post.objects.filter(status=True)
        serializer = Postserializers(posts,many=True)
        return Response(serializer.data)
    elif request.method =="POST":
        serializer = Postserializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response(serializer.data)
  
@api_view(["GET","PUT","DELETE"])    
def PostDetail(request,id):
    post = get_object_or_404(Post,pk=id,status=True)
    if request.method == "GET":
        serializer = Postserializers(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = Postserializers(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response({'detail':"Item removed successfully"},status=status.HTTP_204_NO_CONTENT)
'''
