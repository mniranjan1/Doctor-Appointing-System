# Generated by Django 2.2.1 on 2019-07-18 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='experience',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doc',
            name='like',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doc',
            name='patient_experience',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]