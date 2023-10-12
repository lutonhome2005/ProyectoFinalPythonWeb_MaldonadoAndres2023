# Generated by Django 4.2.4 on 2023-09-09 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='ObraArte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('descripcion', models.TextField()),
                ('autor', models.CharField(max_length=100)),
                ('precio', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('imagen', models.ImageField(upload_to='')),
                ('fechaCreacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreUsuario', models.CharField(max_length=50)),
                ('apellidoUsuario', models.CharField(max_length=60)),
                ('edadUsuario', models.IntegerField()),
                ('emailUsuario', models.EmailField(max_length=254, unique=True)),
                ('carrito', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AppGaleriaWeb.carrito')),
            ],
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('fechaCreacion', models.DateField()),
                ('obras', models.ManyToManyField(related_name='galerias', to='AppGaleriaWeb.obraarte')),
            ],
        ),
        migrations.AddField(
            model_name='carrito',
            name='comprador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carritos', to='AppGaleriaWeb.usuario'),
        ),
        migrations.AddField(
            model_name='carrito',
            name='obras',
            field=models.ManyToManyField(to='AppGaleriaWeb.obraarte'),
        ),
    ]