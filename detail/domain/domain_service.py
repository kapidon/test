class DomainService:
    def __init__(self, master_repository, api):
        self.master_repository = master_repository
        self.api = api
    def is_duplicate_master(self, entity):
        master = self.master_repository.find_by_code(entity.code.value)
        return master is not None
    def is_correct_malls(self, entity):
        malls = api.get
        return set(entity.malls).issubset(set(malls))

class Repository:
    def find_by_code(self, code):
        try:
            return Model.objects.get(code=code)
        except Model.DoesNotExist:
            return None

class UseCase:
    if is_duplicate_master(master_entity):
        raise ValueError(すでに登録されているコードです)
    if not is_correct_malls(master_entity):
        raise ValueError('モールがおかしい')