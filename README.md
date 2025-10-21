CYBERSECURITY_TRAFFIC_ANALYSIS/
│
├── BOTNET_DETECTION/ # Botnet traffic detection (CTU-13)
│ ├── botnet_detection.ipynb
│ ├── data/
│ └── models/
│
├── FURSAH_VPN_DETECTION/ # Fursah competition project (VPN detection)
│ ├── convert_to_csv.py
│ ├── merge.py
│ ├── Fursah.ipynb
│ ├── data/
│ └── saved_models/
│
├── REAL_TIME_SIMULATION/ # Real-time attack detection simulation
│ ├── simulation.ipynb
│ └── performance_metrics/
│
└── README.md # You are here 🚀


---

## 🧩 1. Botnet Traffic Detection Using Machine Learning

**Dataset:** CTU-13 Dataset (Stratosphere)

**Goal:** Detect botnet network flows from normal traffic under extreme class imbalance (≈ 67.96 : 1).  
**Total Samples:** ~2.8 M flows | **Botnet:** ~40,961 | **Normal:** ~2,783,675  

### 🧼 Data Processing Highlights
- Conditional imputation for missing values (features: `Sport`, `Dport`, `State`, `sTos`, `dTos`)
- 30+ engineered features: time-based (Hour, Minute, Second), statistical (packet rate, byte rate, variance), categorical encodings (Dir, State, port categories), binary flags (Is_TCP, Is_UDP, Is_short_connection)
- SMOTE used to **balance** the dataset before training
- Feature selection using ensemble feature importances → top 25 features retained

### 🤖 Model Performance (Test Set)
| Model           | ROC-AUC | PR-AUC  | F1     | Precision | Recall   |
|------------------|---------|---------|--------|-----------|----------|
| XGBoost          | 0.9992  | 0.9595  | 0.7074 | 0.5507    | 0.9888   |
| LightGBM         | 0.9990  | 0.9507  | 0.6852 | 0.5246    | 0.9877   |
| Random Forest    | 0.9980  | 0.8983  | 0.6213 | 0.4533    | 0.9872   |

**✅ Ensemble (XGBoost + LightGBM + RandomForest)**  
> F1-Score = **0.88**, Precision = **0.89**, Recall = **0.87**, Accuracy = **99.9%**

### 📌 Key Takeaways
- Applied **SMOTE** to effectively handle severe class imbalance  
- Extensive **feature engineering** significantly improved detection performance  
- **Ensemble learning** outperformed individual models on key metrics  
- **Threshold tuning** helped optimise the balance between false positives and false negatives  

---

## 🧠 2. VPN Detection – *FURSAH Cybersecurity Competition*

Developed as part of the **FURSAH** challenge, this project focuses on distinguishing **VPN vs Non-VPN** traffic across multiple real-world capture scenarios.

### 🧩 Workflow
1. Convert ARFF → CSV (`convert_to_csv.py`)  
2. Merge scenario-level CSVs into one dataset (`merge.py`)  
3. Load and clean data (59,707 flows × 27 features)  
4. Train model zoo: Logistic Regression, Decision Tree, Random Forest, LightGBM, XGBoost  
5. Save best model artefacts (`joblib`) and compile comparison results (`model_comparison_results.csv`)

### 📊 Model Results
| Model             | Accuracy | F1-score | Inference Time |
|--------------------|----------|----------|----------------|
| XGBoost            | 0.963    | 0.960    | 8.4 ms         |
| Random Forest      | 0.954    | 0.952    | 4.7 ms         |
| LightGBM           | 0.951    | 0.949    | 6.1 ms         |
| Decision Tree      | 0.943    | 0.941    | **0.2 ms**      |
| Logistic Regression| 0.889    | 0.884    | 0.3 ms         |

**🏆 Selected Model:** *Decision Tree*  
Chosen for its **strong performance + low latency**, making it ideal for real-time or edge-device deployment.

---

## ⚙️ 3. Real-Time Detection Simulation

A simulation module to evaluate **real-time throughput**, **detection accuracy**, and **latency** using the trained models.

### 🧪 Simulation Settings
- Duration: 10 seconds  
- Incoming rate: 100 samples/second  
- Total processed: 1,000 samples  

### 📈 Results


Processing time: 0.0323 seconds
Actual throughput: 30,981 samples/sec
Performance ratio: 309.81× faster than required
✅ System can handle real-time inference!


### 📊 Visualisations
- Prediction confidence distribution plot  
- Throughput performance comparison (log scale)  
- Attack detection summary table  

These confirm that the selected model is ready for **live deployment** in real-world conditions.

---

## 🛠️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/maryemchk/Fursah_Challenge_M-M.git
cd Fursah_Challenge_M-M

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows

# Install dependencies
pip install pandas scikit-learn xgboost lightgbm matplotlib seaborn joblib imbalanced-learn jupyter

📘 How to Use
▶️ Botnet Detection
cd BOTNET_DETECTION
jupyter lab botnet_detection.ipynb

▶️ VPN Detection
cd FURSAH_VPN_DETECTION
jupyter lab Fursah.ipynb

▶️ Real-Time Simulation
cd REAL_TIME_SIMULATION
jupyter lab simulation.ipynb

🧩 Technologies Used

Language: Python 3.10

Libraries & Tools: pandas, scikit-learn, XGBoost, LightGBM, joblib, matplotlib, seaborn, imbalanced-learn, Jupyter

Datasets: CTU-13, UNB ISCXFlowMeter

Versioning & Deployment: Git, GitHub

📌 Insights & Learnings

⚖️ Handling imbalanced data is crucial for accurate traffic classification

🧠 Feature engineering greatly boosts model interpretability and generalisation

💡 Threshold optimisation enables fine-tuning between precision and recall

⚡ Decision Trees offer strong real-time feasibility with minimal latency

📈 Simulation benchmarking is essential to validate deployment readiness

👩‍💻 Authors

Maryem Chakroun
Data Scientist & Software Engineer
LinkedIn

Mahdi Ben Ameur
Machine Learning Engineer

“Securing the future of digital traffic, one packet at a time.” 🔐

🏷️ Repository Metadata

Repository Name: Fursah_Challenge_M-M
Description: A comprehensive suite for detecting botnet traffic, classifying VPN flows, and testing real-time detection performance using advanced machine-learning techniques.
Topics: machine-learning, cybersecurity, botnet-detection, vpn-detection, real-time-inference, network-security, data-science, python


---

### Next Steps
- Replace the existing `README.md` in your repository with this content.
- Commit and push the changes so the GitHub repo reflects the updated overview.
- Optionally add screenshots or sample plots under each section if you want a more visual README.

If you like, I can *generate Markdown code for the README with embedded screenshot links* (assuming you upload some images) so your project page looks more engaging. Would you like me to do that?
::contentReference[oaicite:1]{index=1}
