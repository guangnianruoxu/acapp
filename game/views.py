from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align: center">术士之战</h1>'
    line2 = '<img src="https://img0.baidu.com/it/u=672126781,3294203100&fm=253&fmt=auto&app=120&f=JPEG?w=873&h=500">'
    return HttpResponse(line1+line2)

