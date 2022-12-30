from rest_framework import serializers
from blog.models import Post,Category

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id','name']


class PostSerializers(serializers.ModelSerializer):    
    class Meta:
        model = Post
        fields = ['id','title', 'author', 'excerpt', 'content', 'status']
