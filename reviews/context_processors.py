from .models import *


def product_reviews(request):
    """
    A view to show customers reviews
    """
    product_reviews = Reviews.objects.filter(
        approved=True, carousel_review=True
    ).order_by("-timestamp")

    context = {
        "service_reviews": product_reviews,
    }

    return context
