from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import Product

def submit_contact_form(request):
    return render(request, 'contact.html')


class submit_contact_form(TemplateView):
    template_name = "shop/contact.html"
    
    def get(self, request, id):
        product = Product.objects.get(id=id)
        context = {
            "title": product.name,
            "description": product.description,
            "price": product.price,
        }
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))
