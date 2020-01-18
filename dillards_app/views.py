from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.contrib import messages
from django.urls import reverse
from .redis_connect import redis_inst
from .models import ParsedProduct


class ParseProductsView(View):
    def get(self, request):
        return render(request, 'dillards_app/parse_products.html')

    def post(self, request):
        redis_inst.lpush('dillards:start_urls', 'https://www.dillards.com/c/men')
        messages.info(request,
                      'Parsing has started. Soon the data will be parsed. '
                      'You can see the product data on this %(page)s' %
                      {'page': f'<a href="{reverse("dillards:products_list")}">page</a>'},
                      extra_tags='safe')
        return render(request, 'dillards_app/parse_products.html')


class ProductsListView(ListView):
    model = ParsedProduct
    template_name = 'dillards_app/products_list.html'
    context_object_name = 'products'
    paginate_by = 15
