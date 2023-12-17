from rest_framework import serializers
from blog.models import Post,Category
from accounts.models import Profile
'''
class Postserializers(serializers.Serializer):
    id = serializers.IntegerField()
    content = serializers.CharField(max_length=255)
    title = serializers.CharField(max_length=255)
'''
class Categoryserializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id","name"] 
        
        
class Postserializers(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source = 'get_snippet')
    relative_url = serializers.URLField(source = "get_absolute_api_url",read_only = True)
    absolute_urls = serializers.SerializerMethodField()
    category = serializers.SlugRelatedField(many=False,slug_field='name',queryset= Category.objects.all())
    class Meta:
        model = Post
        fields = ["id","author","title","image","content","snippet","relative_url","absolute_urls","status","category"]
        read_only_fields = ["author"]
    def get_absolute_urls(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)
    
    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('relative_url',None)
            rep.pop('absolute_urls',None)
            rep.pop('snippet',None)
        else:
            rep.pop('content',None)
        rep['category'] = Categoryserializers(instance.category,context={'request':request}).data
        return rep

    def create(self, validated_data):
        validated_data['author'] = Profile.objects.get(user__id=self.context.get('request').user.id)
        return super().create(validated_data)