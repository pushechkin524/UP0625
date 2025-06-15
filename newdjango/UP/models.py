from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название категории')
    description = models.TextField(max_length=1024, null=True, blank=True, 
                                 default='Нет описания', verbose_name='Описание категории')
    
    def str(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Collection(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название коллекции')
    description = models.TextField(max_length=1024, null=True, blank=True, 
                                 default='Нет описания', verbose_name='Описание коллекции')
    
    def str(self):
        return self.name

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'

class Clothes(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название одежды')
    description = models.TextField(max_length=1024, null=True, blank=True, 
                                 default='Нет описания', verbose_name='Описание одежды')
    price = models.FloatField(verbose_name='Цена')
    size = models.PositiveBigIntegerField(default=32, verbose_name='Размер')
    color = models.CharField(max_length=50, verbose_name='Цвет')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, 
                            verbose_name='Изображение')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    is_exists = models.BooleanField(default=True, verbose_name='Доступность к покупке')

    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    collection = models.ManyToManyField(Collection, verbose_name='Коллекция')

    def str(self):
        return self.name

    class Meta:
        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежда'