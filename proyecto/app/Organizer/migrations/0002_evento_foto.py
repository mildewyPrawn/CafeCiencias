# Generated by Django 2.2.5 on 2020-05-22 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organizer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]