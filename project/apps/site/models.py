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

    def get_markdown_content(self):
        md = markdown.Markdown(extensions=['extra', 'nl2br'])
        return mark_safe(md.convert(self.content))


class Character(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        verbose_name = "Персонаж"
        verbose_name_plural = "Персонажи"

    def get_markdown_content(self):
        md = markdown.Markdown(extensions=['extra', 'nl2br'])
        return mark_safe(md.convert(self.content))


class Object(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        verbose_name = "Объект"
        verbose_name_plural = "Объекты"

    def get_markdown_content(self):
        md = markdown.Markdown(extensions=['extra', 'nl2br'])
        return mark_safe(md.convert(self.content))


class Protocol(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        verbose_name = "Протокол"
        verbose_name_plural = "Протоколы"

    def get_markdown_content(self):
        md = markdown.Markdown(extensions=['extra', 'nl2br'])
        return mark_safe(md.convert(self.content))