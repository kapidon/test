from abc import ABC, abstractmethod
from .repository import BaseDetailRepository, BaseUpdateRepository

class UseCase:
    def __init__(self, repository: Repository):
        self.repository = repository

    def execute(self, value1: str, value2: str) -> EntityDTO:
        try:
            entity = Factory.create_entity(value1, value2)
            if entity.is_valid():
                self.repository.save(entity)
                return EntityDTO(
                    value_object1=value1,
                    value_object2=value2,
                    error_messages=entity.error_messages,
                    success_messages=entity.success_messages
                )
            else:
                return EntityDTO(
                    value_object1=value1,
                    value_object2=value2,
                    error_messages=entity.error_messages,
                    success_messages=[]
                )
        except Exception as e:
            return EntityDTO(
                value_object1=value1,
                value_object2=value2,
                error_messages={"unexpected_error": str(e)},
                success_messages=[]
            )

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