from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Tag
from django.db.models import Q


def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()

    # Search bar based on name, description, category or tag via values
    search_query = request.GET.get("search", "")
    if search_query:
        try:
            products = products.filter(
                Q(name__icontains=search_query)
                | Q(description__icontains=search_query)
                | Q(categories__name__icontains=search_query)
                | Q(tags__name__icontains=search_query)
            ).distinct()
        except (ValueError, TypeError):
            pass

    # Category filter
    category_slug = request.GET.get("category")
    if category_slug:
        try:
            products = products.filter(categories__slug=category_slug).distinct()
        except (ValueError, TypeError):
            pass

    # Tag filter
    tag_slugs = request.GET.getlist("tags")
    if tag_slugs:
        try:
            products = products.filter(tags__slug__in=tag_slugs).distinct()
        except (ValueError, TypeError):
            pass

    context = {
        "products": products,
        "categories": categories,
        "tags": tags,
        "search_query": search_query,
        "selected_category": category_slug,
        "selected_tags": tag_slugs,
    }

    return render(request, "products/product_list.html", context)


def product_detail(request, slug):
    # Get the product item
    product = get_object_or_404(
        Product.objects.prefetch_related("categories", "tags"), slug=slug
    )

    similar_products = (
        Product.objects.filter(categories__in=product.categories.all())
        .exclude(id=product.id)
        .distinct()[:5]
    )

    context = {
        "product": product,
        "similar_products": similar_products,
    }

    return render(request, "products/product_detail.html", context)
