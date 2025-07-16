# 🏦 Aave Wallet Credit Scoring Model (DeFi Risk Analysis)

This project assigns a **credit score (0–1000)** to wallets interacting with the Aave V2 protocol, based on their historical DeFi transaction behavior.

The score estimates how responsible or risky a wallet is, based on actions like deposit, borrow, repay, redeem, and liquidation.

---

## 📂 Project Structure

```plaintext
aave-credit-score/
├── data/                    # Raw input data
│   └── user_transactions.json
├── outputs/                 # Generated outputs
│   ├── wallet_scores.json
│   ├── wallet_scores.csv
│   └── score_distribution.png
├── src/                     # Source code
│   ├── __init__.py
│   ├── inspect_json.py
│   ├── feature_engineering.py
│   ├── scoring_model.py
│   ├── save_and_plot.py
│   ├── test_feature_engineering.py
│   └── test_scoring.py
├── analysis.md              # Behavioral analysis
├── requirements.txt         # Dependencies
└── README.md                # Project documentation
```
---

## ⚙️ How to Run

### 1️⃣ Install Requirements

pip install -r requirements.txt

### 2️⃣ Run Feature Extraction

python -m src.test_feature_engineering

### 3️⃣ Run Scoring Test

python -m src.test_scoring

### 4️⃣ Generate All Outputs (CSV, JSON, Plot)

python -m src.generate_outputs

---

## 🧠 Feature Engineering Logic

From the raw transaction logs, we extract wallet-specific metrics such as:

* Total number of transactions
* Amounts deposited, borrowed, and repaid (in USD)
* Repay-to-borrow and deposit-to-borrow ratios
* Number of unique tokens used
* Activity duration (days active)
* Average time between actions
* Number of liquidations

See: `src/feature_engineering.py`

---

## 📊 Credit Scoring Strategy

Wallets are scored based on behavioral features:

* ✅ Good repayment behavior → Higher score
* ✅ High deposit-to-borrow ratio → Higher score
* ✅ Long-term activity → Higher score
* ❌ Liquidations, low repayments → Lower score

Scoring logic is implemented in: `src/scoring_model.py`

---

## 📈 Results

* Over **3,400 wallets** processed and scored
* Score distribution chart saved to `outputs/score_distribution.png`
* Full behavioral and statistical analysis in `analysis.md`

---
---

## 🔮 Future Work

While the current system uses a rule-based scoring approach for transparency and interpretability, there are several directions to improve robustness and intelligence:

### 🚀 Model Improvements
- **Use supervised learning** (e.g., regression, gradient boosting) if labeled data becomes available
- **Apply unsupervised learning** (e.g., clustering) to detect wallet behavior patterns
- **Incorporate anomaly detection** for identifying flash loan attacks, bot-like behavior, or unusual spikes

### 🧠 Feature Enhancements
- Add **temporal behavior features** (e.g., seasonal activity, recent vs. old actions)
- Include **token volatility**, stablecoin preferences, or LP participation
- Track **interaction frequency with different pools or assets**

### 📊 Scoring Enhancements
- Weight actions using historical outcomes (e.g., penalize known exploit patterns)
- Benchmark against known good or malicious wallets
- Introduce **confidence scores** or **score justifications** for transparency

---

> This baseline rule-based scoring model offers interpretability and ease of audit — ideal for bootstrapping credit scoring in DeFi. Future versions can evolve toward more adaptive and data-driven solutions.

---
## 🙌 Credits

* Built for the **Aave Credit Scoring Internship Challenge**
* By: Salendra Harilaxman
* Date: **16th July 2025**

---
