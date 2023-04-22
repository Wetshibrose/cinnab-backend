from rest_framework.permissions import BasePermission, SAFE_METHODS

from rest_framework.response import Response

# models
from .models import Brand, BrandLogo
from users.models import User

# utility function
from .utility_func import jwt_authentication

class BrandsPermissions(BasePermission):

    def has_object_permission(self, request, view, obj:Brand):
        response = jwt_authentication(req=request)
        if response is Response:
            return False
        
        user:User = response
        if request.method in SAFE_METHODS:
            return user.has_perm("can_view_brand")
        
        if user.is_staff:
            return True
        
        if request.method == "POST":
            return user.has_perm("can_add_brand")
        
        if request.method in ["PUT", "PATCH"]:
            return user.has_perm("can_edit_brand")
        
        if request.method == "DELETE":
            return user.has_perm("can_delete_brand")
        
        