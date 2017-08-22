from schematics.models import Model
from schematics.types import ModelType, IntType


class PaginationSerializer(Model):
    total_pages = IntType(serialized_name='totalPages')


class ModelPaginationSerializer(Model):
    pagination = ModelType(PaginationSerializer)
