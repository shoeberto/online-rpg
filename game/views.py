from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from game.models import Game
from game.serializers import GameSerializer


def game_list(request):
    """
    List all games.
    """
    if request.method == 'GET':
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return JsonResponse(serializer.data, safe=False)