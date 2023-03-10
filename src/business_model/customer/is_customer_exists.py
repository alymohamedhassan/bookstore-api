from src.business_model.customer.get_customer import GetCustomer
from src.business_model.customer.get_customer_by_email import GetCustomerByEmail
from src.core.business_model import BusinessModel, ModelType
from src.data_model.customer import Customer
from src.interface.customer import ICustomer


class IsCustomerExists(BusinessModel):
    def __init__(self, customer_id: int):
        super().__init__(
            model=Customer(),
            model_type=ModelType.read
        )

        self.customer_id = customer_id

    def run(self, data: dict = None, conditions: dict = None) -> dict:
        customer = GetCustomer(
            customer_id=self.customer_id
        ).run()

        return len(customer) > 0
