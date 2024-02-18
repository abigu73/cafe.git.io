from django.urls import path
from shop.views.indexview import IndexView
from shop.views.productdetailsview import ProductDetailsView
from shop.views.aboutview import AboutView
from shop.models import Product
from shop.views.productview import ProductView
from django.conf import settings
from django.conf.urls.static import static
from shop.views.contactview import ContactView

urlpatterns = [
    path("products/<int:id>", ProductDetailsView.as_view(), name="products"),
    path("",IndexView.as_view(), name="index"),
    path("products/",ProductView.as_view(), name="products"),
    path("about/",AboutView.as_view(), name="about"),
    path("contact/",ContactView.as_view(), name="contact"),
]