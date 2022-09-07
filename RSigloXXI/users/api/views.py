from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from users.models import User 
from users.api.serializers import UserSerializer
from django.contrib.auth.hashers import make_password

#CRUD PARA MODIFICAR USUARIOS
class UserApiViewSet(ModelViewSet):
    permission_class = [IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    #encriptar las contraseñas de los nuevos usuarios
    def create(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        return super().create(request, *args, **kwargs)

    #encriptar la contraseña de los usuarios cuando actualizen sus datos
    def partial_update(self, request, *args, **kwargs):
        password = request.data['password']
        if password:
            request.data['password'] = make_password(password)
        else:
            request.data['password'] = request.user.password
        return super().partial_update(request, *args, **kwargs)

#Clase unicamente para pedir informacion del usuario
class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request ):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)