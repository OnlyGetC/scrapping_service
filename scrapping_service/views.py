from django.shortcuts import render
import datetime
def main(request):
    date = datetime.datetime.now().date()
    name = "dave"
    _context = {'date': date, 'name': name}
    return render(request,'main.html', _context)
##def contacts(request):
    ##return render(request,'Contacts.html')
##def cupon(request):
 ##   return render(request,'Cupons.html')
##def faq(request):
   ## return render(request,'FAQ.html')
##def indraw(request):
  ##  return render(request,'Indraw.html')
##def my_cupons(request):
   ## return render(request,'My_cupons.html')
##def News(request):
  ##  return render(request,'News.html')
##def profile(request):
  ##  return render(request,'Profile.html')
##def withdraw(request):
   ## return render(request,'Withdraw.html')