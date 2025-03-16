from synthetic_data_generator.services.data_generator import DataGenerator
from synthetic_data_generator.services.file_handler import save_to_csv
from synthetic_data_generator.utils.logger import setup_logger
import pandas as pd
import os
from dotenv import load_dotenv

logger = setup_logger()

def run_application():
    """
    Main function to run the synthetic data generation application.
    """
    logger.info("Starting synthetic data generation...")

    # Initialize the data generator
    generator = DataGenerator(api_key=os.getenv("GOOGLE_API_KEY"))

    # Generate synthetic data
    num_records = 5
    synthetic_results = generator.generate(
        num_records=num_records,
        subject="TransactionRecord",
        extra=f"Generate exactly {num_records} examples of fraudulent e-commerce transactions."
    )

    # Convert to DataFrame
    data = [record.dict() for record in synthetic_results]
    df = pd.DataFrame(data)
    print(df)
    logger.info(f"Generated {len(synthetic_results)} out of {num_records} requested transactions.")

    # Save to CSV file
    save_to_csv(df)