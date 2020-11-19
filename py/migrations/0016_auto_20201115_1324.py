# Generated by Django 3.1.1 on 2020-11-15 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('py', '0015_auto_20201114_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='alimento',
            name='tipo',
            field=models.CharField(choices=[('A', 'Animal'), ('H', 'Humano')], default='A', max_length=1),
        ),
        migrations.AddField(
            model_name='fecha',
            name='lugar',
            field=models.ForeignKey(default='Killik Aike', on_delete=django.db.models.deletion.CASCADE, to='py.seccion'),
        ),
        migrations.AddField(
            model_name='insumo',
            name='estado',
            field=models.CharField(choices=[('BUEN_ENSTADO', 'Buen estado'), ('MAL_ESTADO', 'Mal estado'), ('PRESTADO', 'Prestado')], default='BUEN_ENSTADO', max_length=16),
        ),
        migrations.AlterField(
            model_name='avicola',
            name='raza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='py.raza'),
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('E', 'Enfermo'), ('L', 'Licencia'), ('T', 'Dia trabajado'), ('NT', 'Dia no trabajado')], default='T', max_length=2)),
                ('fecha', models.DateField()),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='py.persona')),
            ],
        ),
    ]
