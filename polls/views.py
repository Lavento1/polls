from django.http import HttpResponse
from django.shortcuts import render
from polls.models import Question

# Create your views here.


def index(request):
    # db에 있는 모든 데이터 조회하기(select)
    question_list = Question.objects.all()
    return render(request, 'polls/index.html', {'question_list': question_list})
    # return HttpResponse("Welcome~ 환영합니다!!")


def detail(request, question_id):
    # 해당 id(순번)로 자료를 조회
    question = Question.objects.get(id=question_id)
    return render(request, 'polls/detail.html', {'question': question})
