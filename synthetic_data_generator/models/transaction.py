from pydantic import BaseModel

class TransactionRecord(BaseModel):
    transaction_id: str
    customer_id: str
    transaction_amount: float
    transaction_date: str
    payment_method: str
    product_category: str
    quantity: int
    customer_age: int
    customer_location: str
    device_used: str
    ip_address: str
    shipping_address: str
    billing_address: str
    is_fraudulent: int
    account_age_days: int
    transaction_hour: int