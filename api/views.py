from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Profile, Message
from django.shortcuts import get_object_or_404
from django.db.models import OuterRef, Subquery, Q
from rest_framework.response import Response


from .serializers import ProfileSerializer, MessageSerializer, MessageCreateSerializer,MessageDetailSerializer

class ProfileList(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    
    # def get_object(self):
    #     queryset = self.get_queryset()
    #     obj = get_object_or_404(queryset, user__username=self.kwargs['username'])
    #     return obj

class MessageList(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Message.objects.filter(profile__user=self.request.user)

class SendViewMessage(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = Message.objects.filter(Q(sender=self.request.user) | Q(receiver=self.request.user))
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)