
from django.db import models


class AnonymousPost(models.Model):

    CATEGORY_CHOICES = [
        ('CONFESSION', 'Confession'),
        ('APPRECIATION', 'Appreciation'),
        ('QUESTION', 'Question'),
    ]

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='CONFESSION'
    )

    message = models.TextField(max_length=1000)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} - {self.status}"
    
class PostReport(models.Model):
    post = models.ForeignKey(
        AnonymousPost,
        on_delete=models.CASCADE,
        related_name='reports'
    )
    reason = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report for Post #{self.post.id}"

