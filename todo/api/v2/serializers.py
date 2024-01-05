from rest_framework import serializers
from django.contrib.auth.models import User

from todo.models import Task

class TaskSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'absolute_url', 'created_date', 'updated_date']
        read_only_fields = ['user']

    def get_absolute_url(self,obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)
    
    def to_representation(self,instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)

        if request.parser_context.get('kwargs').get('pk') :
            rep.pop('absolute_url', None)
        return rep
    
    def create(self,validated_data):
        validated_data['user'] = User.objects.get(id=self.context.get('request').user.id)
        return super().create(validated_data)