from rest_framework.generics import CreateAPIView
from .serializers import *

#  Models
from .models import *




class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer

