import json

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def draw_bar(request):
    return render(request, 'charts/show_chart.html')


def get_data(request):
    nums = [5, 20, 36, 10, 10, 20]
    categories = ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
    data = {'data': nums, 'category': categories}
    data = json.dumps(data)
    return HttpResponse(data, content_type="application/json")