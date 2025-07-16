import json
import csv
import matplotlib.pyplot as plt

def save_scores_json(scores, filepath="outputs/wallet_scores.json"):
    with open(filepath, "w") as f:
        json.dump(scores, f, indent=2)

def save_scores_csv(scores, filepath="outputs/wallet_scores.csv"):
    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Wallet", "Score"])
        for wallet, score in scores.items():
            writer.writerow([wallet, score])

def plot_score_distribution(scores):
    score_values = list(scores.values())
    bins = list(range(0, 1100, 100))  # 0–1000 in 100 steps

    plt.hist(score_values, bins=bins, edgecolor="black")
    plt.title("Wallet Credit Score Distribution")
    plt.xlabel("Score Range")
    plt.ylabel("Number of Wallets")
    plt.xticks(bins)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.savefig("outputs/score_distribution.png")
    plt.show()
