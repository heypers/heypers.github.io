
import markdown
from django.db import models
from django.utils.safestring import mark_safe

class Information(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def get_markdown_content(self):
        md = markdown.Markdown(extensions=['extra', 'nl2br'])
        return mark_safe(md.convert(self.content))

class DatabaseEntry(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Character(models.Model):
    name = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    clearance_level = models.CharField(max_length=100, default='N/A')
    bio = models.TextField()

    def get_markdown_bio(self):
        md = markdown.Markdown(extensions=['extra', 'nl2br'])
        return mark_safe(md.convert(self.bio))

class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
