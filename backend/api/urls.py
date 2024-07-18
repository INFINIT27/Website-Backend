from django.urls import path
from . import views

urlpatterns = [
    path("notes/", views.NoteListCreate.as_view(), name="note-list"),
    path("notes/delete/<int:pk>/", views.NoteDelete.as_view(), name="delete-note"),
    path("classes/", views.ClassListCreate.as_view(), name="class-list"),
    path("classes/delete/<int:pk>/", views.ClassDelete.as_view(), name="class-note"),
]