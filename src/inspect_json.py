import json

# Load a small portion of the JSON file to examine
with open('data/user_transactions.json', 'r') as f:
    data = json.load(f)

# Check how many records we have
print(f"Total transactions: {len(data)}")

# Print one sample transaction
print("Sample record:\n", json.dumps(data[0], indent=2))
