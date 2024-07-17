import re
from django import template

register = template.Library()

@register.filter
def format_number(value):
    return re.sub(r'\B(?=(\d{3})+(?!\d))', '.', str(value))