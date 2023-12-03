from rest_framework import serializers

class Postserializers(serializers.Serializer):
    id = serializers.IntegerField()
    #Author =serializers.
    content = serializers.CharField(max_length=255)
    title = serializers.CharField(max_length=255)
