import re

def parse_gemini_response(response: str) -> list[dict]:
    """
    Parse Gemini's response into a list of dictionaries.
    """
    # Extract the content between triple backticks (if present)
    if "```" in response:
        response = re.search(r"```(.*?)```", response, re.DOTALL).group(1).strip()
    
    # Split into individual transaction records
    transactions = response.strip().split("\n\n")
    
    parsed_data = []
    for transaction in transactions:
        try:
            # Remove newlines and split into key-value pairs
            pairs = transaction.replace("\n", ", ").split(", ")
            
            # Parse into a dictionary
            data = {}
            for pair in pairs:
                if ": " not in pair:
                    continue
                key, value = pair.split(": ", 1)
                data[key.strip()] = value.strip()
            
            # Add to parsed data
            parsed_data.append(data)
        except Exception as e:
            print(f"Skipping invalid transaction: {e}")
    
    return parsed_data