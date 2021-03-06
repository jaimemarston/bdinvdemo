# Generated by Django 2.0.8 on 2019-05-08 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionapp', '0037_auto_20190507_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='dcotizacion',
            name='genero',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='dcotizacion',
            name='modelo',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='dcotizacion',
            name='talla',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='dcotizacion',
            name='tipo',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='dgasto',
            name='genero',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='dgasto',
            name='modelo',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='dgasto',
            name='talla',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='dgasto',
            name='tipo',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='dguia',
            name='genero',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='dguia',
            name='modelo',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='dguia',
            name='talla',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='dguia',
            name='tipo',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='dmateriales',
            name='genero',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='dmateriales',
            name='modelo',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='dmateriales',
            name='talla',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='dmateriales',
            name='tipo',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
