from rest_framework import serializers
from blog.models import Post
'''
class Postserializers(serializers.Serializer):
    id = serializers.IntegerField()
    content = serializers.CharField(max_length=255)
    title = serializers.CharField(max_length=255)
'''

class Postserializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id","author","title","content","status"]