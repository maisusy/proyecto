# Generated by Django 3.1.1 on 2020-10-30 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('py', '0005_auto_20201029_2300'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avicola',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('raza', models.CharField(max_length=20)),
                ('sexo', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Manada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ovino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.FloatField()),
                ('calidad_de_lana', models.CharField(max_length=30)),
                ('padre', models.CharField(max_length=10)),
                ('madre', models.CharField(max_length=10)),
                ('PDP', models.BooleanField()),
                ('cant_de_dientes', models.IntegerField()),
                ('categoria_por_diente', models.CharField(max_length=10)),
                ('fecha_de_registro', models.DateField()),
                ('fecha_de_nacimiento', models.DateField()),
                ('raza', models.CharField(max_length=10)),
                ('seccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='py.seccion')),
            ],
        ),
        migrations.CreateModel(
            name='Equino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('color_pelaje', models.CharField(max_length=20)),
                ('condicion', models.CharField(max_length=30)),
                ('causa_de_muerte', models.CharField(max_length=30)),
                ('fecha_De_nacimiento', models.DateField()),
                ('raza', models.CharField(max_length=30)),
                ('sexo', models.CharField(max_length=6)),
                ('manada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='py.manada')),
                ('seccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='py.seccion')),
            ],
        ),
        migrations.CreateModel(
            name='Energia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=30)),
                ('fecha_de_instalacion', models.DateField()),
                ('estado', models.CharField(max_length=30)),
                ('descripcion_del_estado', models.CharField(max_length=200)),
                ('fecha_De_mantenimiento', models.DateField()),
                ('seccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='py.seccion')),
            ],
        ),
        migrations.CreateModel(
            name='Alambrado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cant_kilometros', models.FloatField()),
                ('materiales', models.CharField(max_length=200)),
                ('seccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='py.seccion')),
            ],
        ),
    ]
