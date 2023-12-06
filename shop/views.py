from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .forms import ProductCreateForm
from .models import Product
from .models import Category, Product
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required
def product_create(request):
    if request.method == "POST":
        product_form = ProductCreateForm(request.POST, request.FILES)
        if product_form.is_valid():
            new_product = product_form.save(commit=False)
            new_product.user = request.user
            new_product.save()
            messages.success(request, 'Product added successfully')
            return redirect(new_product.get_absolute_url())
    else:
        product_form = ProductCreateForm()

    return render(request, 'shop/product/create.html',
                  {'section': 'product',
                   'product_form': product_form})


@login_required()
def product_detail_shop(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product})


@login_required()
def product_list_shop(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category,
                                     slug=category_slug)
        products = products.filter(category=category)
    paginator = Paginator(products, 20)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If the page parameter is not an integer, deliver the first page.
        products = paginator.page(1)
    except EmptyPage:
        # If the page is out of range (e.g., 9999), deliver the last page.
        products = paginator.page(paginator.num_pages)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_list_market(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category,
                                     slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'market/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


@login_required()
def product_detail_market(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'market/product/detail.html',
                  {'product': product})


@login_required
@require_POST
def product_like(request):
    product_id = request.POST.get('id')
    action = request.POST.get('action')
    if product_id and action:
        try:
            product = Product.objects.get(id=product_id)
            if action == 'like':
                product.users_like.add(request.user)
            else:
                product.users_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except Product.DoesNotExist:
            pass
    return JsonResponse({'status': 'error'})