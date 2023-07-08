# Generated by Django 4.2.2 on 2023-07-08 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_name', models.TextField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('messages', models.ManyToManyField(blank=True, to='chat.message')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]