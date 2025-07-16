import numpy as np

def score_wallet(features):
    """
    Input: feature dict for one wallet
    Output: credit score between 0–1000
    """

    score = 500  # Start from a base score

    # --- Positive Contributions ---
    if features['repay_to_borrow_ratio'] > 0.8:
        score += 150
    elif features['repay_to_borrow_ratio'] > 0.5:
        score += 75
    elif features['repay_to_borrow_ratio'] > 0:
        score += 30

    if features['deposit_to_borrow_ratio'] > 2:
        score += 100
    elif features['deposit_to_borrow_ratio'] > 1:
        score += 50

    if features['total_txns'] > 50:
        score += 80
    elif features['total_txns'] > 20:
        score += 40
    elif features['total_txns'] > 5:
        score += 20

    if features['unique_tokens'] >= 5:
        score += 50
    elif features['unique_tokens'] >= 2:
        score += 20

    if features['activity_span_days'] > 100:
        score += 50
    elif features['activity_span_days'] > 30:
        score += 20

    # --- Negative Deductions ---
    if features['num_liquidation'] > 0:
        score -= 150

    if features['total_borrowed_usd'] > 0 and features['repay_to_borrow_ratio'] < 0.1:
        score -= 100

    if features['total_deposited_usd'] > 0 and features['deposit_to_borrow_ratio'] < 0.5:
        score -= 50

    # Finalize score range
    return int(np.clip(score, 0, 1000))


def score_all_wallets(wallet_features: dict) -> dict:
    scored = {}
    for wallet, features in wallet_features.items():
        scored[wallet] = score_wallet(features)
    return scored
