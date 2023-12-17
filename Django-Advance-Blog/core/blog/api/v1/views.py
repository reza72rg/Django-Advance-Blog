from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework.response import Response
from .serializers import Postserializers,Categoryserializers
from blog.models import Post,Category
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView \
    , ListCreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView \
       , RetrieveUpdateDestroyAPIView
from rest_framework import mixins
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from .pagination import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class PostListModuleSet(viewsets.ModelViewSet):
    permission_classes =[IsAuthenticated,IsOwnerOrReadOnly]
    serializer_class = Postserializers
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        "author": ["exact","in"],
        "category": ["exact","in"],
  
    }
    search_fields = ['=title', 'content']
    ordering_fields = ['created_date']
    pagination_class = CustomPagination
    
class CategoryListModuleSet(viewsets.ModelViewSet):
    permission_classes =[IsAuthenticated]
    serializer_class = Categoryserializers
    queryset = Category.objects.all()
    




'''
class PostListViewSet(viewsets.ViewSet):
    permission_classes =[IsAuthenticated]
    serializer_class = Postserializers
    queryset = Post.objects.filter(status=True)
    
    def list(self, request):
        serializer = self.serializer_class(Post.objects.filter(status=True), many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        post_object = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(post_object)
        return Response(serializer.data)
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response(serializer.data)

    def update(self, request, pk=None):
        post_object = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(post_object, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
  

    def partial_update(self, request, pk=None):
        pass
    def destroy(self, request, pk=None):
        post_object = get_object_or_404(self.queryset, pk=pk)
        post_object.delete()
        return Response({'detail':"Item removed successfully"},status=status.HTTP_204_NO_CONTENT) 

   
class PostList(ListCreateAPIView):
    queryset = Post.objects.filter(status=True)
    permission_classes =[IsAuthenticated]
    serializer_class = Postserializers
    
'''

'''class PostList(GenericAPIView,mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Post.objects.filter(status=True)
    permission_classes =[IsAuthenticated]
    serializer_class = Postserializers
    
    def get(self,request,*args,**kwargs):
        return self.list(request, *args, **kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)
 
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
        return Response(serializer.data)
        
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
  



class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes =[IsAuthenticated]
    serializer_class = Postserializers
    queryset = Post.objects.filter(status=True)
    #lookup_field = 'id'
     

class PostDetail(GenericAPIView,mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    permission_classes =[IsAuthenticated]
    serializer_class = Postserializers
    queryset = Post.objects.filter(status=True)
    #lookup_field = 'id'
    
    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    def put(self,request,*args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self,request,*args, **kwargs):
        return self.destroy(request, *args, **kwargs)
        
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
