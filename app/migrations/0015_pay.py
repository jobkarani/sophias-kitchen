# Generated by Django 3.2.9 on 2022-04-18 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_mpesapayment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=144, null=True)),
                ('last_name', models.CharField(blank=True, max_length=144, null=True)),
                ('contact', models.CharField(max_length=30)),
            ],
        ),
    ]
