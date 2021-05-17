
class CorrectAge:

    def __init__(self, age: int):
        if age < 16 or age > 70 or (age >= 60 and age <= 65):
            raise ValueError("Age value must be 16 to 70(inclusive) except 60 to 65(inclusive).")
        self.age = age


class IncorrectAge:

    def __init__(self, age):
        self.age = age

