from django.shortcuts import render, get_object_or_404
from django.views.generic import base, ListView, DetailView
from .models import Worker, Service, Schedule


class MenuView(base.TemplateView):
    template_name = 'client/menu.html'


class WorkersView(ListView):
    model = Worker
    template_name = 'client/workers.html'
    context_object_name = 'workers'


class ServiceView(DetailView):
    model = Worker
    template_name = 'client/services.html'


def date_time(request, pk):
    worker = get_object_or_404(Worker, pk=pk)
    # selected_services = worker.service_set.get(???)

    return render(request, 'client/date_time.html', {'worker': worker.worker_name, })
