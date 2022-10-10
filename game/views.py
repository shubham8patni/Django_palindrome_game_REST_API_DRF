from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import BoardSerializer, getBoardSerializer, updateBoardSerializer,listSerializer
from .models import Boards
import random
import string

# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def create(request):
    if request.method == 'POST':
        print(request.user.id)
        request.data['user_id'] = request.user.id
        serializer = BoardSerializer(data = request.data)
        # print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data
            )
        else:
            return Response({
                'id' : ""
            })
            
    if request.method == 'GET':
        return Response({
            'message' : 'hello world'
        })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def getBoard(request, id):
    if request.method == 'GET':
        try:
            board_id = Boards.objects.get(id = id, user_id = request.user.id)
            serializer = getBoardSerializer(board_id) 
            return Response(
                serializer.data
            )
        except:
            return Response({
                'statusCode' : 405,
                'message' : 'Board does not exist'
            })


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def updateBoard(request, id):
    if request.method == 'PUT':
        num1 = random.randint(0, 9)
        value = request.data['value']
        board = Boards.objects.get(id = id, user_id = request.user.id)        
        if len(board.game_string) >= 6:
            if board.game_string == board.game_string[::-1] :
                return Response({"message" : "Palindrome", "game_string" : board.game_string})
            else:
                return Response({"message" : "Not a Palindrome", "game_string" : board.game_string})   
        if value.isalpha() and value.islower() and len(value)==1:
            pass
        else:
            return Response({
                'message' : 'Input Value Not between a and z'
            })
        
        board.game_string = board.game_string + value + str(num1)
        board.save()
        if len(board.game_string) == 6:
            if board.game_string == board.game_string[::-1] :
                return Response({"message" : "Palindrome", "game_string" : board.game_string})
            else:
                return Response({"message" : "Not a Palindrome", "game_string" : board.game_string})
        serializer = updateBoardSerializer(board) 
        return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def updateBoardString(request, id):
    if request.method == 'PUT':
        num1 = random.choice(string.ascii_letters)
        value = request.data['value']
        board = Boards.objects.get(id = id)        
        if len(board.game_string) >= 6:
            if board.game_string == board.game_string[::-1] :
                return Response({"message" : "Palindrome", "game_string" : board.game_string})
            else:
                return Response({"message" : "Not a Palindrome", "game_string" : board.game_string})   
        if value.isalpha() and value.islower() and len(value)==1:
            pass
        else:
            return Response({
                'message' : 'Input Value Not between a and z'
            })
        
        board.game_string = board.game_string + value + num1
        board.save()
        if len(board.game_string) == 6:
            if board.game_string == board.game_string[::-1] :
                return Response({"message" : "Palindrome", "game_string" : board.game_string})
            else:
                return Response({"message" : "Not a Palindrome", "game_string" : board.game_string})
        serializer = updateBoardSerializer(board) 
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication]) 
def listview(request):
    if request.method == 'GET':
        board_id = Boards.objects.all()
        serializer = listSerializer(board_id, many = True)
        return Response(
            serializer.data
        )
