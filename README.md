# 🏠 House Price Prediction

A machine learning web app that predicts house prices in Bengaluru based on location, area, bedrooms, bathrooms, and balconies.

## 🔗 Live Demo
[Try the app here](https://house-price-prediction-ay.streamlit.app/)

## 📊 Project Overview
This project uses the **Bengaluru House Price Dataset** (13,320 listings from Kaggle) to build a regression model that estimates house prices in Lakhs (₹). It covers the full ML pipeline — data cleaning, feature engineering, model training, and deployment.

## 🧹 Data Cleaning & Feature Engineering
- Removed the `society` column (41% missing values)
- Extracted `bhk` (bedroom count) from the messy `size` text column
- Converted `total_sqft` ranges (e.g. "2100-2850") into their average
- Removed unrealistic listings (e.g. very low sqft per bedroom)
- Removed price-per-sqft outliers within each location group
- One-hot encoded `location` into 240 binary columns

## 🤖 Model Training
Two models were trained and compared:

| Model | R² Score | MAE | RMSE |
|---|---|---|---|
| Linear Regression | 0.778 | 19.44 | 43.18 |
| Random Forest | 0.685 | 17.82 | 51.39 |

**Linear Regression was chosen** as the final model — it performed better on this high-dimensional, sparse (one-hot encoded) dataset and is easier to interpret.

## 🛠️ Tech Stack
- Python, Pandas, NumPy
- Scikit-learn (Linear Regression, Random Forest)
- Streamlit (deployment)
- Matplotlib/Seaborn (EDA)

## 📁 Project Structure