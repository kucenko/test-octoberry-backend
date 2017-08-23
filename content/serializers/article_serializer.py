from schematics.models import Model
from schematics.types import IntType, StringType, ModelType, ListType

from .user_serializer import UserSerializer
from .comment_serializer import CommentSerializer


class ArticleDetailSerializer(Model):
    id = IntType()
    user = ModelType(UserSerializer, serialized_name='author')
    title = StringType()
    text = StringType()
    comments = ListType(ModelType(CommentSerializer))
