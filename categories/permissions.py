from rest_framework.permissions import BasePermission, SAFE_METHODS

# rest requests,response
from rest_framework.response import Response

# utility functions
from .utility_func import jwt_authentication

# models
from .models import Category
from users.models import User
from businesses.models import Business

class CategoriesPermissions(BasePermission):
    message = "You don't have permissions to edit categories"
    
    def has_object_permission(self, request, view, obj:Category):
        if request.method in SAFE_METHODS:
            return True
        
        response = jwt_authentication(req=request)
        if response is Response:
            return False
        
        user:User = response
        business:Business = user.businesses.filter(id=obj.business.id).first()
        
        is_permitted:bool = False
        if business:
            is_permitted = True
        else:
            if user.is_staff:
                is_permitted = True
        
        return is_permitted
        
