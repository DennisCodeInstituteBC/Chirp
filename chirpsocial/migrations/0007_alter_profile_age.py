# Generated by Django 4.2.16 on 2024-10-10 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chirpsocial', '0006_alter_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
