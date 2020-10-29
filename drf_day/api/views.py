from django.shortcuts import render

# Create your views here.
from rest_framework.parsers import JSONParser, FormParser,MultiPartParser
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.views import exception_handler

from api.models import Teacher
from api.serializer import TeacherSerializer,TeacherDeSerializer


class UserAPIView(APIView):
    # 为某个视图配置局部渲染器
    # 局部配置优先级高于全局配置
    # renderer_classes = (BrowsableAPIRenderer,)
    parser_classes = (JSONParser,FormParser,MultiPartParser)
    def get(self,request,*args,**kwargs):
        # print(request)
        # name = request.GET.get('name')
        # print(name)
        # name1 = request._request.GET.get('name')
        # print(request._request)
        # print(name1)
        # name = request.query_params.get('name')

        id = kwargs.get('id')
        if id:
            obj = Teacher.objects.get(id=id)
            teacher_serializer = TeacherSerializer(obj).data
            print(teacher_serializer)
            return Response({
            "status":200,
            "message":"查询成功",
            "result":teacher_serializer,

        })
        else:
            obj = Teacher.objects.all()
            teachers_serializer = TeacherSerializer(obj,many=True).data
            print(teachers_serializer)
            return Response({
                "status": 200,
                "message": "查询成功",
                "result": teachers_serializer,

            })


    def post(self,request,*args,**kwargs):
        # user = request.data
        # print(user)
        # print(request.data['name'])
        # print(type(user))
        teacher = request.data
        if not isinstance(teacher,dict) or teacher =={}:
            return Response({
                'status': 200,
                "message": "参数不对",

            })
        serializer = TeacherDeSerializer(data=teacher)
        if serializer.is_valid():
            tea = serializer.save()
            return Response({
                'status':200,
                "message":"成功",
                "result":TeacherDeSerializer(tea).data,
            })
        else:
            return Response({
                "status":400,
                "message":"添加失败",
                "result":serializer.errors
            })
