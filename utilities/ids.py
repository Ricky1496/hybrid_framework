class Father:
    def __init__(self):
        self.f_age = 65


class Son(Father):
    def __init__(self, f_age):
        super().__init__()
        self.s_age = 20


s = Son(70)
print(s.f_age)