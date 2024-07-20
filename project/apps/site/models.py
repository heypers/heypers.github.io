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


class Information(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    class Meta:
        app_label = 'site'

    def get_markdown_content(self):
        md = markdown.Markdown(extensions=['extra', 'nl2br'])
        return mark_safe(md.convert(self.content))


class DatabaseEntry(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        app_label = 'site'

    def __str__(self):
        return self.title


class Character(models.Model):
    name = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    clearance_level = models.CharField(max_length=100, default='N/A')
    bio = models.TextField()

    class Meta:
        app_label = 'site'

    def get_markdown_bio(self):
        md = markdown.Markdown(extensions=['extra', 'nl2br'])
        return mark_safe(md.convert(self.bio))


class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        app_label = 'site'

    def __str__(self):
        return self.name
