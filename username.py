
class CorrectUsername:

    def __init__(self, username: str):
        if len(username) < 7 or len(username) > 10:
            raise ValueError("Usernames must be between 7 and 10 characters(inclusive).")

        self.username = username


class IncorrectUsername:

    def __init__(self, username):
        self.username = username

