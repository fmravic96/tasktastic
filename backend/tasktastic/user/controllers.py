from django.contrib.auth import get_user_model
from ninja_extra import api_controller, ModelControllerBase, ModelConfig, ModelSchemaConfig

@api_controller('/users')
class UserModelController(ModelControllerBase):
    schema_config = ModelSchemaConfig(
        exclude={'groups', 'user_permissions', 'is_staff', 'is_superuser'},
        write_only_fields=['password'],
        read_only_fields=['id', 'date_joined', 'last_login', 'is_active'],
    )
    model_config = ModelConfig(
        model=get_user_model(),
        schema_config=schema_config,
        allowed_routes=['create', 'find_one']
    )