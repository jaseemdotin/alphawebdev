import django_filters
from .models import *
class filters(django_filters.FilterSet):
    prize=django_filters.RangeFilter()
    class Meta:
        model=alphaproducts1
        fields=['productname', 'catname', 'prize', 'sell','brand']