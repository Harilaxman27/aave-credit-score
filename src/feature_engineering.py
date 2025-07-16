import json
from collections import defaultdict
from datetime import datetime
import numpy as np

def extract_features(transactions):
    wallets = defaultdict(list)

    # Group transactions by wallet
    for txn in transactions:
        wallet = txn.get("userWallet")
        if not wallet:
            continue
        wallets[wallet].append(txn)

    wallet_features = {}

    for wallet, txns in wallets.items():
        txns.sort(key=lambda x: x['timestamp'])  # Ensure ordered by time
        timestamps = [t['timestamp'] for t in txns]

        # Initialize counters and sums
        features = {
            'total_txns': len(txns),
            'num_deposit': 0,
            'num_borrow': 0,
            'num_repay': 0,
            'num_redeem': 0,
            'num_liquidation': 0,
            'total_deposited_usd': 0.0,
            'total_borrowed_usd': 0.0,
            'total_repaid_usd': 0.0,
            'tokens': set()
        }

        for txn in txns:
            action = txn.get('action', '').lower()
            data = txn.get('actionData', {})
            amount = float(data.get('amount', 0))
            price = float(data.get('assetPriceUSD', 0))
            symbol = data.get('assetSymbol', 'UNKNOWN')

            features['tokens'].add(symbol)

            usd_value = amount * price

            if action == 'deposit':
                features['num_deposit'] += 1
                features['total_deposited_usd'] += usd_value
            elif action == 'borrow':
                features['num_borrow'] += 1
                features['total_borrowed_usd'] += usd_value
            elif action == 'repay':
                features['num_repay'] += 1
                features['total_repaid_usd'] += usd_value
            elif action == 'redeemunderlying':
                features['num_redeem'] += 1
            elif action == 'liquidationcall':
                features['num_liquidation'] += 1

        # Derived metrics
        features['repay_to_borrow_ratio'] = (
            features['total_repaid_usd'] / features['total_borrowed_usd']
            if features['total_borrowed_usd'] > 0 else 0
        )
        features['deposit_to_borrow_ratio'] = (
            features['total_deposited_usd'] / features['total_borrowed_usd']
            if features['total_borrowed_usd'] > 0 else 0
        )
        features['unique_tokens'] = len(features['tokens'])
        features.pop('tokens')  # remove set, already converted

        # Time-based features
        if len(timestamps) >= 2:
            time_diffs = np.diff(sorted(timestamps))
            features['avg_time_between_txns'] = np.mean(time_diffs)
        else:
            features['avg_time_between_txns'] = 0

        features['activity_span_days'] = (
            (max(timestamps) - min(timestamps)) / (60 * 60 * 24)
            if len(timestamps) >= 2 else 0
        )

        wallet_features[wallet] = features

    return wallet_features
