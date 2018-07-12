# Generated by Django 2.0.7 on 2018-07-11 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gateway', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='block_num',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='transfer',
            name='is_valid_memo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='transfer',
            name='memo',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
