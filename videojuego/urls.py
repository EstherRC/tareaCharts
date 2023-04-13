from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'estudiante', views.EstudianteViewSet)
router.register(r'intentos', views.IntentosViewSet)
router.register(r'juego', views.JuegoViewSet)

urlpatterns = [
    path('api', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('',views.index, name='index'),
    path('charts',views.charts, name='charts'),
]