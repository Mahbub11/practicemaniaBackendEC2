from rest_framework import serializers,fields
from . models import Vocabulary
import logging


class SerializersVOC(serializers.ModelSerializer):
    # qas= serializers.SerializerMethodField()
 


    class Meta:
        model = Vocabulary
        fields = (
            'id',
            'level',
            'total_tested',
            'type',
            'time',
            'inner_type',
             'qa'
           
        )
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
    

     