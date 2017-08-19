from rest_framework import serializers
from games.models import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'name', 'release_date', 'game_category')

    def is_empty(self, value):
    	#game = Game.objects.get(value=value)
        if (value is None) or (value == ""):
        	raise serializers.ValidationError("Jogos não podem estar vazios!")
        return value

    def is_repeated(self, value):
    	if value in list(map(lambda it: it.name, Game.objects.filter(name=value))):
            raise serializers.ValidationError("Esse jogo ja existe!")



