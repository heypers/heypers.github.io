"""
Copyright 2023 mr_fortuna

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import markdown
from django.db import models
from django.utils.safestring import mark_safe


class BaseModel(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        abstract = True
        app_label = 'site'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_markdown_content(self):
        md = markdown.Markdown(extensions=['extra', 'nl2br'])
        return mark_safe(md.convert(self.content))


class Information(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        verbose_name = "Информация"
        verbose_name_plural = "Информация"
        app_label = 'site'


class Character(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        verbose_name = "Персонаж"
        verbose_name_plural = "Персонажи"
        app_label = 'site'


class Object(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        verbose_name = "Объект"
        verbose_name_plural = "Объекты"
        app_label = 'site'


class Protocol(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        verbose_name = "Протокол"
        verbose_name_plural = "Протоколы"
        app_label = 'site'


class Lore(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        verbose_name = "Лор"
        verbose_name_plural = "Лор"
        app_label = 'site'


class Plot(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        verbose_name = "Сюжет"
        verbose_name_plural = "Сюжеты"
        app_label = 'site'


class Location(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"
        app_label = 'site'


class Department(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделения"
        app_label = 'site'


class Organization(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Огранизации"
        app_label = 'site'


class Group(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
        app_label = 'site'


class Technology(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        verbose_name = "Технология"
        verbose_name_plural = "Технологии"
        app_label = 'site'


class Document(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"
        app_label = 'site'
