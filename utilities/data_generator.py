from faker import Faker


class UserData:
    def __init__(self):
        self.faker = Faker()

    def generate_text_box(self):
        return {
            "full_name": self.faker.name(),
            "email": self.faker.email(),
            "current_address": self.faker.address(),
            "permanent_address": self.faker.address()
        }