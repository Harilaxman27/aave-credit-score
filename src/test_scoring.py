import json
from src.feature_engineering import extract_features
from src.scoring_model import score_all_wallets

# Load data
with open("data/user_transactions.json", "r") as f:
    data = json.load(f)

# Feature extraction
features = extract_features(data)

# Scoring
wallet_scores = score_all_wallets(features)

# Show sample
for i, (wallet, score) in enumerate(wallet_scores.items()):
    print(f"{wallet} => Credit Score: {score}")
    if i >= 9:
        break
