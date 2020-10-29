from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt


# @csrf_exempt
# def user(request):
#     if request.method == "GET":
#         return HttpResponse('GET 查询')
#     if request.method == "POST":
#         return HttpResponse('POST 添加')
#     if request.method == "DELETE":
#         return HttpResponse('DELETE 删除')
#     if request.method == "PUT":
#         return HttpResponse('PUT 更新')
from rest_framework.response import Response
from app.models import User


@method_decorator(csrf_exempt,name='dispatch')
class UserView(View):

    def get(self,request, *args, **kwargs):

        id = kwargs.get('id')
        print(id)
        user = User.objects.filter(id=id).values("name",'password',"hoddy")
        if user:
            print(user)
            return JsonResponse(
                {
                    "status":200,
                    "message":"查询信息",
                    "result":list(user),
                }
            )
        else:
            user = User.objects.all().values("name",'password',"hoddy")
            return JsonResponse({
                "status":200,
                "message":"查询所有信息",
                "result":list(user)
            })


    def post(self,request,*args, **kwargs):
        name = request.POST.get('name')
        password = request.POST.get('password')
        hoddy = request.POST.get('hoddy')
        try:
            user = User.objects.create(name=name,password=password,hoddy=hoddy)
            return JsonResponse({
                "status":200,
                "message":"添加成功",
                "result":{"name":user.name,"hoddy":user.hoddy}
            })
        except:
            return JsonResponse({
                "status":400,
                "message":"添加失败",
            })


    def delete(self,request,*args, **kwargs):
        id = kwargs.get('id')
        print(id)
        try:
            user = User.objects.get(id=id)
            user.delete()
            return JsonResponse({
                "status":"200",
                "message":"删除成功",
                "result":{"name":user.name,"password":user.password,"hoddy":user.hoddy}
            })
        except:
            return JsonResponse({
                "status":400,
                "message":"删除失败"
            })

from rest_framework.views import APIView

class UserApi(APIView):
    def get(self,request,*args,**kwargs):
        return Response('GET 查询')