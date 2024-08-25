from typing import Any, Dict
from django.views.generic import TemplateView


class TestView(TemplateView):
    template_name = 'test.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        dict = {'a': 'あ', 'b': 'ぶ', 'c': 'ちゅ', 'd': 'ぢゅ'}
        context.update({'dict':dict})
        return context