from django.shortcuts import render
from .models import questions
# Create your views here.
def main_view(request):
    qs = questions.objects.all()
    return render(request, 'main.html', {'object_list': qs}) #contacts,cupons,faq,indraw,my_cupons,news,profile,withdraw
def contact_view(request):
    #qs = questions.objects.all()
    return render(request, 'Contacts.html')
def cupons_view(request):
    #qs = questions.objects.all()
    return render(request, 'Cupons.html')
def faq_view(request):
    #qs = questions.objects.all()
    return render(request, 'FAQ.html')
def indraw_view(request):
    #qs = questions.objects.all()
    return render(request, 'Indraw.html')
def my_cupons_view(request):
    #qs = questions.objects.all()
    return render(request, 'My_cupons.html')
def news_view(request):
    #qs = questions.objects.all()
    return render(request, 'News.html')
def profile_view(request):
    #qs = questions.objects.all()
    return render(request, 'Profile.html')
def withdraw_view(request):
    #qs = questions.objects.all()
    return render(request, 'Withdraw.html')