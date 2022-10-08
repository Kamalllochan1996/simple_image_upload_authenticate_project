from rest_framework import serializers
from .models import Awsimage
from django.core.files.images import get_image_dimensions

class AwsimageSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Awsimage
    fields = ('title','images')

def clean_picture(self):
  picture = self.cleaned_data.get("images")
  if not picture:
    raise serializers.ValidationError("No Image")
  else:
    w,h = get_image_dimensions(picture)
  if w != 500:
      raise serializers.ValidationError("It's supposed to 500px")
  if h != 500:
      raise serializers.ValidationError("THe image is %i pixel high. It's supposed to be 500px" % h)
      return images