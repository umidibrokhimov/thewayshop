from itertools import product
from django.shortcuts import reverse, render
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from .forms import *
from .models import *

class RegistrationView(CreateView):
    form_class = CreationForm
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse('login')

class Home(ListView):
    context_object_name = 'categories'
    queryset = Categories.objects.all()
    template_name = 'index.html'

    def get_queryset(self):
        return HomeSlides.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        # here we can add so many context using that way
        context['slides'] = HomeSlides.objects.all()
        context['products'] = Products.objects.filter(is_top=True)
        context['blogs'] = Blog.objects.all()
        context['product_categories'] = Categories.objects.all()
        return context


class About(ListView):
    context_object_name = 'teammembers'
    queryset = TeamMembers.objects.all()
    template_name = 'about.html'

def ProductsList(request):
    brandcategories = BrandCategories.objects.all()
    category = request.GET.get('brand')
    if category == None:
        products = Products.objects.all()
    else:
        products = Products.objects.filter(brand_clothe__name=category)

    context = {
        "brandcategories": brandcategories,
        "products": products,
    }
    return render(request, 'shop.html', context)

class OurService(ListView):
    context_object_name = 'members'
    queryset = TeamMembers.objects.all()
    template_name = 'service.html'

class Contact(TemplateView):
    template_name = 'contact-us.html'

class UserAccount(DetailView):
    queryset = User.objects.all()
    context_object_name = 'user'
    template_name = 'my-account.html'

class ProductCart(TemplateView):
    template_name = 'cart.html'

class ProductDetail(DetailView):
    context_object_name = 'product'
    queryset = Products.objects.all()
    template_name = 'shop-detail.html'

    def get_queryset(self):
        return Products.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        # here we can add so many context using that way
        context['products'] = Products.objects.all()
        return context

class ProductCheckout(TemplateView):
    context_object_name = 'product'
    queryset = Products.objects.all()
    template_name = 'checkout.html'

class Wishlist(TemplateView):
    # context_object_name = 'product'
    # queryset = Products.objects.all()
    template_name = 'wishlist.html'