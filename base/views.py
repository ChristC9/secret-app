from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import todo
from .serializers import TodoSerializer
# Create your views here.


@api_view(['GET'])
def get_todos(request,pk=None):
    data=request.data
    if pk:
        if todo.objects.filter(id=pk).exists():
            todo_obj=todo.objects.get(id=pk)
            return Response({'id':todo_obj.id,'title':todo_obj.title,'body':todo_obj.body})
        return Response({'details':f'Id {pk} not found'})
    
    todolist=todo.objects.all()
    serialzier=TodoSerializer(todolist,many=True)
    return Response(serialzier.data)


@api_view(['POST'])
def create_todo(request):
    data=request.data
    todo.objects.create(
        title=data['title'],
        body=data['body']
    )
    return Response({'details':'Todo created successfully'})
