from django.conf.urls import url
from django.contrib import admin

from charts import views


urlpatterns = [
    url(r'bar/', views.draw_bar, name='bar'),
    url(r'getdata/', views.get_data, name='get_data'),
]
