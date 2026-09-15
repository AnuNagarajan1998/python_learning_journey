
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

This was performed for fact
