

class Card:
    def __init__(self, number, shape):
        self.number = number
        self.shape = shape

    def check_number(self):
        letter = ["A", "K", "Q", "J"]
        if isinstance(self.number, int):
            if self.number < 2 or self.number > 10:
                return False
        elif isinstance(self.number, str):
            if self.number not in letter:
                return False
        return True

    def to_dict(self):
        as_a_dict = {}
        number = self.number
        shape = self.shape
        as_a_dict["card number"] = number
        as_a_dict["shape"] = shape
        return as_a_dict
    def to_string(self):
        if self.number == 11:
            self.number = "J"
        elif self.number == 12:
            self.number = "Q"
        elif self.number == 13:
            self.number = "K"
        elif self.number == 14:
            self.number = "A"



    def from_string(self):
        if self.number == "J":
            self.number = 11
        elif self.number == "Q":
            self.number = 12
        elif self.number == "K":
            self.number = 13
        elif self.number == "A":
            self.number = 14
        return self.number


