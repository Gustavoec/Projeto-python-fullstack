from django.urls import path
from . import views

app_name = 'chamados'

urlpatterns = [
    path('', views.lista_chamados, name='lista_chamados'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('cliente/novo/', views.criar_cliente, name='criar_cliente'),
    path('novo/', views.criar_chamado, name='criar_chamado'),
    path('chamado/<int:pk>/pdf/', views.gerar_pdf_os, name='gerar_pdf_os'),
    path('chamado/<int:pk>/status/<str:novo_status>/', views.alterar_status_rapido, name='alterar_status_rapido'),
]