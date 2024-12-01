from rest_framework import serializers
from .models import Profile, Message

class ProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Profile
        fields = ['user_id', 'username', 'email', 'bio', 'location', 'birth_date']

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField(read_only=True)
    receiver = serializers.StringRelatedField(read_only=True)
    groups = serializers.StringRelatedField(many=True)

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'content', 'groups', 'timestamp', 'is_read']

class MessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['sender','receiver', 'content']

    # def create(self, validated_data):
    #     validated_data['sender'] = self.context['request'].user
    #     return super().create(validated_data)
    
class MessageUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['is_read']

class MessageDetailSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField(read_only=True)
    receiver = serializers.StringRelatedField(read_only=True)
    groups = serializers.StringRelatedField(many=True)

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'content', 'groups', 'timestamp', 'is_read']
    
