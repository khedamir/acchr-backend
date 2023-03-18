from django.db import models
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField

from accounts_chamber.enum import FileType, PostCategories, DocumentCategories
from core.models import Image


class Employee(models.Model):
    first_name = models.CharField(max_length=64, verbose_name=_('Имя'))
    second_name = models.CharField(max_length=64, verbose_name=_('Фамилия'))
    third_name = models.CharField(max_length=64, blank=True, null=True, verbose_name=_('Отчество'))
    birth_date = models.DateTimeField(verbose_name=_('Дата рождения'))
    avatar = models.ForeignKey(Image, blank=True, null=True, on_delete=models.PROTECT, verbose_name=_('Фотография'))
    main_position = models.CharField(max_length=250, blank=True, verbose_name=_('Должность'))
    second_position = models.CharField(max_length=250, blank=True, null=True, verbose_name=_('Вторая должность'))
    biography = RichTextField(verbose_name=_('Биография'))
    priority = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=_('Приоритет в отображений'))


    def get_full_name(self):
        return f'{self.second_name} {self.first_name} {self.third_name} '

    def __str__(self):
        return f"{type(self).__name__}: {self.get_full_name()} {self.main_position} {self.priority}"

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'


class File(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name=_('Имя'))
    url = models.FileField(upload_to='files', verbose_name=_('Файл'))
    type = models.PositiveSmallIntegerField(choices=FileType.choices(), verbose_name=_('Тип файла'))

    def __str__(self):
        return f"{type(self).__name__}: {self.name} {self.type}"

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'


class Document(models.Model):
    title = models.CharField(max_length=512, verbose_name=_('Заголовок'))
    file = models.ForeignKey(File, on_delete=models.PROTECT, verbose_name=_('Файл'))
    category = models.PositiveSmallIntegerField(choices=DocumentCategories.choices(), verbose_name=_('Категория'))

    def __str__(self):
        return f"{type(self).__name__}: {self.title} {self.category}"

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


class Posts(models.Model):
    main_image = models.ForeignKey(Image, blank=True, null=True, on_delete=models.PROTECT,
                                   verbose_name=_('Главное изображение'))
    title = models.CharField(max_length=512, verbose_name=_('Заголовок'))
    content = RichTextField(verbose_name=_('Содержимое'))
    category = models.PositiveSmallIntegerField(choices=PostCategories.choices(), verbose_name=_('Категория'))
    public_date = models.DateTimeField(verbose_name=_('Дата публикации'))

    def __str__(self):
        return f"{type(self).__name__}: {self.title} {self.category}"

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class PageHTML(models.Model):
    id = models.CharField(max_length=256, primary_key=True, verbose_name=_('Идентификатор'))
    title = models.CharField(max_length=512, verbose_name=_('Заголовок'))
    content = RichTextField(verbose_name=_('Содержимое'))
    public_date = models.DateTimeField(verbose_name=_('Дата публикации'))
    description = models.CharField(max_length=1024, blank=True, null=True, verbose_name=_('Описание'))

    def __str__(self):
        return f"{type(self).__name__}: {self.title} {self.public_date}"

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

