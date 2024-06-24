from django.contrib import admin
from .models import Reviews


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    """
    Displays the Reviews in the admin panel
    """
    list_display = (
        "name",
        "review_title",
        "timestamp",
        "product_review",
        "product_rating",
        "approved",
        "carousel_review",
    )