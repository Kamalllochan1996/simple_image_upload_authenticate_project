from django.contrib import admin
from .models import Awsimage

# Register your models here.
@admin.register(Awsimage)
class AwsimageAdmin(admin.ModelAdmin):
  list_display = ['title','images']
