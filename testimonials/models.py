"""testimonials Models"""

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Testimonial(models.Model):
    """Model for Testimonial"""
    name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="testimonials")
    title = models.CharField(max_length=200, unique=True)    
    body = models.TextField()
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        """ To display the testimonials by created_on in ascending order """
        ordering = ['created_on']

    def get_absolute_url(self):
        """Get url after user adds/edits testimonial"""
        return reverse('testimonials')

    def __str__(self):
        return f"Testimonial: {self} by {self.name}"