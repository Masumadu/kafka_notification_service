# local imports
from app.core.repository import SQLBaseRepository
from app.models import CustomerModel
from app.services import RedisService


class CustomerRepository(SQLBaseRepository):
    model = CustomerModel

    def __init__(self, redis_service: RedisService):
        self.redis_service = redis_service
        super().__init__()