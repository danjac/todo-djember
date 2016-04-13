from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import TodoItem
from .serializers import TodoItemSerializer
from .permissions import BelongsToUser


class TodoItemViewSet(viewsets.ModelViewSet):

    serializer_class = TodoItemSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, BelongsToUser, )

    def get_queryset(self):
        if self.request.user.is_authenticated():
            return TodoItem.objects.filter(user=self.request.user)
        return TodoItem.objects.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
