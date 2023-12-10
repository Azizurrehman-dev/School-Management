from rest_framework.permissions import IsAuthenticated


class CustomPermission(IsAuthenticated):
    def has_permission(self, request, view):
        try:

            if super().has_permission(request, view):
                user = request.user
                if user.is_admin:
                    return True
                request_type, model = request.method, view.queryset.model.__name__

                if request_type == "GET" and model == "Class":
                    return True
        except Exception as e:
            print("ERROR : ", e)
            print("ERROR : ", e)
