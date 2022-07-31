from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Contact
from .serializers import ContactSerializer
from .models import Contact
from .serializers import ContactSerializer
from rest_framework import generics


class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    #def list(self, request, *args, **kwargs):
        #queryset = Contact.objects.all()

        # response.Response({"results": self.get_serializer(queryset, many=True).data}, status=200)

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer



# Create your views here.

# Create your views here.
