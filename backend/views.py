from django.shortcuts import reverse
from django.views.generic import TemplateView, ListView, CreateView
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

class ProductsList(ListView):
    template_name = 'shop.html'

    def get_queryset(self):
        return BrandCategories.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProductsList, self).get_context_data(**kwargs)
        # here we can add so many context using that way
        context['brandcategories'] = BrandCategories.objects.all()
        context['products'] = Products.objects.all()
        return context

class OurService(ListView):
    context_object_name = 'members'
    queryset = TeamMembers.objects.all()
    template_name = 'service.html'

class Contact(TemplateView):
    template_name = 'contact-us.html'