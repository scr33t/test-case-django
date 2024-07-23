from django.db import models


class ItemImage(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.caption

    class Meta:
        ordering = ['order']
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


class ItemDetail(models.Model):
    title = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
        verbose_name = "Параметры товара"


class Item(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField()
    order = models.PositiveIntegerField(default=0)
    image = models.ForeignKey(ItemImage, on_delete=models.CASCADE)
    details = models.ForeignKey(ItemDetail, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
