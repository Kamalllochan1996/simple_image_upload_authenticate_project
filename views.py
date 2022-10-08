from .models import Awsimage
from .serializers import AwsimageSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class AwsimageModelView(viewsets.ModelViewSet):
  queryset = Awsimage.objects.all()
  serializer_class = AwsimageSerializer
  authentication_classes=[TokenAuthentication]
  permission_classes=[IsAuthenticated]
  