from rest_framework import serializers
from news.models import News, Author

from datetime import datetime
from datetime import date
from django.utils.timesince import timesince


# ModelSerializer
class NewsSerializer(serializers.ModelSerializer):
    time_since_pub = serializers.SerializerMethodField()
    # author = serializers.StringRelatedField()
    # author = AuthorSerializer()

    class Meta:
        model = News
        fields = '__all__'
        # fields = ['author', 'title', 'text']
        # exclude = ['id', 'date']
        read_only_fields = ['id', 'update_date']

    def get_time_since_pub(self, object):
        now = datetime.now()
        pub_date = object.date
        if object.is_active:
            time_delta = timesince(pub_date, now)
            return time_delta
        else:
            return 'Not active!'

    def validate_date(self, datevalue):
        today = date.today()
        if datevalue > today:
            raise serializers.ValidationError('Publish date cannot be in future!')
        return datevalue


class AuthorSerializer(serializers.ModelSerializer):
    # news = NewsSerializer(many=True, read_only=True)
    news = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='news_actions',
    )

    class Meta:
        model = Author
        fields = '__all__'



# class NewsSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField()
#     title = serializers.CharField()
#     subtitle = serializers.CharField()
#     text = serializers.CharField()
#     city = serializers.CharField()
#     date = serializers.DateField()
#     is_active = serializers.BooleanField()
#     update_date = serializers.DateField(read_only=True)
#
#     def create(self, validated_data):
#         print(validated_data)
#         return News.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.author = validated_data.get('author', instance.author)
#         instance.title = validated_data.get('title', instance.title)
#         instance.subtitle = validated_data.get('subtitle', instance.subtitle)
#         instance.text = validated_data.get('text', instance.text)
#         instance.city = validated_data.get('city', instance.city)
#         instance.date = validated_data.get('date', instance.date)
#         instance.is_active = validated_data.get('is_active', instance.is_active)
#         instance.save()
#         return instance
#
#     def validate(self, data):  # object level
#         if data['title'] == data['subtitle']:
#             raise serializers.ValidationError(
#                 "Title and subtitle can't be the same.")
#         return data
#
#     def validate_title(self, value):
#         if len(value) < 10:
#             raise serializers.ValidationError(
#                 f'Title must be minimum 10 characters. You entered {len(value)} character.')
#         return value


