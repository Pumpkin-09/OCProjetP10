from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from authentication.permissions import IsRequestUser
from authentication.serializers import UserSerializer
from authentication.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [permissions.AllowAny]

        else:
            permission_classes = [IsRequestUser]
        
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        if self.action == 'list' and not self.request.user.is_staff:
            if self.request.user.is_authenticated:
                return User.objects.filter(id=self.request.user.id)
            return User.objects.none()
        
        return super().get_queryset()
    