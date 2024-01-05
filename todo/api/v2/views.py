
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .serializers import TaskSerializer
from todo.models import Task
# from .permissions import IsOwnerOrReadOnly
# from .paginations import StandardPagination

class TaskModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['category', 'author', 'status']
    # search_fields = ['title', 'content']
    # ordering_fields = ['published_date']
    # pagination_class = StandardPagination