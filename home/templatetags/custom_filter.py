from django import template
from home.models import *

register = template.Library()

@register.filter
def getChilds(parentId):
    return Category.objects.filter(cate_parent_id=parentId)

