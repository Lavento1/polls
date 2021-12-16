from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'control/index.html')


def register(request):
    if request.method == "POST":
        userid = request.POST['userid']
        # html로 렌더링할때 딕셔너리 구조로 자료를 보냄
        return render(request, 'control/reg_result.html', {'userid': userid})
    else:
        return render(request, 'control/register.html')


# 반복문 forloop.counter
def counter(request):
    items = ['a', 'b', 'c', 'd']
    return render(request, 'control/counter.html', {'items': items})


# 짝수/홀수 판별 calc_even_odd
def calc_even_odd(request):
    if request.method == 'POST':
        try:
            num = int(request.POST['num'])
        except:
            return render(request, 'control/calc_even_odd.html',
                          {'error':'정수만 입력 가능합니다.'})
        else:
            if num % 2 == 0:
                result = "짝수입니다."
            else:
                result = "홀수입니다."
            return render(request, 'control/calc_result.html',
                          {'num': num, 'result': result})
    else:
        return render(request, 'control/calc_even_odd.html')

