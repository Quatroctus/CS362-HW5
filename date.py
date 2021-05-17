
class CorrectDate:

    def __init__(self, date: int):
        if date > 31 and date < 1:
            raise ValueError("Date must be a value between 1 and 31(inclusive).")
        self.date = date


class IncorrectDate:

    def __init__(self, date):
        self.date = date


