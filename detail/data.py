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

class CsvProcessor:
    def __init__(self, brand_factory, file_log_factory, file_log_repository, brand_repository, file_row_log_factory, file_row_log_repository):
        self.brand_factory = brand_factory
        self.file_log_factory = file_log_factory
        self.file_log_repository = file_log_repository
        self.brand_repository = brand_repository
        self.file_row_log_factory = file_row_log_factory
        self.file_row_log_repository = file_row_log_repository

    def process_csv_contents(self, csv_contents):
        brand_entities = []
        file_row_log_entities = []
        file_log_entity = self.file_log_factory.create(message='開始')
        self.file_log_repository.create(file_log_entity)

        try:
            for index, csv_content in enumerate(csv_contents):
                self._process_csv_row(index, csv_content, brand_entities, file_row_log_entities)
                
            self.brand_repository.bulk_create(brand_entities)
            self.file_row_log_repository.bulk_create(file_row_log_entities)
            file_log_entity.update(message='完了')
            self.file_log_repository.save(file_log_entity)

        except Exception as e:
            file_log_entity.update(message=str(e))
            self.file_log_repository.save(file_log_entity)

    def _process_csv_row(self, index, csv_content, brand_entities, file_row_log_entities):
        try:
            brand_entity = self.brand_factory.create_entity_from_csv(csv_content)
            if not brand_entity.is_valid():
                raise ValueError(brand_entity.error_messages_dict)
            brand_entities.append(brand_entity)
            file_row_log_entity = self.file_row_log_factory.create_entity(line_num=index, message='成功')
            file_row_log_entities.append(file_row_log_entity)
        except ValueError as e:
            error_message = '\n'.join(e.args[0])
            file_row_log_entity = self.file_row_log_factory.create_entity(line_num=index, message=error_message)
            file_row_log_entities.append(file_row_log_entity)

# 呼び出し例
processor = CsvProcessor(brand_factory, file_log_factory, file_log_repository, brand_repository, file_row_log_factory, file_row_log_repository)
processor.process_csv_contents(csv_contents)
