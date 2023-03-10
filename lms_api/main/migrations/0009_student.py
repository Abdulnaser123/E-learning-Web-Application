# Generated by Django 4.1.4 on 2022-12-22 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=200)),
                ('interested_categories', models.TextField()),
            ],
            options={
                'verbose_name_plural': '5. Students',
            },
        ),
    ]
