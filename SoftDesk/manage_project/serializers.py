from rest_framework import serializers
from manage_project.models import Project, Issue, Comment
from django.shortcuts import get_object_or_404


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "title", "description", "author", "contributors", "project_type", "time_created"]
        read_only_fields = ["time_created", "author"]

    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user
        project = super().create(validated_data)
        return project

    def update(self, instance, validated_data):
        contributors_data = validated_data.pop("contributors", None)
        instance = super().update(instance, validated_data)
        if contributors_data is not None:
            instance.contributors.set(contributors_data)
        
        return instance


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ["id", "title", "description", "author", "assigned_user", "project", "time_created", "project_status", "project_tag", "project_priority"]
        read_only_fields = ["author", "project", "time_created"]

    def validate_assigned_user(self, value):
        if self.instance:
            project = self.instance.project
        else:
            project_pk = self.context['view'].kwargs.get('project_pk')
            project = get_object_or_404(Project, pk=project_pk)
        
        for user in value:
            if not (project.contributors.filter(id=user.id).exists() or project.author == user):
                raise serializers.ValidationError(
                    f"L'utilisateur '{user.username}' n'est pas membre du projet"
                )
        
        return value

    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user
        issue = super().create(validated_data)

        return issue

    def update(self, instance, validated_data):
        assigned_user_data = validated_data.pop("assigned_user", None)
        instance = super().update(instance, validated_data)
        if assigned_user_data is not None:
            instance.assigned_user.set(assigned_user_data)
        
        return instance


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["description", "author", "issue", "id", "time_created"]
        read_only_fields = ["author", "issue", "id", "time_created"]

    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user
        comment = super().create(validated_data)
        
        return comment