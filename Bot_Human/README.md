# 🤖 Botnet Traffic Detection using Machine Learning

This project tackles the challenge of **botnet traffic detection** using the [CTU-13 dataset](https://www.stratosphereips.org/datasets-ctu13) and advanced machine learning techniques. The goal is to distinguish between **normal** and **botnet** traffic in a highly imbalanced environment.

---

## 📊 Dataset Overview

- **Dataset Size:** 2,824,636 network flow records  
- **Columns:** 15 original features including `StartTime`, `Dur`, `Proto`, `SrcAddr`, `Sport`, `Dir`, `DstAddr`, `Dport`, `State`, `TotPkts`, `TotBytes`, etc.  
- **Target:** `Label` (botnet vs. normal flow)

---

## 🔍 Problem Characteristics

- **Type:** Binary Classification (Normal vs. Botnet)  
- **Challenge:** Severe class imbalance (67.96:1)  
  - **Normal traffic:** 2,783,675 samples  
  - **Botnet traffic:** 40,961 samples

---

## 🧼 Data Preprocessing

### ✅ Missing Values

- Columns with missing values: `Sport`, `Dport`, `State`, `sTos`, `dTos`  
- Handled via conditional imputation and added flags for missingness.

### ✅ Feature Engineering

Created **30+ new features**, including:

- **Time-based:** Hour, Minute, Second  
- **Statistical:** Packet rate, Byte rate, Average packet size, Variance  
- **Categorical Transformations:** Encoded `Dir`, `State`, port categories  
- **Binary Flags:** Is_TCP, Is_UDP, Is_short_connection, etc.

### ✅ Feature Selection

- Selected **top 25 features** using feature importance from ensemble models.

---

## ⚖️ Class Imbalance Handling

- Used **SMOTE (Synthetic Minority Oversampling Technique)** to balance the dataset.  
- **Before SMOTE:**  
  - Normal: 2,226,939  
  - Botnet: 32,769  
- **After SMOTE:**  
  - Normal: 2,226,939  
  - Botnet: 2,226,939

---

## 🤖 Model Development

### Individual Classifiers

| Model               | ROC-AUC | PR-AUC | F1-Score | Precision | Recall |
|---------------------|---------|--------|----------|-----------|--------|
| XGBoost             | 0.9992  | 0.9595 | 0.7074   | 0.5507    | 0.9888 |
| LightGBM            | 0.9990  | 0.9507 | 0.6852   | 0.5246    | 0.9877 |
| Random Forest       | 0.9980  | 0.8983 | 0.6213   | 0.4533    | 0.9872 |
| Logistic Regression | 0.9742  | 0.3499 | 0.2432   | 0.1397    | 0.9369 |

### ✅ Ensemble Model

Averaged predictions from **XGBoost**, **LightGBM**, and **Random Forest**:

- **ROC-AUC:** 0.9990  
- **PR-AUC:** 0.9497  
- **F1-Score:** 0.6858  
- **Tuned threshold:**  
  - F1-Score = **0.88**  
  - Precision = **0.89**  
  - Recall = **0.87**

---

## 📈 Evaluation (on Test Set)

- **Accuracy:** 99.9%  
- **Botnet Class Performance:**  
  - Precision: **0.89**  
  - Recall: **0.87**  
  - F1-Score: **0.88**

---

## 📌 Key Takeaways

- Applied **SMOTE** to effectively handle severe class imbalance.
- Extensive **feature engineering** and selection significantly improved model accuracy.
- **Ensemble learning** outperformed individual models on key metrics.
- **Threshold tuning** helped optimize the balance between false positives and false negatives.

---

🧠 Author
Maryem Chakroun
