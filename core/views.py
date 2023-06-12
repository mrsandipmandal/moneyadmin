from django.shortcuts import render
from django.views import View
from .models import *

class Index(View):
    template = 'adminlte/index.html'
    
    def get(self, request):
        income = Total.Sum_Total
        return render(request, self.template, {'income': income})