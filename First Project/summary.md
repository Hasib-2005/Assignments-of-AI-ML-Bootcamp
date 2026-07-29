# California Housing Price Prediction — Executive Project Summary

**Author:** Mohammad Hasibur Rahman  
**Dataset:** 1990 California Census Dataset (20,640 records)  
**Task:** Continuous Regression Modeling for Housing Valuation  

---

### 1. Technical Approach & Pipeline
To predict neighborhood median house values, I designed a structured five-stage data science pipeline:
1. **Exploratory Analysis (EDA)**: I examined distributions and correlation matrices across features. Spatial visual plotting revealed clear geographic price clusters along coastal California regions.
2. **Data Cleaning & Feature Engineering**: Missing values in `total_bedrooms` (207 rows) were imputed using median values to preserve distributional stability against extreme outliers. Three aggregate ratio features were generated to capture density metrics per household: `rooms_per_household`, `bedrooms_per_room`, and `population_per_household`.
3. **Encoding & Scaling**: Categorical variables (`ocean_proximity`) were converted via one-hot encoding, and numerical attributes were standard-scaled for linear modeling.
4. **Modeling & Evaluation**: I partitioned the dataset (80/20 train-test split) and trained both a baseline Linear Regression model and an ensemble Random Forest Regressor (100 estimators). Models were evaluated using MAE, RMSE, and $R^2$ metrics.

---

### 2. Best Model & Empirical Performance
The **Random Forest Regressor** demonstrated superior predictive performance across all evaluation metrics, significantly outperforming the baseline Linear Regression model.

| Model Metric | Linear Regression (Baseline) | Random Forest Regressor (Best) |
| :--- | :--- | :--- |
| **Mean Absolute Error (MAE)** | $49,645.51 | **$31,928.15** |
| **Root Mean Squared Error (RMSE)** | $69,126.81 | **$49,837.92** |
| **Variance Explained ($R^2$)** | 0.6353 | **0.8105** |

The Random Forest model accounts for **81.05%** of variance in house prices across the test set, reducing typical prediction errors by nearly **$19,288** compared to linear baseline estimation.

---

### 3. Key Limitations & Future Improvements
* **Target Variable Capping at $500,000**: A notable constraint in this dataset is the upper boundary artificial cap at $500,001 on `median_house_value`. This ceiling forces the model to underestimate high-value property tiers.
* **Proposed Solution**: Given additional time, I would isolate capped target instances into a secondary classification problem or apply truncated regression models (such as Tobit regression) specifically designed to handle artificial ceiling constraints. Furthermore, incorporating geographic spatial clustering algorithms (e.g., K-Means on coordinates) would better capture localized micro-market pricing trends.