# Generated by Django 2.1.2 on 2018-11-29 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet_management', '0003_drive_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='drive',
            name='end_location',
            field=models.CharField(default='Warsaw', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='drive',
            name='start_location',
            field=models.CharField(default='Warsaw', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='drive',
            name='description',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]