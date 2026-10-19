from django.urls import path
from product.views import ProductList


urlpatterns = [
    path('products/', ProductList.as_view()),
]
