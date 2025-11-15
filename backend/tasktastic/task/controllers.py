from ninja_extra import api_controller, ModelControllerBase, ModelConfig, ModelSchemaConfig
from ninja_jwt.authentication import JWTAuth

from tasktastic.task.models import Task


@api_controller('/tasks', auth=JWTAuth())
class TaskModelController(ModelControllerBase):
    schema_config = ModelSchemaConfig(
        read_only_fields=['id', 'created_at', 'updated_at', 'completed'],
        exclude=set()
    )
    model_config = ModelConfig(
        model=Task,
        schema_config=schema_config,
    )