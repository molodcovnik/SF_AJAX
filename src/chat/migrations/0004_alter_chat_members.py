# Generated by Django 4.2.2 on 2023-07-09 19:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0003_chat_members_alter_chat_chat_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='members',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]