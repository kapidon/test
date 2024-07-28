from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class ValueObject1:
    value: str
    error_messages: List[str]
    succes_messages: List[str]

    def __post_init__(self):
        self.validate()
    
    def validate(self):
        if(Validator.is_empty(self.value)):
            self.error_messages.append('ValuObject1必須です')
        if(Validator.is_int(self.value)):
            self.succes_messages.append('整数です')

    def is_valid(self):
        return len(self.error_messages) == 0

@dataclass(frozen=True)
class ValueObject2:
    value: str
    error_messages: List[str]
    succes_messages: List[str]

    def __post_init__(self):
        self.validate()
    
    def validate(self):
        if(Validator.is_empty(self.value)):
            self.error_messages.append('ValuObject2必須です')
        if(Validator.is_int(self.value)):
            self.succes_messages.append('整数です')

    def is_valid(self):
        return len(self.error_messages) == 0

@dataclass
class Entity:
    valueObject1: ValueObject1
    valueObject2: ValueObject2

    def __post_init__(self):
        if not (self.valueObject1.is_valid):
            raise ValueError('¥n'.join(self.valueObject1.error_messages))
        

class Factory:
    @staticmethod
    def create_entity():

class UseCase:
    def execute(self):

最終的にテンプレートの各input(ValueObject)にエラーメッセージまたは成功メッセージを表示できるようにしたいです。
Djangoのクリーンアーキテクチャ的に最適な方法を教えて
        
class Validator:
    @staticmethod
    def is_empty(value):
        return not value

    @staticmethod
    def is_int(value):
        try:
            int(value)
            return True
        except ValueError:
            return False
class Validator:
    @staticmethod
    def is_empty(value):
        return not value

    @staticmethod
    def is_int(value):
        try:
            int(value)
            return True
        except ValueError:
            return False

