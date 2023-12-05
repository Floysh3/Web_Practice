from django.db.models import Count
from django.contrib.contenttypes.models import ContentType
from .models import *

menu = [{'title': 'Опубликовать фотографию', 'url_name': 'pub_photo'},]

class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        user_menu = menu.copy()
        context['menu'] = user_menu
        return context
