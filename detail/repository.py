from abc import ABC, abstractmethod


class BaseDetailRepository(ABC):
    @abstractmethod
    def find_by_id(self, request_detail_dto):
        pass

from .models import Blog

class DetailRepository(BaseDetailRepository):
    def find_by_id(self, request_detail_dto):
        print(request_detail_dto.pk)
        blog = Blog.objects.get(id=request_detail_dto.pk)
        return blog


class BaseUpdateRepository(ABC):
    @abstractmethod
    def find_by_id(self, request_detail_dto):
        pass

from .models import Blog

class UpdateRepository(BaseDetailRepository):
    def find_by_id(self, request_detail_dto):
        print(request_detail_dto.pk)
        blog = Blog.objects.get(id=request_detail_dto.pk)
        return blog
