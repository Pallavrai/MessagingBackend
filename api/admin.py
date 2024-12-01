from django.contrib import admin
from .models import Profile, Message, Group

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'location', 'birth_date')
    search_fields = ('user__username', 'bio', 'location')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'timestamp', 'content')
    search_fields = ('sender__username', 'receiver__username', 'content')
    list_filter = ('timestamp',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Group)