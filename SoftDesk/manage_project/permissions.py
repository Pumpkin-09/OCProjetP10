from rest_framework import permissions


class IsAuthorOrContributor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in ["destroy", "partial_update", "update"]:
            return obj.author == request.user or request.user.is_superuser
        
        elif request.method in permissions.SAFE_METHODS:
            return obj.contributor.filter(id=request.user.id).exists() or request.user.is_superuser or obj.author == request.user

        return False
