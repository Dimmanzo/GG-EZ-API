from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsStaffOrReadOnly(BasePermission):
    """
    Custom permission to allow only staff users or superusers to edit or delete objects.
    Read-only permissions for others, including anonymous users.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        
        return (
            request.user.is_authenticated and
            (request.user.role == 'staff_user' or request.user.is_superuser)
        )