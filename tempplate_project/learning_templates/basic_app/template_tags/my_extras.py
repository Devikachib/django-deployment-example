from django import learning_templates

register = template.Library()

def cut(value,arg):
    return value.replace(arg,'')

register.filter('cut', cut)
