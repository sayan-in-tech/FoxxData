from langchain_google_genai import ChatGoogleGenerativeAI
from synthetic_data_generator.prompts.templates import get_prompt_template
from synthetic_data_generator.models.transaction import TransactionRecord
from synthetic_data_generator.services.parser import parse_gemini_response
from pydantic import ValidationError

class DataGenerator:
    def __init__(self, api_key: str, model: str = "gemini-2.0-flash"):
        self.llm = ChatGoogleGenerativeAI(model=model, google_api_key=api_key)
        self.prompt_template = get_prompt_template()

    def generate(self, num_records: int, subject: str, extra: str) -> list[TransactionRecord]:
        formatted_prompt = self.prompt_template.format(
            subject=subject,
            extra=extra
        )
        response = self.llm.invoke(formatted_prompt)
        parsed_data = parse_gemini_response(response.content)
        
        synthetic_results = []
        for data in parsed_data:
            try:
                record = TransactionRecord.parse_obj(data)
                synthetic_results.append(record)
            except ValidationError as e:
                print(f"Skipping invalid record: {e}")
            except Exception as e:
                print(f"Error processing record: {e}")
        
        return synthetic_results