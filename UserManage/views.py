from django.http import HttpResponse
from django.shortcuts import render
# from UserManage.models import service_account

# def hello(request):
#     return HttpResponse('home page!')


# def helloworld(request):
    # context = {}
    # test = service_account.objects.get(id=1)
    # value = test.account
    # context['value'] = value
    # return render(request, 'hellowld.html', context)

# def addExam(request):
#     exam = service_account()
#     exam.ID = '100001'
#     exam.SceneID = '1001',
#     exam.ExamName = '期末考试'
#     exam.save()
#     context = {}
#     context['value'] = exam.ExamName + '数据添加成功！'
#     return render(request,'helloworld.html',context)