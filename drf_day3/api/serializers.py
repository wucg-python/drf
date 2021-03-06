from rest_framework.serializers import ModelSerializer

from api.models import Book, Publisher


class PublisherModelSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = ("pub_name",'pic',"address")


class BookModelSerializer(ModelSerializer):
    # publish = PublisherModelSerializer()
    class Meta:
        model = Book  # 指定当前序列化的模型

        # 指定要序列化的字段
        # 序列化所有字段
        # fields = "__all__"

        # fields = ("book_name","price","pic")
        # fields = ("book_name","price","pic","publish")

        # 指定不展示的字段
        # exclude = ("is_delete","create_time")

        # 查询深度
        # depth = 1
        # fields = ("book_name","price","pic","pub_name","authors")


        # 序列化与反序列化的整合
        fields = ("book_name", "price", "pic", "pub_name", "authors",'author','publish')

        extra_kwargs = {
            "book_name":{
                "min_length":2,  #最小长度
                "error_messages":{
                    "min_length":"书籍名称不能小于两个子"
                }
            },
            # 只用于序列化
            "pic":{
                "read_only":True
            },
            "pub_name":{
                "read_only": True
            },
            "authors":{
                "read_only": True
            },
            # 只用于反序列化
            "author":{
                "write_only":True
            },
            "publish": {
                "write_only": True
            }
        }

    # 全局钩子函数
    def validate(self, attrs):
        return attrs

    def validate_price(self,price):
        if price <= 10:
            raise ValueError('价格太低')
        return price
