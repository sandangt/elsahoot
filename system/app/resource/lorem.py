from faker import Faker

from app.constant import SEED_NUMBER

faker = Faker()
faker.seed_instance(SEED_NUMBER)
