from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Book
from api.serializers import BookModelSerializer


class BookAPIView(APIView):

    def get(self,request,*args,**kwargs):
        book_id = kwargs.get('id')
        if book_id:
            book = Book.objects.filter(id=book_id,is_delete=False)[0]
            serialize = BookModelSerializer(book).data
            # print(serialize)
            return Response({
                'status':200,
                "message":"查询一个书籍",
                "result":serialize,
            })
        else:
            books = Book.objects.filter(is_delete=False)
            serialize = BookModelSerializer(books,many=True).data
            return Response({
                'status': 200,
                "message": "查询所有书籍",
                "result": serialize,
            })

    def post(self,request,*args,**kwargs):
        request_data = request.data
        print(request_data)
        if isinstance(request_data,dict):
            many = False
        elif isinstance(request_data,list):
            many = True
        else:
            return Response({
                "status":400,
                "message":"添加失败"
            })
        serialize = BookModelSerializer(data=request_data,many=many)
        serialize.is_valid(raise_exception=True)
        book = serialize.save()
        return Response({
            'status': 200,
            "message": "添加书籍",
            "result": BookModelSerializer(book,many=many).data,
        })


    def delete(self,request,*args,**kwargs):
        id = kwargs.get('id')
        if id:
            # 删除单个
            ids = [id]
        else:
            ids = request.data
        response = Book.objects.filter(id__in=ids,is_delete=False).update(is_delete=True)
        if response:
            return Response({
                "status":200,
                "message":"删除成功",
            })
        else:
            return Response({
                "status": 400,
                "message": "删除失败或已被删除",
            })

    # 更新单个整体
    def put(self,request,*args,**kwargs):
        # 获取到修改的值
        request_data = request.data
        # 获取到被修改的对象
        book_id = kwargs.get('id')
        try:
            book_obj = Book.objects.get(id=book_id)
        except:
            return Response({
                "status":400,
                "message":"对象不存在"
            })
        serializer = BookModelSerializer(data=request_data,instance=book_obj)
        serializer.is_valid(raise_exception=True)
        book = serializer.save()
        return Response({
            "status":200,
            "message":"修改成功",
            "result":BookModelSerializer(book).data
        })

    def patch(self,request,*args,**kwargs):
        # 获取到修改的值
        request_data = request.data
        # 获取到被修改的对象
        book_id = kwargs.get('id')
        try:
            book_obj = Book.objects.get(id=book_id)
        except:
            return Response({
                "status": 400,
                "message": "对象不存在"
            })
        serializer = BookModelSerializer(data=request_data, instance=book_obj,partial=True)
        serializer.is_valid(raise_exception=True)
        book = serializer.save()
        return Response({
            "status": 200,
            "message": "修改成功",
            "result": BookModelSerializer(book).data
        })