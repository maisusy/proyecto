# Generated by Django 3.1.1 on 2020-11-04 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('py', '0006_alambrado_avicola_energia_equino_manada_ovino_seccion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fecha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('titulo', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=500)),
                ('horadesde', models.DateTimeField()),
                ('horahasta', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='persona',
            name='direccion',
        ),
        migrations.AddField(
            model_name='persona',
            name='direccion',
            field=models.ManyToManyField(to='py.Direccion'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='rol',
            field=models.CharField(choices=[('DÑ', 'Dueño'), ('ENC', 'Encargado'), ('CZ', 'Capataz'), ('PG', 'Peon General'), ('PC', 'Peon Comun'), ('CAS', 'Casero'), ('PUES', 'Puestero'), ('QUIN', 'Quintero'), ('ESQ', 'Esquilador'), ('COC', 'Cocinero')], default='PC', max_length=4),
        ),
        migrations.AlterField(
            model_name='persona',
            name='telefono',
            field=models.CharField(max_length=10),
        ),
    ]