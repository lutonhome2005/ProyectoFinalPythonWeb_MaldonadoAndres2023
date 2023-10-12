# Generated by Django 4.2.4 on 2023-09-09 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppGaleriaWeb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreArtista', models.CharField(max_length=50)),
                ('apellidoArtista', models.CharField(max_length=60)),
                ('nacionalidadArtista', models.CharField(max_length=50)),
                ('emailArtista', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='obraarte',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='obras', to='AppGaleriaWeb.artista'),
        ),
    ]
