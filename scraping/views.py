from django.shortcuts import render
from .models import questions
# Create your views here.
def main_view(request):
    qs = questions.objects.all()
    return render(request, 'main.html', {'object_list': qs})