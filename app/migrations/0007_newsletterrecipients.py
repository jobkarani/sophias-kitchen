# Generated by Django 3.2.9 on 2022-01-06 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_profile_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetterRecipients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
