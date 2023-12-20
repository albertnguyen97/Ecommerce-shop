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
from cart.forms import CartAddProductForm
import redis
from django.conf import settings

r = redis.Redis(host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_DB)


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


@login_required
def product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Check if the current user is the owner of the product
    if request.user != product.user:
        messages.error(request, "You don't have permission to delete this product.")
        return redirect('some_redirect_url')  # Specify the appropriate URL to redirect if permission is denied

    if request.method == "POST":
        form = ProductDeleteForm(request.POST)
        if form.is_valid():
            # Assuming your ProductDeleteForm has some validation logic, perform validation here

            # Delete the product
            product.delete()
            messages.success(request, 'Product deleted successfully')
            return redirect('some_redirect_url')  # Specify the appropriate URL to redirect after deletion
    else:
        form = ProductDeleteForm()

    return render(request, 'shop/product/delete.html',
                  {'section': 'product',
                   'product': product,
                   'form': form})


@login_required
def product_detail_shop(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug)
    cart_product_form = CartAddProductForm()
    total_views = r.incr(f'product:{product.id}:views')
    r.zincrby('product_ranking', 1, product.id)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'total_views': total_views})


@login_required
def product_list_shop(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    user = request.user  # Get the currently logged-in user
    products = Product.objects.filter(user=user)
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


@login_required
def product_list_market(request, category_slug=None):
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
                  'shop/product/list_product.html',
                  {'category': category,
                   'categories': categories,
                   'products_market': products})


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


@login_required
def product_ranking(request):
    product_ranking = r.zrange('product_ranking', 0, -1,
                               desc=True)[:10]
    product_ranking_ids = [int(id) for id in product_ranking]
    most_viewed = list(Product.objects.filter(
        id__in=product_ranking_ids))
    most_viewed.sort(key=lambda x: product_ranking_ids.index(x.id))
    return render(request,
                  'shop/product/ranking_views.html',
                  {'section': 'products',
                   'most_viewed': most_viewed})
