# python
import factory
from django.contrib.auth import get_user_model

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = factory.Faker("user_name")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    password = factory.PostGenerationMethodCall("set_password", "defaultpassword")
    is_active = True
