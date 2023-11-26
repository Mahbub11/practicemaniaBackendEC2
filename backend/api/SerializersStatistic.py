from rest_framework import serializers,fields
from . models import StatisticDUOLINGO


class SerializersStatistic(serializers.ModelSerializer):
    


    class Meta:
        model = StatisticDUOLINGO
        fields = (
            'id',
            'user',
            'qn',
            'level',
            'type',
            'time',
            'inner_type',
             'result',
             'created_at',
           
        )
   

     