import random
from django import template
register = template.Library()

@register.filter(name="shuffle")
def shuffle(arg):
    tmp = list(arg)[:]
    random.shuffle(tmp)
    return tmp

register.filter('shuffle', shuffle)
