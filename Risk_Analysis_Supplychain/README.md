# Supply Chain Risk Analysis

## Project Overview

This project analyzes **global supply chain shipment data** to identify the key factors associated with shipment disruptions.

The analysis focuses on operational, environmental, geopolitical, and carrier-related factors such as:

* Weather conditions
* Geopolitical risk
* Carrier reliability
* Lead time
* Transport mode
* Distance
* Shipment weight
* Fuel price
* Product category

The goal is to identify **high-risk shipment conditions** and generate insights that can help organizations understand and manage supply chain disruption risk.

---

## Dataset

The dataset contains **5,000 shipment records** and **14 columns**, covering shipments from **2024 to 2025**.

### Key Columns

| Column                      | Description                             |
| --------------------------- | --------------------------------------- |
| `Shipment_ID`               | Unique identifier for each shipment     |
| `Date`                      | Shipment date                           |
| `Origin_Port`               | Shipment origin port                    |
| `Destination_Port`          | Shipment destination port               |
| `Transport_Mode`            | Air, Rail, Road, or Sea                 |
| `Product_Category`          | Type of product being transported       |
| `Distance_km`               | Shipment distance in kilometers         |
| `Weight_MT`                 | Shipment weight in metric tons          |
| `Fuel_Price_Index`          | Fuel price index                        |
| `Geopolitical_Risk_Score`   | Geopolitical risk score                 |
| `Weather_Condition`         | Weather condition during shipment       |
| `Carrier_Reliability_Score` | Carrier reliability score               |
| `Lead_Time_Days`            | Shipment lead time                      |
| `Disruption_Occurred`       | Indicates whether a disruption occurred |

---

## Tools & Technologies

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Seaborn**
* **Jupyter Notebook**

---

## Analysis Performed

### 1. Data Understanding

* Loaded and inspected the dataset
* Checked dataset dimensions and data types
* Examined categorical and numerical variables
* Checked unique shipment IDs
* Converted and analyzed date information
* Analyzed the distribution of shipments across 2024 and 2025

### 2. Data Quality Checks

Performed checks for:

* Missing values
* Duplicate records
* Duplicate shipment IDs
* Data types
* Date validity
* Unique categorical values

The dataset had **no missing values**, and shipment IDs were unique.

### 3. Descriptive Statistics

Analyzed:

* Minimum and maximum values
* Mean and median
* Quartiles
* Distribution of numerical variables

This was performed for factors such as:

* Distance
* Weight
* Fuel price
* Geopolitical risk
* Carrier reliability
* Lead time

### 4. Outlier Analysis

The **IQR method** was used to identify potential outliers.

The most significant finding was in `Lead_Time_Days`.

* Upper IQR threshold: **49.85 days**
* **518 shipments** were above this threshold

Instead of automatically removing these records, they were investigated because unusually long lead times may represent genuine supply chain disruptions.

### 5. Lead Time & Disruption Analysis

Among the 518 unusually long lead-time shipments:

* **96.72% experienced a disruption**
* **3.28% did not experience a disruption**

This indicates that unusually long lead times can be an important **warning signal for supply chain disruption**.

### 6. Individual Risk Factor Analysis

Disruption rates were compared across different risk factors.

#### Weather

| Weather   | Disruption Rate |
| --------- | --------------: |
| Clear     |          36.98% |
| Rain      |          41.97% |
| Fog       |          48.07% |
| Storm     |          79.54% |
| Hurricane |         100.00% |

Weather showed one of the strongest relationships with disruption.

#### Geopolitical Risk

| Risk Level | Disruption Rate |
| ---------- | --------------: |
| Low        |          45.28% |
| Mid-Low    |          58.83% |
| Mid-High   |          65.58% |
| High       |          74.46% |

Disruption rates increased as geopolitical risk increased.

#### Carrier Reliability

| Reliability Level | Disruption Rate |
| ----------------- | --------------: |
| Low               |          65.30% |
| Mid-Low           |          65.08% |
| Mid-High          |          58.96% |
| High              |          55.72% |

Higher carrier reliability was generally associated with lower disruption rates.

---

## Combined Risk Analysis

To understand interactions between risk factors, heatmaps were created.

### Geopolitical Risk × Weather

The analysis showed that higher geopolitical risk amplified weather-related disruption.

For example, storm-related disruption increased from approximately **59.92% at low geopolitical risk** to **95.75% at high geopolitical risk**.

Hurricanes resulted in **100% disruption across all geopolitical risk levels**.

### Carrier Reliability × Weather

Carrier reliability also influenced disruption rates.

Higher carrier reliability generally reduced disruption rates for conditions such as:

* Clear weather
* Fog
* Rain
* Storm

However, hurricanes resulted in **100% disruption regardless of carrier reliability**, suggesting that extreme weather conditions can overwhelm the benefits of carrier reliability.

### Lead Time × Weather

A heatmap was also used to compare lead-time ranges with weather conditions.

The analysis showed particularly high disruption rates for:

* Hurricanes
* Storms
* Longer lead-time ranges

---

## Key Findings

The analysis identified several important patterns:

1. **Weather is a major disruption driver.**

   * Hurricanes had a 100% disruption rate.
   * Storms had a disruption rate of approximately 79.54%.

2. **Higher geopolitical risk is associated with higher disruption.**

   * Disruption increased from 45.28% under low geopolitical risk to 74.46% under high risk.

3. **Extreme weather can dominate other risk factors.**

   * Hurricane shipments experienced 100% disruption across geopolitical risk and carrier reliability ranges.

4. **Carrier reliability matters.**

   * Higher carrier reliability was associated with lower disruption rates.

5. **Unusually long lead times are a strong warning signal.**

   * 96.72% of the identified lead-time outliers were associated with disruptions.

6. **Transport mode had relatively similar disruption rates.**

   * Air, Rail, Road, and Sea were all around 61%, indicating limited differentiation between modes in this dataset.

7. **Distance, weight, fuel price, and product category showed relatively smaller differences** in disruption rates compared with weather, geopolitical risk, carrier reliability, and lead time.

---

## Business Insights

The findings suggest that supply chain teams could prioritize:

* Monitoring severe weather conditions
* Tracking geopolitical risk in high-risk regions
* Monitoring unusually long lead times
* Evaluating carrier reliability
* Combining multiple risk indicators rather than evaluating them independently

A shipment with **high geopolitical risk + severe weather + low carrier reliability + unusually long lead time** could be treated as a higher-priority shipment for monitoring.

---

## Project Structure

```text
Supply-Chain-Risk-Analysis/
│
├── Exploratory_analysis(3).ipynb
├── global_supply_chain_risk_2026.csv
└── README.md
```

---

## Project Workflow

```text
Data Collection
      ↓
Data Understanding
      ↓
Data Quality Checks
      ↓
Descriptive Statistics
      ↓
Outlier Detection
      ↓
Disruption Rate Analysis
      ↓
Risk Range Analysis
      ↓
Heatmap Analysis
      ↓
Combined Risk Analysis
      ↓
Business Insights
```

---

## Conclusion

This project demonstrates how **Python and Pandas can be used to explore supply chain data, identify risk patterns, investigate outliers, and translate analytical findings into business insights**.

The analysis found that **weather severity, geopolitical risk, carrier reliability, and unusually long lead times** were more informative for understanding disruption risk than factors such as distance, weight, fuel price, transport mode, and product category.

---

## Author

**Anuradha Nagarajan**

Data Analytics | SQL | Excel | Python & Pandas | Data Quality & Reporting
