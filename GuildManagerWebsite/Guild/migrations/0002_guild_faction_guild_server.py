# Generated by Django 4.2.5 on 2023-10-02 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guild', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guild',
            name='faction',
            field=models.CharField(default='Alliance', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='guild',
            name='server',
            field=models.CharField(default='Arugal', max_length=50),
            preserve_default=False,
        ),
    ]
