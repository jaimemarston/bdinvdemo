# Generated by Django 2.0.8 on 2019-04-26 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionapp', '0029_auto_20190425_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='tipo',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
