from typing import Any, Dict
from django.views.generic import TemplateView, View
from .data import DetailRequestDTO
from .controller import DetailController
from .usecase import DetailUsecase
from .repository import DetailRepository

from django.shortcuts import render
from django.views import View
from .use_cases import UseCase
from .repositories import Repository

class MyView(View):
    def get(self, request):
        return render(request, 'template.html')

    def post(self, request):
        value1 = request.POST.get('value1')
        value2 = request.POST.get('value2')

        repository = Repository()
        use_case = UseCase(repository)
        dto = use_case.execute(value1, value2)

        return render(request, 'template.html', {
            'dto': dto,
        })

class ListView(TemplateView):
    template_name = 'list.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        context.update({'list':list})
        return context

class DetailView(TemplateView):
    template_name = 'detail.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        repository = DetailRepository()
        usecase = DetailUsecase(repository)
        controller = DetailController(usecase)
        detail_request_dto = DetailRequestDTO(pk=kwargs['pk'])
        init_obj = controller.handle_request(detail_request_dto)
        context.update({
            'init_obj': init_obj,
        })
        return context

class UpdateView(View):
    def post(self, request, *args, **kwargs):
        pass