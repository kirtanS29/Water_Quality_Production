# Water_Quality_Production
AICTE Eduskill internship

# 💧 Water Quality Pollutant Predictor

This project analyzes and predicts water pollution parameters using machine learning and Streamlit. It estimates key water pollutant levels like NH₄, BOD₅, NO₃, etc., and evaluates water safety against standard environmental thresholds.

---

## 🧠 Project Overview

This repository contains:

- A Jupyter Notebook (`.ipynb`) with full **data analysis**, **preprocessing**, **outlier removal**, and **model training**
- A **Streamlit app (`app.py`)** that predicts pollutant levels and provides safety insights
- Trained model files (not uploaded due to size constraints)

---

## 📌 Features

- Exploratory Data Analysis (EDA) with visualizations
- Outlier detection and removal to improve model quality
- One-hot encoding for categorical variables
- Voting Regressor using **Random Forest** and **Linear Regression**
- Pollution threshold logic for predicting **% of safe parameters**
- Streamlit app interface with endbar navigation (runs locally)

---

## 🗂 File Structure

```

├── app.py                    # Streamlit web app
├── WaterQualityPred\_week2.ipynb  # Jupyter Notebook with EDA + Model Training
├── model\_columns.pkl         # Feature columns used (small model metadata)
├── pollution\_model.pkl       # Trained model (not uploaded due to size)
└── README.md                 # Project overview and instructions

````

> Note: `pollution_model.pkl` is large and not included in the repo. You can generate it by running the notebook locally.

---

## 📊 Pollutants Tracked & Thresholds

| Pollutant     | Safe Limit     |
|---------------|----------------|
| NH₄ (Ammonium) | < 0.5 mg/L     |
| BSK5 (BOD₅)    | < 3.0 mg/L     |
| Suspended      | < 25 mg/L      |
| O₂ (Oxygen)    | > 5.0 mg/L     |
| NO₃ (Nitrate)  | < 10.0 mg/L    |
| NO₂ (Nitrite)  | < 0.1 mg/L     |
| SO₄ (Sulfate)  | < 250 mg/L     |
| PO₄ (Phosphate)| < 0.1 mg/L     |
| CL (Chloride)  | < 250 mg/L     |

---

## 🛠 How to Run Locally

1. **Clone the repository**
```bash
git clone https://github.com/your-username/water-quality-predictor.git
cd water-quality-predictor
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **(Optional) Run the Notebook**

```bash
jupyter notebook WaterQualityPred_week2.ipynb
```

4. **Run the Streamlit App**

```bash
streamlit run app.py
```

---

## 🚫 Not Deployed Yet

This app is currently not deployed online. You can run it locally via Streamlit. Due to size constraints, the trained model `.pkl` is not hosted — but can be generated from the notebook.

---

## 📜 License

This project is open-source under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author


* **KIRTAN SARAIYA**

---

## 📎 Acknowledgements

* CPCB India for water quality data
* Streamlit and scikit-learn for app and ML tools

```
# The google drivelink for pollution_model.pkl

*https://drive.google.com/file/d/1kKf21XG2QohQ5h6hI-ST7SCM6XP5vk0u/view?usp=drive_link


