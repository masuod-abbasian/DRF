from rest_framework import serializers
from blog.models import Article
from django.contrib.auth import get_user_model

# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields = ['id','username','last_name','first_name']

# class AuthorUsernameField(serializers.RelatedField):
#     def to_representation(self, value):
#         return value.username

class ArticleSerializer(serializers.ModelSerializer):
    def get_author(self, obj):
        return {
            'username':obj.author.username,
            'first_name':obj.author.first_name,
            'last_name':obj.author.last_name,
            'email':obj.author.email,
        }
    # author = AuthorSerializer()
    # author = serializers.HyperlinkedIdentityField(view_name='api:authors_detail')
    # author = AuthorUsernameField(read_only=True)
    # author = serializers.CharField(source="author.username", read_only=True)
    author = serializers.SerializerMethodField("get_author")
    
    class Meta:
        model = Article
        # fields = ('title','slug','author','content','publish','status')
        # exclude = ('created','updated')
        fields = '__all__'

    def validate_title(self, value):
        filter_list = ['javascript', 'laravel', 'PHP']
        for i in filter_list:
            if i in value:
                raise serializers.ValidationError("Don't use bad world! : {}".format(i))
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'