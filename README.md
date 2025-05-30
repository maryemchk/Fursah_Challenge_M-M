# Fursah_Bot_Traffic_Detection
🛡️ Botnet Traffic Detection in Network Flows
📌 Project Description
This project addresses the detection of botnet network traffic using a large dataset of network flow records. The dataset is highly imbalanced, with botnet flows making up only ~1.45% of total records. The goal is to develop a high-performance model capable of distinguishing normal from malicious (botnet) traffic.

📂 Dataset Overview
Total samples: 2,824,636

Features: 15 original, extended to 45 through feature engineering

Label: Multi-class labels reduced to binary (Normal, Botnet)

Imbalance ratio: ~68:1 (Normal to Botnet)

🔧 Key Steps & Decisions
✅ 1. Data Cleaning
Missing values found in Sport, Dport, sTos, dTos, and State.

Handled using:

Filling with "unknown" for categorical.

Filling with 0 or appropriate placeholder for numerical.

🧠 2. Feature Engineering
Added 30+ new features, including:

Time-based: Hour, Minute, Second

Traffic stats: Packet_rate, Byte_rate, Avg_packet_size, Bytes_ratio

Categorical grouping: Sport_category, Dport_category

Binary flags: Is_TCP, Is_UDP, Is_high_volume, etc.

📉 3. Feature Selection
Selected 25 most informative features using model-based feature importance (e.g., from XGBoost):

Top features: Dur, Packet_rate, Bytes_ratio, State, Dir, Avg_packet_size, etc.

⚖️ 4. Handling Class Imbalance
Used SMOTE (Synthetic Minority Oversampling Technique):

Original:
Normal: 2,226,939
Botnet: 32,769

After SMOTE:
Normal: 2,226,939
Botnet: 2,226,939

🤖 Models Trained
Model	ROC-AUC	PR-AUC	F1-Score	Precision	Recall
XGBoost	0.9992	0.9595	0.7074	0.5507	0.9888
LightGBM	0.9990	0.9507	0.6852	0.5246	0.9877
Random Forest	0.9980	0.8983	0.6213	0.4533	0.9872
Logistic Regression	0.9742	0.3499	0.2432	0.1397	0.9369
Ensemble (Best)	0.9990	0.9497	0.6858	0.5248	0.9896

The Ensemble Model (XGBoost + LightGBM + RF) was selected as the final model due to:

High Recall (0.9896) – essential in security tasks

Excellent Precision-Recall AUC

Balanced F1-score

🎯 Final Evaluation (with optimal threshold)
Class	Precision	Recall	F1-score
Normal	1.00	1.00	1.00
Botnet	0.89	0.87	0.88
Accuracy: 1.00	F1: 0.88		

📊 Visualizations Included
Feature importance

Class distribution

ROC and PR curves

Confusion matrices

🔍 Cross-Validation
5-fold CV confirms high consistency across folds.

ROC-AUC > 0.998 in all folds.

🏁 Conclusion
This project demonstrates an effective pipeline for detecting botnet traffic:

Advanced preprocessing

Balanced data via SMOTE

Robust modeling using ensemble methods

The system is capable of flagging botnet activities in real-time-like settings with high recall, critical for intrusion detection systems.

💡 Future Work
Deploy the model in a streaming framework (e.g., Kafka + Spark)

Integrate real-time alerting and visualization dashboard

Extend to multi-class botnet family classification
