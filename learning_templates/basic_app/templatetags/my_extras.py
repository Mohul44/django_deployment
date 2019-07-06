from django import template

register=template.Library()

def cut(value,arg):
    """
    doc docc
    """
    return value.replace(arg,"")

register.filter('cut',cut)
# from django import template
# register = template.Library()
#
# @register.filter
# def cutout(value, arg):
#     return value.replace(arg, '')
