# 🚀 Data Science Project 1: Advanced EDA & Feature Engineering

## 📌 Overview

This project is part of my internship at **DecodeLabs**, focusing on **Advanced Exploratory Data Analysis (EDA)** and **Feature Engineering**.

The primary objective is to transform raw, unstructured data into a **clean, optimized dataset ready for machine learning models**, ensuring high performance, minimal noise, and strong generalization.

---

## 🎯 Objectives

* Handle missing data using statistical and model-based techniques
* Detect and treat outliers effectively
* Engineer meaningful features to improve predictive power
* Reduce redundancy using correlation analysis and PCA
* Build a robust preprocessing pipeline to avoid data leakage

---

## 🧠 Key Concepts Applied

* Data Cleaning & Preprocessing
* Feature Engineering
* Outlier Detection & Treatment
* One-Hot Encoding
* Scaling & Normalization
* Dimensionality Reduction (PCA)
* Pipeline Design (Scikit-learn)
* Data Leakage Prevention

---

## 📊 Dataset Description

The dataset represents transactional data with features such as:

* Product details
* Quantity & pricing
* Payment methods
* Order status
* Customer behavior indicators

---

## 🔧 Data Preprocessing Steps

### 1. Data Cleaning

* Removed irrelevant columns (IDs, tracking info, addresses)
* Handled missing values using:

  * Median Imputation
  * KNN Imputation (for numerical features)

---

### 2. Feature Engineering

Created meaningful features:

* **Year, Month, DayOfWeek** (from Date)
* **CouponUsed** (binary feature)
* **CartValue** (UnitPrice × ItemsInCart)

Removed redundant features:

* TotalPrice (derived)
* BulkBuyer, IsWeekend (highly correlated)

---

### 3. Outlier Handling

* Visualized using boxplots
* Handled using **RobustScaler** (no aggressive deletion)

---

### 4. Encoding

* Applied **One-Hot Encoding** to all categorical variables
* Handled unseen categories safely (`handle_unknown='ignore'`)

---

### 5. Feature Scaling

* Used **RobustScaler** for numerical features
* Ensures resistance to outliers

---

### 6. Dimensionality Reduction

* Applied **PCA (Principal Component Analysis)**
* Retained **90% variance**
* Reduced noise and improved generalization

---

## 🏗️ Pipeline Architecture

A complete **Scikit-learn Pipeline** was implemented:

* Numeric Pipeline:

  * KNN Imputer / Median Imputer
  * RobustScaler

* Categorical Pipeline:

  * Mode Imputation
  * OneHotEncoder

* Final Step:

  * PCA

👉 This ensures:

* No data leakage
* Consistent transformations
* Reusability on new data

---

## 📈 Exploratory Data Analysis

### 🔹 Correlation Heatmap

* Identified feature relationships
* Removed multicollinearity

### 🔹 Boxplots

* Analyzed outliers
* Confirmed natural distributions

### 🔹 PCA Curve

* Determined optimal number of components
* Balanced bias-variance tradeoff

---

## 📁 Project Structure

```
Project-1/
│
├── data/
├── notebooks/
├── X_train_processed.pkl
├── X_test_processed.pkl
├── preprocessing_pipeline.pkl
├── README.md
```

---

## 💾 Saved Artifacts

* `X_train_processed.pkl` → Processed training data
* `X_test_processed.pkl` → Processed testing data
* `preprocessing_pipeline.pkl` → Full preprocessing pipeline

---

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Seaborn & Matplotlib
* Joblib

---

## 🚀 Future Work

* Model Training (Random Forest, XGBoost, Logistic Regression)
* Hyperparameter tuning using **Optuna**
* Performance optimization (ROC-AUC, F1-score)
* Deployment-ready pipeline

---

## 🧠 Key Learnings

* Importance of proper data preprocessing
* Avoiding data leakage using pipelines
* Trade-offs between feature engineering and overfitting
* Practical use of PCA for dimensionality reduction

---

## 📌 Conclusion

This project demonstrates how raw data can be transformed into a **high-quality, machine-learning-ready dataset** using structured preprocessing, feature engineering, and statistical reasoning.

It lays a strong foundation for building accurate and scalable machine learning models.

---

## 👨‍💻 Author

**Mritunjay Singh**
Data Science Intern @ DecodeLabs

---
