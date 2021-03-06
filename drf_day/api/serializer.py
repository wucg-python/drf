from django.conf import settings
from rest_framework import serializers

# 定义序列化器类
from api.models import Teacher


class TeacherSerializer(serializers.Serializer):
    name = serializers.CharField()
    # gender = serializers.IntegerField()
    ke = serializers.CharField()
    # pic = serializers.ImageField()

    gender = serializers.SerializerMethodField()

    def get_gender(self,obj):
        return obj.get_gender_display()

    pic = serializers.SerializerMethodField()

    def get_pic(self,obj):
        return "%s%s%s" % ("http://127.0.0.1:8000/", settings.MEDIA_URL, str(obj.pic))


class TeacherDeSerializer(serializers.Serializer):

    # 添加校验的规则
    name = serializers.CharField(max_length=10,min_length=1)
    ke = serializers.CharField()

    # 全局钩子
    def validate(self, attrs):
        print(attrs, 11111)
        if attrs.get('name') == "王超":
            return attrs
        else:
            raise ValueError('用户名不对')

    # 局部钩子
    def validate_name(self,name):
        if name =="王超":
            raise ValueError('又错了')


    def create(self, validated_data):
        return Teacher.objects.create(**validated_data)



