# Generated by Django 5.1 on 2024-08-09 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(max_length=60, verbose_name='Notebook color')),
            ],
        ),
        migrations.CreateModel(
            name='Notebooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Notebook name')),
                ('price', models.PositiveIntegerField(verbose_name='Notebook price')),
                ('cpu', models.CharField(max_length=60, verbose_name='Notebook CPU')),
                ('gpu', models.CharField(max_length=100, verbose_name='Notebook GPU')),
                ('ram', models.PositiveIntegerField(verbose_name='Notebook ram')),
                ('ssd', models.PositiveIntegerField(verbose_name='Notebook ssd')),
                ('display', models.FloatField(verbose_name='Notebook display')),
                ('dpi', models.CharField(max_length=60, verbose_name='Notebook dpi')),
                ('os', models.CharField(choices=[('windows', 'windows'), ('linux', 'linux'), ('mac os', 'mac os'), ('DOS', 'DOS')], max_length=30, verbose_name='Notebook os')),
                ('image1', models.ImageField(upload_to='notebook_images', verbose_name='Notebook image1')),
                ('image2', models.ImageField(blank=True, upload_to='notebook_images', verbose_name='Notebook image2')),
                ('image3', models.ImageField(blank=True, upload_to='notebook_images', verbose_name='Notebook image3')),
                ('color', models.ManyToManyField(to='main.color')),
            ],
        ),
    ]
