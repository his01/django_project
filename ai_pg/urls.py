from django.urls import path
from . import views

urlpatterns = [
    path('', views.ai_pg),
    path('ai_tool_guide/', views.ai_tool_guide),
    path('ai_sld/', views.ai_sld),
    path('ai_pjrv/', views.ai_pjrv),
]