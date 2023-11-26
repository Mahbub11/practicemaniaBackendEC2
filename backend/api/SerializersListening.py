from rest_framework import serializers,fields
from . models import Listening
import logging


class SerializersListening(serializers.ModelSerializer):
    # qas= serializers.SerializerMethodField()
 


    class Meta:
        model = Listening
        fields = (
            'id',
            'title',
            'level',
            'total_tested',
            'type',
            'time',
            'inner_type',
             'qa',
             'created_at',
           
        )
        extra_kwargs = {
            'qa': {'required': True},
            'time': {'required': True},
            
        
        }
    # def create(self, validated_data):
           
    #         validated_data['qa'] =  {'q': self.initial_data['qas'],'a':['ansList']}
    #         instance = Vocabulary(**validated_data)
    #         instance.save()
    #         return instance
    
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['qa'] = instance.qa
    #     return representation
    
    # def get_qas(self, object):
    #      return object.inner_type
    

     