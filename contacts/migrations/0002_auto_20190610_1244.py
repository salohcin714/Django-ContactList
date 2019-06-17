# Generated by Django 2.2.1 on 2019-06-10 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='name',
        ),
        migrations.AddField(
            model_name='contact',
            name='city',
            field=models.CharField(default='null', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='first_name',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='last_name',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='state',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='zip',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.CharField(max_length=64),
        ),
    ]
