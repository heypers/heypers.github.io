from django import template
from ..model_map import MODEL_MAP

register = template.Library()

@register.inclusion_tag('model_navigation.html')
def model_navigation():
    models_with_names = {
        model_name: {
            'verbose_name_plural': model._meta.verbose_name_plural,
            'model_name': model_name
        }
        for model_name, model in MODEL_MAP.items()
    }
    return {'models': models_with_names}
