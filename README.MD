# FoxxData

## Overview

This project generates synthetic transaction data using the **Google Gemini API**. The data is structured according to a predefined schema (`TransactionRecord`) and saved to a CSV file. The project is modular, with clear separation of concerns, making it easy to maintain, extend, and test.

---

## Directory Structure

```
FoxxData/
│
├── synthetic_data_generator/          # Main Python package
│   ├── __init__.py                    # Package initialization
│   ├── models/                        # Pydantic models
│   │   └── transaction.py             # TransactionRecord model
│   ├── prompts/                       # Prompt templates
│   │   └── templates.py               # FewShotPromptTemplate and PromptTemplate
│   ├── services/                      # Core services
│   │   ├── data_generator.py          # Synthetic data generation logic
│   │   ├── parser.py                  # Response parsing logic
│   │   └── file_handler.py            # File handling logic
│   ├── utils/                         # Utility functions
│   │   └── logger.py                  # Logging setup
│   ├── app.py                         # Application logic
│   └── main.py                        # Entry point for the application
│
├── tests/                             # Unit tests
│   └── test_data_generator.py         # Test cases for data generation
│
├── requirements.txt                   # Project dependencies
├── README.md                          # Project documentation
└── .env                               # Environment variables (e.g., API keys)
```

---

## Key Features

1. **Synthetic Data Generation**:

   - Uses the **Google Gemini API** to generate realistic transaction data.
   - Data is validated against a **Pydantic schema** (`TransactionRecord`).
2. **Modular Design**:

   - Clear separation of concerns (e.g., data generation, file handling, logging).
   - Easy to extend or modify individual components.
3. **File Handling**:

   - Automatically creates a `saved_data` directory if it doesn't exist.
   - Saves generated data to a **timestamped CSV file**.
4. **Logging**:

   - Centralized logging configuration for consistent logging across the application.
5. **Scalability**:

   - Designed to handle large-scale data generation with minimal changes.

---

## How It Works

### 1. **Data Generation**

- The `DataGenerator` class interacts with the **Gemini API** to generate synthetic transaction data.
- The generated data is validated against the `TransactionRecord` schema to ensure consistency.

### 2. **File Handling**

- The `file_handler.py` module ensures the output directory exists and saves the generated data to a CSV file with a **timestamped filename**.

### 3. **Logging**

- The `logger.py` module configures logging for the application, ensuring consistent log formatting and output.

### 4. **Execution**

- The `main.py` file serves as the entry point for the application. It calls the `run_application` function from `app.py`, which orchestrates the entire workflow.

---

## Code Files and Their Roles

### 1. **`main.py`**

- **Purpose**: Entry point for the application.
- **Role**: Calls the `run_application` function from `app.py`.

### 2. **`app.py`**

- **Purpose**: Contains the main application logic.
- **Role**:
  - Initializes the `DataGenerator`.
  - Generates synthetic data.
  - Saves the data to a CSV file using `file_handler.py`.

### 3. **`data_generator.py`**

- **Purpose**: Handles synthetic data generation.
- **Role**:
  - Interacts with the Gemini API.
  - Validates generated data using the `TransactionRecord` schema.

### 4. **`file_handler.py`**

- **Purpose**: Handles file-related operations.
- **Role**:
  - Ensures the output directory exists.
  - Saves generated data to a CSV file.

### 5. **`parser.py`**

- **Purpose**: Parses the response from the Gemini API.
- **Role**:
  - Extracts transaction data from the API response.
  - Converts the data into a list of dictionaries.

### 6. **`logger.py`**

- **Purpose**: Configures logging for the application.
- **Role**:
  - Sets up logging format and level.
  - Provides a logger instance for use across the application.

### 7. **`transaction.py`**

- **Purpose**: Defines the schema for transaction data.
- **Role**:
  - Uses **Pydantic** to validate the structure of generated data.

### 8. **`templates.py`**

- **Purpose**: Defines prompt templates for the Gemini API.
- **Role**:
  - Provides a structured prompt for generating synthetic data.

---

## Setup and Installation

### 1. **Clone the Repository**

```bash
git clone https://github.com/sayan-in-tech/foxxdata.git
cd foxxdata
```

### 2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

### 3. **Set Up Environment Variables**

- Create a `.env` file in the root directory:
  ```plaintext
  GOOGLE_API_KEY=your_google_api_key_here
  ```

### 4. **Run the Application**

```bash
python main.py
```

---

## Example Output

### Logs

```
2023-10-27 14:30:22 - app - INFO - Starting synthetic data generation...
2023-10-27 14:30:22 - file_handler - INFO - Created directory: saved_data
2023-10-27 14:30:25 - app - INFO - Generated 5 out of 5 requested transactions.
2023-10-27 14:30:25 - file_handler - INFO - Data saved to saved_data/synthetic_data_20231027_143022.csv
```

### CSV File (`synthetic_data_20231027_143022.csv`)

| transaction_id                       | customer_id | transaction_amount | transaction_date | payment_method | product_category | quantity | customer_age | customer_location | device_used | ip_address    | shipping_address            | billing_address             | is_fraudulent | account_age_days | transaction_hour |
| ------------------------------------ | ----------- | ------------------ | ---------------- | -------------- | ---------------- | -------- | ------------ | ----------------- | ----------- | ------------- | --------------------------- | --------------------------- | ------------- | ---------------- | ---------------- |
| 2b9d1c7a-f8e2-4b33-a911-0a4e5f66c7d8 | 542         | 2500.00            | 10/27/2024 03:17 | credit card    | electronics      | 1        | 42           | Anytown, USA      | desktop     | 91.202.234.56 | PO Box 123, Lagos, Nigeria  | 123 Main St, Anytown, USA   | 1             | 10               | 3                |
| e6f78a9b-c2d3-410e-95b4-1b2a3c4d5e6f | 101         | 99.99              | 10/27/2024 14:52 | debit card     | clothing         | 2        | 28           | Smallville, USA   | mobile      | 192.168.1.100 | 456 Elm St, Smallville, USA | 456 Elm St, Smallville, USA | 0             | 365              | 14               |

---

## Extending the Project

### 1. **Add New Data Fields**

- Update the `TransactionRecord` schema in `transaction.py`.
- Modify the prompt template in `templates.py` to include the new fields.

### 2. **Support Other File Formats**

- Extend `file_handler.py` to support saving data in formats like JSON or Excel.

### 3. **Add Unit Tests**

- Write unit tests for each module in the `tests/` directory.

### 4. **Enhance Error Handling**

- Add error handling for API requests, file operations, and data validation.

---

## Dependencies

- **Python 3.8+**
- **Pydantic**: Data validation and schema definition.
- **LangChain**: Integration with the Gemini API.
- **Pandas**: Data manipulation and CSV export.
- **python-dotenv**: Environment variable management.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---

## Contact

For questions or feedback, please contact:

- **Your Name**: sayan18012004@gmail.com
- **GitHub**: [sayan-in-tech](https://github.com/sayan-in-tech)
