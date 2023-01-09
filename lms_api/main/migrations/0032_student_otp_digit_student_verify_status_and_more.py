# Generated by Django 4.1.4 on 2023-01-04 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_faq'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='otp_digit',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='verify_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacher',
            name='otp_digit',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='verify_status',
            field=models.BooleanField(default=False),
        ),
    ]
