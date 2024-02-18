from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import Product
from django.shortcuts import render, redirect
from shop.forms import ProductForm
from django.shortcuts import render

def productview(request):
  
    return render(request, 'products.html')



class ProductView(TemplateView):
    template_name = "shop/products.html"
    
    def get(self, request):
        products = Product.objects.order_by("name")
        context = {"products": [{ "id": p.id, "name": p.name, "price": p.price} for p in products]}
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))
    
    def upload_product(request):
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success URL
        else:
            form = ProductForm()
            return render(request, 'upload_product.html', {'form': form})
