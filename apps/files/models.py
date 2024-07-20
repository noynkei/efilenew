from django.db import models
from django.contrib.auth.models import User
from apps.categories.models import Category
class File(models.Model):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.SET_NULL, null=True, blank=True)
    document = models.FileField(upload_to='documents/')
    description = models.CharField(max_length=255, blank=True)
    updated_by = models.ForeignKey(User, related_name='files_updated', on_delete=models.SET_NULL, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='files_created', on_delete=models.SET_NULL, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)