from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    """
    Inheritng basepermision and ovveride the has_object_permision method
    to return boolean on owner of an object
    """
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user