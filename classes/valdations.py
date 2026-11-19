
class Validation:
    def is_int(self, number):
        try:
            int(number)
            return True
        except ValueError:
            return False

    def is_str(self, word):
        if not word.strip():
            return False
        return True

    def main_choose_checker(self, number):
        if not self.is_int(number):
            return False
        number = int(number)
        if number < 1 or number > 2:
            return False
        return True

