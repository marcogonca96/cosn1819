# Generated by Django 2.1.4 on 2018-12-05 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogue',
            name='image',
            field=models.ImageField(null=True, upload_to='img'),
        ),
    ]
