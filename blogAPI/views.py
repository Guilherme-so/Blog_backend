from blog.models import Post
from .serializers import PostSerializers
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly,  BasePermission, SAFE_METHODS

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

#  Create your views here.

class IsOwnerOrReadOnly(BasePermission):
    message = 'only the author has the credential to updade and delete'
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user

class PostList(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializers
    queryset = Post.postobjects.all()

    # mostra o title em vez do Ud
    def get_object(self,queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, title=item)

    #custom query_set
    # def get_queryset(self):
    #     return Post.objects.all()
















# class PostList(viewsets.ViewSet):
#     permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
#     queryset = Post.postobjects.all()

#     def list(self, request):
#         serializer_class = PostSerializers(self.queryset, many=True)
#         return Response(serializer_class.data)

#     def retrieve(self, request, pk=None):
#         post  = get_object_or_404(self.queryset, pk=pk)
#         serializer_class = PostSerializers(post)
#         return Response(serializer_class.data)



#    def list(self, request):
#         pass

#     def create(self, request):
#         pass

#     def retrieve(self, request, pk=None):
#         pass

#     def update(self, request, pk=None):
#         pass

#     def partial_update(self, request, pk=None):
#         pass

#     def destroy(self, request, pk=None):
#         pass




# class PostList(generics.ListCreateAPIView,):
#     permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
#     queryset = Post.postobjects.all()
#     serializer_class = PostSerializers

# class PostDetail(generics.RetrieveUpdateDestroyAPIView, IsOwnerOrReadOnly):
#     permission_classes = [IsOwnerOrReadOnly]
#     queryset = Post.postobjects.all()
#     serializer_class = PostSerializers