from django.urls import path, re_path
from .views import product_list, product_detail

app_name = 'app_shop'

urlpatterns = [
    path('', view=product_list, name='product_list'),
    path('<slug:category_slug>/', view=product_list,
         name='product_list_by_category'),
    # path('<int:product_id>/', view=product_detail, name='product_detail'),
    # path('<slug:product_slug>/', view=product_detail, name='product_detail'),
    re_path(r'^', view=product_detail, name='product_detail'),
]
