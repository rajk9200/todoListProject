from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TodoSerializer
from task.models import Task
from django.shortcuts import get_object_or_404

class TaskListCreateView(APIView):
    def get(self, request):
        query = request.GET.get("search")
        if query:
            tasks = Task.objects.filter(title__icontains=query)
        else:
            tasks = Task.objects.filter().order_by('-id')

        serializer = TodoSerializer(tasks, many=True)
        return Response({
            'message': "Tasks retrieved successfully.",
            'data': serializer.data
        })

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': "Task created successfully.",
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetailView(APIView):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TodoSerializer(task)
        return Response({
            'message': "Task retrieved successfully.",
            'data': serializer.data
        })

    def put(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TodoSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': "Task updated successfully.",
                'data': serializer.data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return Response({
            'message': "Task deleted successfully."
        }, status=status.HTTP_204_NO_CONTENT)
