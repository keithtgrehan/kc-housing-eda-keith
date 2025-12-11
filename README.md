# EDA Housing Project 1 – King County Housing Data

This repository contains my exploratory data analysis (EDA) of the King County housing dataset.  
The goal is to understand the drivers of house prices and to provide clear, non-technical recommendations for a fictional high-budget client.

---

## 📂 Repository Structure

project-root/
│
├── notebooks/
│   └── EDA_Housing_Project_1.ipynb      # Final cleaned analysis notebook
│
├── data/
│   └── kc_house_sales_joined.csv        # Source dataset (not uploaded if large)
│
├── slides/
│   └── housing-project-presentation.pdf # 10-minute client-facing slides
│
├── src/                                 # (Optional) scripts for cleaning functions
│
└── README.md                             # This document

---

## 🎯 Project Objectives

- Understand the structure and quality of the housing dataset  
- Explore key variables, distributions, and relationships  
- Test hypotheses related to size, renovation, grade, and geography  
- Translate technical findings into business-ready recommendations  
- Support a fictional client (“Jennifer Montgomery”) in making a high-value house purchase with resale potential

---

## 🧪 Methodology Summary

The final notebook follows a clean and reproducible EDA workflow:

1. **Understanding the Data**  
   Column types, missing values, basic structure.

2. **Hypotheses**  
   Price drivers (size, grade, renovation, ZIP code, waterfront).

3. **Explore**  
   Univariate and bivariate inspection, distributions, outliers.

4. **Cleaning**  
   - Dropped rows missing critical values  
   - Trimmed extreme outliers  
   - Added log-price variable

5. **Relationships**  
   Correlations, scatterplots, boxplots, ZIP code comparison.

6. **Back to Hypotheses**  
   Clear confirmation/refutation of each hypothesis.

7. **Fine Tune**  
   Cleaned visuals, consistent formatting, removed irrelevant steps.

8. **Explain**  
   Business-level recommendations for the client.

---

## 📊 Key Insights (High-Level)

- **Size and grade** are the strongest predictors of price.  
- **Renovated homes** command a meaningful premium.  
- **Waterfront properties** form a separate luxury tier.  
- A small cluster of **high-value ZIP codes** consistently outperforms the rest.  
- Strategic filtering is essential for resale potential within 12 months.

Full details and plots are in the notebook.

---

## 🖥️ Files to Review

### 🔍 **1. Final EDA Notebook**
`notebooks/EDA_Housing_Project_1.ipynb`  
Contains all analysis, figures, reasoning, and cleaned code.

### 🎤 **2. Presentation Slides (PDF)**
`slides/housing-project-presentation.pdf`  
A 10-minute client-friendly summary of problem → insights → recommendations.

### 🧰 **3. Optional Scripts**
Any reusable code (e.g., cleaning functions) lives in `src/`.

---

## 🚀 How to Run the Notebook

1. Clone the repo  
2. Install dependencies (if a requirements.txt exists)  
3. Open the notebook in Jupyter or VS Code  
4. Run all cells from top to bottom

Dataset must be placed in `data/`.

---

## 👤 Author

Keith Grehan  
AI Product Management Bootcamp – neuefische Berlin

---