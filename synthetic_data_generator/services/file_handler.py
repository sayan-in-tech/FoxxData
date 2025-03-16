import os
import pandas as pd
from datetime import datetime
from synthetic_data_generator.utils.logger import setup_logger

logger = setup_logger()

def ensure_directory_exists(directory: str):
    """
    Ensure the specified directory exists. If not, create it.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
        logger.info(f"Created directory: {directory}")

def save_to_csv(df: pd.DataFrame, output_dir: str = "saved_data", filename_prefix: str = "synthetic_data"):
    """
    Save a DataFrame to a CSV file with a timestamped filename.
    """
    ensure_directory_exists(output_dir)  # Ensure the directory exists

    # Generate a timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"{output_dir}/{timestamp}_{filename_prefix}.csv"

    # Save the DataFrame to CSV
    df.to_csv(output_file, index=False)
    logger.info(f"Data saved to {output_file}")

    return output_file