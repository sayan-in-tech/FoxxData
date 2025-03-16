from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_experimental.tabular_synthetic_data.prompts import (
    SYNTHETIC_FEW_SHOT_PREFIX,
    SYNTHETIC_FEW_SHOT_SUFFIX,
)

# Example data for few-shot prompting
examples = [
    { "example": """transaction_id: 44e09e24-74b9-4041-9894-8734ad525faa, customer_id: 379, transaction_amount: 10.01, transaction_date: 10/01/2024 20:08, payment_method: debit card, product_category: home & garden, quantity: 4, customer_age: 37, customer_location: Christopherland, device_used: desktop, ip_address: 211.189.218.190, shipping_address: 471 Mary Courts Apt. 872\nMaryhaven, KS 16126, billing_address: 471 Mary Courts Apt. 872\nMaryhaven, KS 16126, is_fraudulent: 1, account_age_days: 30, transaction_hour: 20"""},
    {"example": """transaction_id: aa81b9ff-034d-4d8e-bec6-ed29b8ae5d54, customer_id: 19.25, transaction_amount: 11/02/2024 16:54, transaction_date: bank transfer, payment_method: clothing, product_category: 1, quantity: 32, customer_age: Marymouth, customer_location: mobile, device_used: 126.224.150.175, ip_address: 68763 Bryant Points Suite 057\nGuzmanfort, ME 02932, shipping_address: 139 Lopez Neck\nCarterview, DE 85571, billing_address: 0, is_fraudulent: 131, account_age_days: 16, transaction_hour: 16"""},
    {"example": """transaction_id: 7ac1febd-3e94-457e-bfe4-acf081dc8da0, customer_id: 104.07, transaction_amount: 07/01/2024 15:41, transaction_date: PayPal, payment_method: electronics, product_category: 1, quantity: 43, customer_age: Paynefurt, customer_location: tablet, device_used: 195.31.145.184, ip_address: Unit 5864 Box 9572\nDPO AE 69746, shipping_address: Unit 5864 Box 9572\nDPO AE 69746, billing_address: 0, is_fraudulent: 53, account_age_days: 15, transaction_hour: 15"""},
]

# Define the prompt template
EXAMPLE_TEMPLATE = PromptTemplate(input_variables=["example"], template="{example}")

def get_prompt_template() -> FewShotPromptTemplate:
    return FewShotPromptTemplate(
        prefix=SYNTHETIC_FEW_SHOT_PREFIX,
        examples=examples,
        suffix=SYNTHETIC_FEW_SHOT_SUFFIX,
        input_variables=["subject", "extra"],
        example_prompt=EXAMPLE_TEMPLATE,
    )