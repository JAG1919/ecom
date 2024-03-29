from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^book/(\d+)', views.book_details, name='book_details'),
    url(r'^add/(\d+)', views.add_to_cart, name='add_to_cart'),
    url(r'^remove/(\d+)', views.remove_from_cart, name='remove_from_cart'),
    url(r'^cart/', views.cart, name='cart'),
    url(r'^products/', views.store, name='products'),
    url(r'^genre/', views.genre, name='genre'),
    url(r'^genreresults/(\w+)', views.genreresults, name='genreresults'),
    url(r'^checkout/(\w+)', views.checkout, name='checkout'),
    url(r'^process/(\w+)', views.process_order, name='process_order'),
    url(r'^order_error/', views.order_error, name='order_error'),
    url(r'^complete_order/(\w+)', views.complete_order, name='complete_order'),
]
