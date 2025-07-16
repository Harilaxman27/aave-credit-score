import json
from src.feature_engineering import extract_features
from src.scoring_model import score_all_wallets
from src.save_and_plot import save_scores_json, save_scores_csv, plot_score_distribution

def main():
    # Load data
    with open("data/user_transactions.json") as f:
        data = json.load(f)

    # Process
    features = extract_features(data)
    scores = score_all_wallets(features)

    # Save
    save_scores_json(scores)
    save_scores_csv(scores)

    # Visualize
    plot_score_distribution(scores)

if __name__ == "__main__":
    main()
