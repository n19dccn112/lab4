from django.shortcuts import render
from myapp.models import *

def home(request):
    if len(Question.objects.order_by('-id')) > 0 :
        questiondata = Question.objects.order_by('-id')[0]
        question_text = questiondata.question_text
        pub_date = questiondata.pub_date
        return render(request, 'index.html', {'question_text':question_text,'pub_date':pub_date})
    else:
        return render(request, 'index.html', {'question_text':'','pub_date':''})



