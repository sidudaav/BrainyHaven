from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'api'

router = routers.SimpleRouter()
router.register('patterns', views.PatternViewSet)
router.register('analogies', views.AnalogyViewSet)
router.register('riddles', views.RiddleViewSet)

urlpatterns = [
    path('', include(router.urls))
]