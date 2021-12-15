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