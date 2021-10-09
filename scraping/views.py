from django.shortcuts import render
from .models import questions, news, contacts
# Create your views here.
def main_view(request):
    qs = questions.objects.all()
    return render(request, 'main.html', {'object_list': qs}) #contacts,cupons,faq,indraw,my_cupons,news,profile,withdraw
def contact_view(request):
    qs2 = contacts.objects.all()
    return render(request, 'Contacts.html', {'contact_list': qs2})
def cupons_view(request):
    #qs = questions.objects.all()
    return render(request, 'Cupons.html')

def faq_view(request):
    qs = questions.objects.all()
    #title = questions.question_title()
   # descr = questions.description()
    #answ = questions.answer()
   # context = {
        #'object_list': qs,
       # 'title': qt,
      #  'descr': ds,
       # 'answ': aw,
   # }           http://surl.li/aijxs - смотреть здесь как исправить ошибку
    return render(request, 'FAQ.html',{'object_list': qs})

def indraw_view(request):
    #qs = questions.objects.all()
    return render(request, 'Indraw.html')
def my_cupons_view(request):
    #qs = questions.objects.all()
    return render(request, 'My_cupons.html')

def news_view(request):
    qs1 = news.objects.all()
    return render(request, 'News.html', {'news_list': qs1})

def profile_view(request):
    #qs = questions.objects.all()
    return render(request, 'Profile.html')
def withdraw_view(request):
    #qs = questions.objects.all()
    return render(request, 'Withdraw.html')