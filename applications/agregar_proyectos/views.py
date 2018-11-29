from django.shortcuts import render
from django.views.generic import (CreateView, ListView)
from . import (models, forms)
# Create your views here.

class Create(CreateView):
    model = models.Proyecto
    form_class = forms.Form_proyecto
    template_name = "create.html"
    success_url = "/prueba/create/"

    def form_valid(self, form):
        print(form)
        return super(Create,self).form_valid(form)

class ListPost(ListView):
    queryset = models.Proyecto.objects.all()
    template_name =

