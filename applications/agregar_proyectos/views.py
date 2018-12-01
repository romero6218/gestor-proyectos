from django.views.generic import (CreateView, ListView, TemplateView, DetailView, UpdateView, DeleteView)
from . import (models, forms, conf)
from django.urls import reverse


# Create your views here.

class Create(CreateView):
    model = models.Proyecto
    form_class = forms.Form_proyecto
    template_name = "create.html"
    def get_success_url(self):
        return  reverse(conf.PROYECTO_DETAIL_URL_NAME, self.get_object().id)

    def form_valid(self, form):
        print(form)
        return super(Create, self).form_valid(form)

class ListPost(ListView):
    queryset = models.Proyecto.objects.all()
    template_name = "list.html"
    context_object_name = "lista"

class DetallePost(DetailView):
    model = models.Proyecto
    template_name = "detail.html"
    context_object_name = "proyecto"

class ActualizarPost(UpdateView):
    model = models.Proyecto
    form_class = forms.Form_proyecto
    template_name = "actualizar.html"
    success_url = "/"
