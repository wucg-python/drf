from django.shortcuts import render

# Create your views here.
from rest_framework.parsers import JSONParser, FormParser,MultiPartParser
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.views import exception_handler


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
        return Response({
            "status":200,
            "message":"查询成功",
            "result":{
                # 'name':name,
            }
        })

    def post(self,request,*args,**kwargs):
        user = request.data
        print(user)
        print(request.data['name'])
        print(type(user))
        return Response({
            'status':200,
            "message":"成功",
            "result":user,
        })

