from django.db import models
from django.urls import reverse
from products.models import Product


class Reviews(models.Model):
    """
    Model for Reviews
    """

    class Meta:
        verbose_name_plural = "Reviews"

    name = models.CharField(max_length=20)
    image = models.ImageField(
                              upload_to="reviews_images/",
                              null=True,
                              blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    product_review = models.TextField(null=True, max_length=400)
    product_rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    featured_image_url = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name="products_image_url", null=True)
    product_name = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name="product_name", null=True,
        limit_choices_to={'orderlineitem__isnull': False})
    approved = models.BooleanField(default=True)
    carousel_review = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Sets absolute URL"""
        return reverse("reviews")
