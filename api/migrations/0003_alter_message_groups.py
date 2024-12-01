# Generated by Django 5.1.3 on 2024-11-27 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_message_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='group_messages', to='api.group'),
        ),
    ]
