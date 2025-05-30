# FURSAH — VPN Detection & Traffic-Type Classification  
*Author: Mahdi Ben Ameur*  

---

## 1 . Project goal
This repository contains the **end-to-end pipeline** I built for the Fursah cybersecurity competition.  
The objective is to learn a model that distinguishes **VPN** from **non-VPN** network traffic (and act as a first step toward a broader traffic-source classifier).

---

## 2 . Repository layout
```bash
FURSAH_CODE/
│
├── data/ # Raw datasets
│ ├── Scenario A1-ARFF/ # ⇣ exported by UNB ISCXFlowMeter
│ ├── Scenario A2-ARFF/ # ⇢ each “Scenario X” ≈ one capture session
│ └── Scenario B-ARFF/
│
├── saved_models/ # Persisted artefacts (Joblib)
│ ├── decision_tree_model.joblib
│ ├── lightgbm_model.joblib
│ ├── logistic_regression_model.joblib
│ ├── random_forest_model.joblib
│ ├── xgboost_model.joblib
│ ├── model_metadata.joblib # feature list, preprocessing details, etc.
│ └── model_comparison_results.csv
│
├── convert_to_csv.py # ARFF ➜ CSV converter
├── merge.py # Merges per-scenario CSVs → data.csv
├── data.csv # 59 707 flows × 27 features (after merge)
├── Fursah.ipynb # Notebook: EDA + training + evaluation
├── .gitignore # ignores venv & temp artefacts
└── fursah_venv/ # local virtual-env (not committed)

```



---

## 3 . Data pipeline

| Step | Script / Notebook cell | What happens |
|------|------------------------|--------------|
| 1    | `convert_to_csv.py`    | Each **ARFF** file (output of ISCXFlowMeter) is parsed and saved as a tidy CSV. |
| 2    | `merge.py`             | All scenario-level CSVs are concatenated → **`data.csv`**. An extra column `scenario_id` is added so you can stratify by capture session if needed. |
| 3    | `Fursah.ipynb` – Section **1 & 2** | Loads `data.csv`, performs cleaning, derives a **binary label** `is_vpn`, handles missing values, and casts everything to `float32` for lighter models. |
| 4    | Notebook – Section **3** | Exploratory analysis: descriptive stats, distribution plots, correlation heat-map. |
| 5    | Notebook – Section **4** | Feature/target split. |
| 6    | Notebook – Section **5** | **Model zoo** (LogReg, Decision Tree, Random Forest, LightGBM, XGBoost).  |
| 7    | Notebook – Section **6** | Metrics gathered (Accuracy, Precision, Recall, F1, Inference time) ➜ saved to `model_comparison_results.csv`; best model’s artefact + metadata dumped to `saved_models/`. |
| 8    | Notebook – Section **7** | *How-to-reload* snippet that demonstrates loading the chosen model and its expected feature list in a production script. |

---

## 4 . How to reproduce

```bash
# 1. Clone 🌿
git clone https://github.com/<YOUR_USERNAME>/Fursah_VPN_detection.git
cd Fursah_VPN_detection/FURSAH_CODE

# 2. Create / activate virtual-env
python -m venv fursah_venv
source fursah_venv/bin/activate   # or .\fursah_venv\Scripts\activate on Windows

# 3. Install deps
pip install -r requirements.txt   # if provided
# OR, minimally:
pip install pandas scikit-learn xgboost lightgbm matplotlib seaborn joblib

# 4. Re-build dataset (optional — the repo already ships data.csv)
python convert_to_csv.py
python merge.py

# 5. Open notebook
jupyter lab Fursah.ipynb
```
## 5 . Results
```

Model	Accuracy	F1-score	Inference (ms/flow)
XGBoost	0.963	0.960	8.4 ms
Random Forest	0.954	0.952	4.7 ms
LightGBM	0.951	0.949	6.1 ms
Decision Tree	0.943	0.941	0.2 ms
Logistic Regression	0.889	0.884	0.3 ms
```


## 6 . Conclusion
Although XGBoost edges out the others on raw accuracy/F1, the margin over a plain Decision Tree is < 2 %.
Given the competition’s real-time inference constraint (edge devices, limited CPU budget), the Decision Tree offers the best performance-to-latency trade-off and is therefore selected as the production model.

