from rest_framework import permissions
from rest_framework.generics import get_object_or_404

from .models import Project

class IsAuthor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method not in permissions.SAFE_METHODS:
            return obj.author == request.user or request.user.is_superuser

        return True


class IsProjectAuthorOrContributor(permissions.BasePermission):
    
    def has_permission(self, request, view):
        project_pk = view.kwargs['project_pk']
        if not project_pk:
            return False
        
        project = get_object_or_404(Project, pk=project_pk)
        is_project_author = (request.user == project.author)
        is_project_contributor = (request.user in project.contributors.all())
        is_superuser = request.user.is_superuser

        return is_project_author or is_project_contributor or is_superuser
