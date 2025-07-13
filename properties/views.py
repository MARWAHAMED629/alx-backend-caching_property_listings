from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .models import Property
from .utils import get_all_properties

# Create your views here.

@cache_page(60 * 15)
def property_list(request):
    properties = get_all_properties()
    data = {
        'properties': list(properties.values('id', 'title', 'description', 'price', 'location', 'created_at'))
    }
    return JsonResponse(data)
