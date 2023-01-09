# Generated by Django 4.1.4 on 2022-12-29 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_delete_notificationmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notif_for', models.CharField(max_length=200, verbose_name='Notification For')),
                ('notif_subject', models.CharField(max_length=200, verbose_name='Notification Subject')),
                ('notif_created_time', models.DateTimeField(auto_now_add=True, verbose_name='Notification Time')),
                ('notif_status', models.BooleanField(default=False)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.student')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.teacher')),
            ],
            options={
                'verbose_name_plural': '10. Notifications Assignment',
            },
        ),
    ]
