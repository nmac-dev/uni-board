from django import template

## Filters
register = template.Library()
@register.filter(name='split')
def split(value, arg):

    if value != None:
        value = value.split(arg)
    return value