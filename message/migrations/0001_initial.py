# Generated by Django 5.1.1 on 2024-09-15 21:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('topic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('content', models.TextField()),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_topic_ids', to='topic.topicmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
