from abc import ABC, abstractmethod
from .usecase import BaseDetailUsecase, BaseUpdateUsecase


class BaseDetailController(ABC):
    def __init__(self, usecase: BaseDetailUsecase):
        self.usecase = usecase

    @abstractmethod
    def handle_request(self, request_detail_dto):
        pass


class DetailController(BaseDetailController):
    def handle_request(self, request_detail_dto):
        obj = self.usecase.execute(request_detail_dto)
        return obj

class BaseUpdateController(ABC):
    def __init__(self, usecase: BaseUpdateUsecase):
        self.usecase = usecase

    @abstractmethod
    def handle_request(self, request_detail_dto):
        pass

class UpdateController(BaseUpdateController):
    def handle_request(self, request_detail_dto):
        obj = self.usecase.execute(request_detail_dto)
        return obj

