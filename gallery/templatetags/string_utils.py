from django import template
from string import digits


register = template.Library()


@register.filter
def strip_digits(string):
    if string.isdigit():
        return string
    else:
        return string.lstrip(digits + ' ')
