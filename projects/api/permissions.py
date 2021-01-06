from rest_framework import permissions


class IsProjectOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsTaskOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.project.user == request.user
