from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController

from tasktastic.task.controllers import TaskModelController
from tasktastic.user.controllers import UserModelController

api = NinjaExtraAPI()
api.register_controllers(UserModelController)
api.register_controllers(NinjaJWTDefaultController)
api.register_controllers(TaskModelController)