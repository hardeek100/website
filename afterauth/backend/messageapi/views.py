from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import serializers, viewsets
from .serializers import MessageSerialzer
from .models import Message
from .permissions import MessagePermission
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.middleware.csrf import get_token

@method_decorator(csrf_exempt, name="dispatch")
class MessageView(viewsets.ModelViewSet):
    serializer_class = MessageSerialzer
    queryset = Message.objects.all()
    permission_classes = [MessagePermission]
    
class Csrf:
    def get_csrf(request):
        return HttpResponse("{0}".format(get_token(request)), content_type="text/plain")


