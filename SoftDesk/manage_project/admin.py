from django.contrib import admin
from authentication.models import User
from manage_project.models import Project, Issue, Comment


admin.site.register(User)
admin.site.register(Project)
admin.site.register(Issue)
admin.site.register(Comment)
