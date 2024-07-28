from dataclasses import dataclass


from dataclasses import dataclass
from typing import List, Dict

from dataclasses import dataclass, field
from typing import List

@dataclass
class ValueObject:
    value: str
    error_messages: List[str] = field(default_factory=list)
    success_messages: List[str] = field(default_factory=list)

    def __post_init__(self):
        self.validate()

    def validate(self):
        raise NotImplementedError("Subclasses should implement validate method")

    def is_valid(self) -> bool:
        return len(self.error_messages) == 0

@dataclass
class ValueObject1(ValueObject):
    def validate(self):
        if Validator.is_empty(self.value):
            self.error_messages.append("ValueObject1は必須です")
        if Validator.is_int(self.value):
            self.success_messages.append("整数です")

@dataclass
class ValueObject2(ValueObject):
    def validate(self):
        if Validator.is_empty(self.value):
            self.error_messages.append("ValueObject2は必須です")
        if Validator.is_int(self.value):
            self.success_messages.append("整数です")


@dataclass
class EntityDTO:
    value_object1: str
    value_object2: str
    error_messages: Dict[str, str]
    success_messages: Dict[str, str]

@dataclass
class Entity:
    value_object1: ValueObject1
    value_object2: ValueObject2
    error_messages: dict = field(default_factory=dict)
    success_messages: List[str] = field(default_factory=list)

    def __post_init__(self):
        if not self.value_object1.is_valid():
            self.error_messages['value_object1'] = "\n".join(self.value_object1.error_messages)
        else:
            self.success_messages.extend(self.value_object1.success_messages)
        
        if not self.value_object2.is_valid():
            self.error_messages['value_object2'] = "\n".join(self.value_object2.error_messages)
        else:
            self.success_messages.extend(self.value_object2.success_messages)

    def is_valid(self) -> bool:
        return len(self.error_messages) == 0


@dataclass
class DetailRequestDTO:
    pk: int

@dataclass
class FilterParamsDTO:
    codefilter: str
    idfilter: int

    def __post_init__(self):
        self.validate()

    def validate(self):
        if(Validator.is_empty(self.codefilter)):
            raise ValidationError('codeを入力してください')
        if(Validator.is_empty(self.codefilter)):
            raise ValidationError('idを入力してください')

class ValidationError(Exception):
    def __init__(self, message, field):
        self.message = message
        self.field = field
        super.__init__(self, self.field)

class Validator:
    @staticmethod
    def is_empty(value):
        bool(value)

