# Wallet Credit Score Analysis

This analysis summarizes the results from processing 100,000 DeFi transactions from the Aave V2 protocol, and assigning a credit score (0–1000) to each wallet based on behavior patterns.

## 🔢 Score Distribution

| Score Range | Number of Wallets |
|-------------|-------------------|
| 0–100       | 0                 |
| 100–200     | 0                 |
| 200–300     | 0                 |
| 300–400     | ~20               |
| 400–500     | ~1700             |
| 500–600     | ~650              |
| 600–700     | ~220              |
| 700–800     | ~540              |
| 800–900     | ~300              |
| 900–1000    | ~100              |

> See: `outputs/score_distribution.png`

---

## 🧠 Behavior Analysis

### 🟠 Low-Scoring Wallets (400–500)
- Typically made 1–2 deposits or transactions
- Borrowed nothing or repaid nothing
- Little time activity (`activity_span_days` = 0–7)
- May represent one-time users, test wallets, or bots

### 🟡 Mid-Scoring Wallets (600–700)
- Moderate borrow/repay behavior
- Reasonable `repay_to_borrow_ratio` (> 0.5)
- Diverse token interactions (3+ tokens)
- Active for 1–3 months

### 🟢 High-Scoring Wallets (800+)
- Consistent interaction with protocol
- Repaid a large share of borrowed funds
- Good `deposit_to_borrow_ratio` (> 2.0)
- Interacted over a long duration (100+ days)
- Used 5+ unique tokens

---

## 📊 Observations

- Majority of users are either casual or passive participants
- Few power users show truly responsible behavior
- Scoring logic is sensitive to repayment behavior and duration of engagement
- Can be extended to reward liquidity providers or governance voters

---

## 🔁 Next Steps

- Add clustering to detect user types
- Analyze wallets involved in liquidation
- Extend features to cover profit/loss (PnL), flash loans, or arbitrage

