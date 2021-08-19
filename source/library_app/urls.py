from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('document/<str:pk>/',views.document, name='document'),
    path('type/<str:type>/', views.types, name='type'),
    path('section/<str:section>/', views.sections, name='section'),
    path('home/', views.home, name='home'),
    path('tag/<slug:tag_slug>/', views.dashboard, name='tag'),
    path('delete/<str:pk>', views.document_delete, name='document_delete'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name='logout')
]