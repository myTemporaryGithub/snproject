# Generated by Django 2.1.3 on 2018-11-19 22:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name='Creation time')),
                ('mtime', models.DateTimeField(auto_now=True, verbose_name='Update time')),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='friend', to=settings.AUTH_USER_MODEL)),
                ('initiator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='friend_initiator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name='Creation time')),
                ('mtime', models.DateTimeField(auto_now=True, verbose_name='Update time')),
                ('status', models.CharField(choices=[(1, 'pending'), (2, 'confirmed'), (3, 'rejected')], default=1, max_length=10)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='friend_request_receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='friend_request_sender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='friend',
            unique_together={('initiator', 'friend')},
        ),
    ]
