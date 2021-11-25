from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.projects, name='projects'),
    path('project/<str:pk>/', views.project, name='project'),
    path('create_project/', views.create_project, name='create_project'),
    path('update-project/<str:pk>/', views.updateproject, name='update-project'),
    path('delete-project/<str:pk>/', views.delete_project, name='delete-project'),
]




urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)