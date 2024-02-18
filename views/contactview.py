from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import Product
from django.shortcuts import render, redirect
from shop.forms import ProductForm
from django.shortcuts import render





def contactview(request):
  
    return render(request, 'contact.html')


class ContactView(TemplateView):
    template_name = "shop/contact.html"

    
    def get(self, request):
        products = Product.objects.order_by("name")
        context = {"products": [{ "id": p.id, "name": p.name, "price": p.price} for p in products]}
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))
    
  
def get(self, request, id):
        Contact = Contact.objects.get(id=id)
        context = {
            "user": user.name,
            "password": user.password,
        
        }
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))
    # views.py
from django.shortcuts import render
from shop.forms import ContactForm

def contact_view(request):
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})
