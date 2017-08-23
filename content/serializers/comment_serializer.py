from schematics.models import Model
from schematics.types import IntType, StringType, ModelType

from .user_serializer import UserSerializer


class CommentSerializer(Model):
    id = IntType()
    text = StringType()
    user = ModelType(UserSerializer, serialized_name='commenter')
