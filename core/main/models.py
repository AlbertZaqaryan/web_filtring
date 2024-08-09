from django.db import models

# Create your models here.

class Color(models.Model):

    color_name = models.CharField('Notebook color', max_length=60)

    def __str__(self):
        return self.color_name
    

class Notebooks(models.Model):

    OS_LIST = (
        ('windows', 'windows'),
        ('linux', 'linux'),
        ('mac os', 'mac os'),
        ('DOS', 'DOS'),
    )

    name = models.CharField('Notebook name', max_length=60)
    price = models.PositiveIntegerField('Notebook price')
    color = models.ManyToManyField(Color, related_name='note_color')
    cpu = models.CharField('Notebook CPU', max_length=60)
    gpu = models.CharField('Notebook GPU',  max_length=100)
    ram = models.PositiveIntegerField('Notebook ram')
    ssd = models.PositiveIntegerField('Notebook ssd')
    display = models.FloatField('Notebook display')
    dpi = models.CharField('Notebook dpi', max_length=60)
    os = models.CharField('Notebook os', choices=OS_LIST, max_length=30)
    image1 = models.ImageField('Notebook image1', upload_to='notebook_images')
    image2 = models.ImageField('Notebook image2', upload_to='notebook_images', blank=True)
    image3 = models.ImageField('Notebook image3', upload_to='notebook_images', blank=True)


    def __str__(self):
        return self.name
