from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from rest_framework.permissions import AllowAny
from .models import Task, User
from .serializers import TaskSerializer, RegisterSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'priority']
    search_fields = ['title', 'description']


    def perform_create(self, serializer):
        task = serializer.save()
        task.assigned_to.add(self.request.user)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


# Home View (Temporary)
def home(request):
    return HttpResponse("<h1>Welcome to the Task & Team Management API</h1><p>Visit <a href='/api/docs/'>API Documentation</a> to get started.</p>")