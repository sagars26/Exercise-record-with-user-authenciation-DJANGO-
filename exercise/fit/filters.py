import django_filters
from .models import *

class exerciseFilter(django_filters.FilterSet):
    class Meta:
        model = Exerc
        fields = ['name']