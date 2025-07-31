from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.exceptions import PermissionDenied

from manage_project.models import Project, Issue, Comment
from manage_project.serializers import ProjectSerializer, IssueSerializer, CommentSerializer
from manage_project.permissions import IsAuthorOrContributor, IsProjectAuthorOrContributor


class ProjetViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrContributor]
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Project.objects.all()
        return Project.objects.filter(
            Q(author=self.request.user) | Q(contributor=self.request.user)
        ).distinct()


class IssueViewSet(ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticated, IsProjectAuthorOrContributor, IsAuthorOrContributor]

    def get_queryset(self):
        project_pk = self.kwargs['project_pk']
        project = get_object_or_404(Project, pk=project_pk)
        if self.request.user in project.contributors.all() or self.request.user == project.author or self.request.user.is_superuser:
            return Issue.objects.filter(project=project_pk)
        raise PermissionDenied("Vous n'avez pas accès à cette fonctionnalité")
    
    def perform_create(self, serializer):
        project_pk = self.kwargs['project_pk']
        project = get_object_or_404(Project, pk=project_pk)
        serializer.save(author=self.request.user, project=project)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsProjectAuthorOrContributor, IsAuthorOrContributor]

    def get_queryset(self):
        issue_pk = self.kwargs['issue_pk']
        project_pk = self.kwargs['project_pk']
        project = get_object_or_404(Project, pk=project_pk)
        if self.request.user in project.contributors.all() or self.request.user == project.author or self.request.user.is_superuser:
            return Comment.objects.filter(
                issue=issue_pk,
                issue__project=project_pk
            )
        raise PermissionDenied("Vous n'avez pas accès à cette fonctionnalité")

    def perform_create(self, serializer):
        issue_pk = self.kwargs['issue_pk']
        project_pk = self.kwargs['project_pk']

        issue = get_object_or_404(Issue, pk=issue_pk, project=project_pk)
        serializer.save(author=self.request.user, issue=issue)

