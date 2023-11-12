from django.urls import path
from . import views
from .views import LikeView, UnlikeView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns=[
    path('', views.index, name='index'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('photo/', views.photo, name='photo'),
    path('authorisation/', views.authorisation, name='authorisation'),
    path('registration/', views.registration, name='registration'),
    path('api/post/<int:id>/like/', LikeView.as_view()),
    path('api/post/<int:id>/unlike/', UnlikeView.as_view()),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
