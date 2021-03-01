from django.urls import path
from . import views

app_name = 'notes'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.NoteDetailView.as_view(), name='detail'),
    path('note/', views.createNoteView, name='create'),
    path('edit/<int:pk>/', views.editNote, name='edit'),
    path('delete/<int:pk>', views.deleteNote, name='delete'),
]