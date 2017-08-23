from schematics.models import Model
from schematics.types import IntType, StringType


class UserSerializer(Model):
    id = IntType()
    name = StringType()
