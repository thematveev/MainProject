class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class BusinessUser(User):
    def __init__(self, name, age, company=None):
        super().__init__(name, age)
        self.company = company


class VipUser(BusinessUser):
    def __init__(self, name, age, company, lvl):
        super().__init__(name, age, company)
        self.lvl = lvl
