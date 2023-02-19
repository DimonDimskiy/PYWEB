

from django.shortcuts import render
from datetime import datetime
import random

from django.views import View
from django.http import HttpResponse

class CurrentDateView(View):
    def get(self, request):
        html = f'{datetime.now()}'
        return HttpResponse(html)

class RandomNumber(View):
    def get(self, request):
        return HttpResponse(random.random())

class IndexView(View):
    def get(self, request):
        return render(request, 'common/index.html')