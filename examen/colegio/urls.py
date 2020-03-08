from   django.urls import path, include
from   rest_framework.routers import DefaultRouter 
import colegio.views.users as user_views
import colegio.views.cursos as curso_views
import colegio.views.asign as asign_views
router = DefaultRouter()
router.register(r'users', user_views.UserViewSet, basename='users'),
router.register(r'cursos', curso_views.CursoViewSet, basename='cursos')
router.register(r'asign', asign_views.AsignViewSet, basename='asign')

urlpatterns = [
    path('', include(router.urls))
]