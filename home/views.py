from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


class Home(APIView):
	def get(self, request, format=None):
		context = {
			'test': "value"
		}
		return render(request, 'base.html', context)