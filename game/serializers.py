from rest_framework import serializers
from .models import Boards

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boards
        fields = (
            'id', 'user_id'
        )

    # def create(self, validated_data):
    #     instance = self.meta.model(**validated_data)
    #     user = validated_data.user.id
    #     return {

    #     }

class getBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boards
        fields = (
            'id', 
            'game_string',
        )



class updateBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boards
        fields = (
            'game_string',
        )


class listSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boards
        fields = (
            'id',
        )