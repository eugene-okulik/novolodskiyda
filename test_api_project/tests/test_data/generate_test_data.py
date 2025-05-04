from faker import Faker

fake = Faker()


def generate_test_data():
    return {
        "name": fake.name(),
        "data": {
            "color": fake.color(),
            "country": fake.country()
        }
    }
