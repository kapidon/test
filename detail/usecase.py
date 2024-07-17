from abc import ABC, abstractmethod
from .repository import BaseDetailRepository, BaseUpdateRepository


class BaseDetailUsecase(ABC):
    def __init__(self, repository: BaseDetailRepository):
        self.repository = repository

    @abstractmethod
    def execute(self, request_detail_dto):
        pass


class DetailUsecase(BaseDetailUsecase):
    def execute(self, request_detail_dto):
        obj = self.repository.find_by_id(request_detail_dto)
        return obj


class BaseUpdateUsecase(ABC):
    def __init__(self, repository: BaseUpdateRepository):
        self.repository = repository

    @abstractmethod
    def execute(self, request_detail_dto):
        pass


class UpdateUsecase(BaseUpdateUsecase):
    def execute(self, request_detail_dto):
        obj = self.repository.find_by_id(request_detail_dto)
        return obj