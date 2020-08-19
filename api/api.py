from django.db.models import Q
from rest_framework import generics, status
from rest_framework.response import Response

from . import models
from . import serializers


class TaskListView(generics.ListCreateAPIView):
    class Meta:
        model = models.Task
        fields = '__all__'

    def get_queryset(self):
        if 'pk' in self.kwargs:
            pk = self.kwargs['pk']
            qs = models.Task.objects.filter(Q(id=pk) | Q(linked_task=pk))
        else:
            qs = models.Task.objects.all()
        return qs

    def put(self, request, pk):
        if 'linked_task' in request.data:
            linked_task = request.data['linked_task']
            task1 = self.get_object()
            serializer1 = serializers.TaskSerializer(task1, data=request.data)

            task2 = models.Task.objects.get(id=linked_task)
            serializer2 = serializers.TaskSerializer(task2, data={'linked_task': task1.id})
            if serializer1.is_valid() & serializer2.is_valid():
                serializer1.save()
                serializer2.save()
                return Response({'task1': serializer1.data, 'task2': serializer2.data})
            return Response(serializer1.error_messages, status=status.HTTP_400_BAD_REQUEST)

    serializer_class = serializers.TaskSerializer
