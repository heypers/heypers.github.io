from django import template
from ..model_map import MODEL_MAP

register = template.Library()

@register.inclusion_tag('model_navigation.html')
def model_navigation():
    return {'models': MODEL_MAP}