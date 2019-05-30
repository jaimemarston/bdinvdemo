# Generated by Django 2.0.8 on 2019-04-29 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionapp', '0030_articulo_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=60)),
                ('cantidad', models.IntegerField(default=0)),
                ('color', models.CharField(choices=[('0', 'Blanco'), ('1', 'Negro'), ('2', 'Rojo'), ('3', 'Amarillo'), ('4', 'Azul')], default=0, max_length=2)),
                ('descolor', models.CharField(blank=True, max_length=60, null=True)),
                ('stock1', models.IntegerField(default=0)),
                ('codbarra', models.CharField(blank=True, max_length=60, null=True)),
                ('stockalm1', models.IntegerField(default=0)),
                ('stockalm2', models.IntegerField(default=0)),
                ('stockalm3', models.IntegerField(default=0)),
                ('afectoigv', models.IntegerField(default=0)),
                ('preciocosto', models.IntegerField(default=0)),
                ('precioventa', models.IntegerField(default=0)),
                ('aplicadscto', models.IntegerField(default=0)),
                ('cc1', models.CharField(blank=True, max_length=60, null=True)),
                ('descc1', models.CharField(blank=True, max_length=60, null=True)),
                ('modelo', models.CharField(blank=True, max_length=60, null=True)),
                ('genero', models.CharField(blank=True, max_length=30, null=True)),
                ('talla', models.CharField(blank=True, max_length=30, null=True)),
                ('ruc', models.CharField(blank=True, max_length=11, null=True)),
                ('desruc', models.CharField(blank=True, max_length=60, null=True)),
                ('unimed', models.CharField(blank=True, max_length=30, null=True)),
                ('desunimed', models.CharField(blank=True, max_length=30, null=True)),
                ('umdsali', models.CharField(blank=True, max_length=30, null=True)),
                ('umdsaliconv', models.CharField(blank=True, max_length=30, null=True)),
                ('tipo', models.CharField(blank=True, max_length=60, null=True)),
                ('deposito', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestionapp.Deposito')),
            ],
        ),
    ]
