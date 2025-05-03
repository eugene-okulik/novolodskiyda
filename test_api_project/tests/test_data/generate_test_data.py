from faker import Faker

fake = Faker()


def generate_test_data():
    """Generate test data for API testing.
    
    Returns:
        dict: Dictionary containing test data with name, color and country.
    """
    return {
        "name": fake.name(),
        "data": {
            "color": fake.color(),
            "country": fake.country()
        }
    } 
