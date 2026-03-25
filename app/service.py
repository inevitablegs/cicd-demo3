from app.calculator import divide
import logging

logger = logging.getLogger(__name__)

def process_data(data):
    results = []

    for item in data:
        value = divide(item["value"], item["divider"])  # ❌ crash if divider = 0
        results.append(value)

    return sum(results) / len(results)  # ❌ crash if results empty
