from freight.models import User

from .base import Serializer
from .manager import add


@add(User)
class UserSerializer(Serializer):
    def serialize(self, item, attrs):
        return {
            "id": str(item.id),
            "name": item.name,
            "dateCreated": self.format_datetime(item.date_created),
        }
