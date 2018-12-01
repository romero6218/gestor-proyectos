from django.urls import path

from . import views, conf

urlpatterns = [
    path("create/", views.Create.as_view(), name=conf.PROYECTO_CREATE_URL_NAME),
    path("lista/", views.ListPost.as_view(), name=conf.PROYECTO_LIST_URL_NAME),
    path("<int:pk>/", views.DetallePost.as_view(), name=conf.PROYECTO_DETAIL_URL_NAME),
    path("<int:pk>/actualizar/", views.ActualizarPost.as_view(), name=conf.PROYECTO_UPDATE_POST_URL_NAME)
]