import json
from src.feature_engineering import extract_features

def main():
    # Load the JSON data
    with open("data/user_transactions.json", "r") as f:
        transactions = json.load(f)

    # Extract features from transactions
    wallet_features = extract_features(transactions)

    # Print total wallets found
    print(f"Total wallets processed: {len(wallet_features)}\n")

    # Show features for the first 5 wallets
    for i, (wallet, features) in enumerate(wallet_features.items()):
        print(f"Wallet Address: {wallet}")
        for feature_name, value in features.items():
            print(f"  {feature_name}: {value}")
        print("-" * 40)
        if i >= 4:
            break

if __name__ == "__main__":
    main()
