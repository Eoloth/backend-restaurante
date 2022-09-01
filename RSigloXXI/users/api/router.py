from django.urls import path
from rest_framework.routers import DefaultRouter
from users.api.views import UserApiViewSet, UserView

router_user = DefaultRouter()

router_user.register(
    prefix='users', basename='users', viewset=UserApiViewSet
)

#ruta de UserView para consultar info user
urlpatterns = [
    path('auth/me/', UserView.as_view())
]