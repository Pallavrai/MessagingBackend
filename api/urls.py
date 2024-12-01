from django.urls import path
from .views import ProfileList, MessageList, MessageDetail, SendViewMessage

urlpatterns = [
   path('profile/<pk>', ProfileList.as_view(), name='profile-list'),
    path('message/', SendViewMessage.as_view(), name='message'),
    path('message/<pk>', MessageDetail.as_view(), name='message-detail'),

]