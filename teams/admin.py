from django.contrib import admin
from .models import Team, Membership, Task, User


admin.site.site_title = "Task- & Team-Management API Admin"
admin.site.site_header = "Task- & Team-Management API Admin"
admin.site.site_index_title = "Task- & Team-Management API Admin"

class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 0

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')
    list_filter = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    list_filter = ('name', 'description', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('name',)
    inlines = [MembershipInline]

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('user', 'team', 'role')
    list_filter = ('user', 'team', 'role')
    search_fields = ('user__username', 'team__name')
    ordering = ('user',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Task model.
    Organizes fields into logical groups and provides filtering/search capabilities.
    """
    list_display = ('title', 'status', 'priority', 'team', 'due_date', 'created_at', 'updated_at')
    fields = (('title', 'priority', 'status'), ('description', 'due_date'), ('assigned_to', 'team'))
    search_fields = ('title',)
    ordering = ('title',)
    filter_horizontal = ('assigned_to',)

    
