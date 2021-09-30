from django.contrib import admin
from .models import Cuponi,questions,news,contacts, ticket
# Register your models here.
admin.site.register(Cuponi)
admin.site.register(questions)
admin.site.register(news)
admin.site.register(contacts)
admin.site.register(ticket)
