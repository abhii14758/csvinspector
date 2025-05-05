# 📊 CSV Data Profiling Report

**File Analyzed**: `preprocessed_data.csv`
**Generated On**: 2025-05-05 16:31:45

## 📌 Basic Info
- Rows: 2820
- Columns: 5

## 🧬 Feature Types
```
Date: Text
Simulated_SoilMoisture: Numerical
Simulated_discharge: Numerical
WRF: Numerical
Obs_discharge: Numerical
```

## 📈 Quantile Summary (first 5 columns)
|                        |   count |         mean |           std |         min |          25% |
|:-----------------------|--------:|-------------:|--------------:|------------:|-------------:|
| Simulated_SoilMoisture |    2820 |     0.124172 |     0.0406978 |   0.0531209 |    0.0894851 |
| Simulated_discharge    |    2820 | 13476.3      | 22421.2       | 996.902     | 1773.71      |
| WRF                    |    2820 |     2.71964  |     3.96836   |   0         |    0.137766  |
| Obs_discharge          |    2820 |  6047.21     | 10329         | 457.15      |  850.263     |

## 🚫 Missing Data
|                        |   Missing Count |   Missing % |
|:-----------------------|----------------:|------------:|
| Date                   |               0 |           0 |
| Simulated_SoilMoisture |               0 |           0 |
| Simulated_discharge    |               0 |           0 |
| WRF                    |               0 |           0 |
| Obs_discharge          |               0 |           0 |

## 🔗 Correlation Matrix (first 5 rows)
|                        |   Simulated_SoilMoisture |   Simulated_discharge |      WRF |   Obs_discharge |
|:-----------------------|-------------------------:|----------------------:|---------:|----------------:|
| Simulated_SoilMoisture |                 1        |              0.720926 | 0.613215 |        0.653395 |
| Simulated_discharge    |                 0.720926 |              1        | 0.609045 |        0.861754 |
| WRF                    |                 0.613215 |              0.609045 | 1        |        0.490133 |
| Obs_discharge          |                 0.653395 |              0.861754 | 0.490133 |        1        |

## 🧪 Outlier Summary
|                        |   count |   percent |
|:-----------------------|--------:|----------:|
| Simulated_discharge    |     380 |  13.4752  |
| Obs_discharge          |     348 |  12.3404  |
| WRF                    |     251 |   8.90071 |
| Simulated_SoilMoisture |       0 |   0       |

## 📊 Sample Distributions (Before)
![Distributions](distribution_before_outlier_removal.png)

## 📉 Correlation Heatmap
![Correlation Heatmap](correlation_heatmap.png)

## 🕳️ Missing Data Heatmap
![Missing Data Heatmap](missing_data_heatmap.png)

## 🔄 Skewness and Suggested Transformations
| Feature | Skewness | Suggested Transformation |
|:--------|----------:|:-------------------------|
| Obs_discharge | 3.09 | log1p |
| Simulated_discharge | 2.66 | log1p |
| WRF | 2.12 | sqrt |

## 🪄 Normalization Summary
### StandardScaler
|                        |   count |         mean |     std |       min |       25% |        50% |       75% |     max |
|:-----------------------|--------:|-------------:|--------:|----------:|----------:|-----------:|----------:|--------:|
| Simulated_SoilMoisture |    2820 | -6.04717e-17 | 1.00018 | -1.74613  | -0.852458 | -0.0949661 | 0.79397   | 2.13385 |
| Simulated_discharge    |    2820 | -7.55897e-18 | 1.00018 | -0.556685 | -0.522033 | -0.480121  | 0.0594802 | 6.67784 |
| WRF                    |    2820 | -3.52752e-17 | 1.00018 | -0.685452 | -0.650729 | -0.449139  | 0.23778   | 5.87689 |
| Obs_discharge          |    2820 |  1.25983e-17 | 1.00018 | -0.541296 | -0.50323  | -0.449172  | 0.0547379 | 8.41011 |
### MinMaxScaler
|                        |   count |      mean |      std |   min |        25% |       50% |       75% |   max |
|:-----------------------|--------:|----------:|---------:|------:|-----------:|----------:|----------:|------:|
| Simulated_SoilMoisture |    2820 | 0.450036  | 0.257779 |     0 | 0.23033    | 0.42556   | 0.654669  |     1 |
| Simulated_discharge    |    2820 | 0.0769484 | 0.138251 |     0 | 0.00478986 | 0.0105832 | 0.0851702 |     1 |
| WRF                    |    2820 | 0.104452  | 0.152412 |     0 | 0.00529116 | 0.0360105 | 0.140686  |     1 |
| Obs_discharge          |    2820 | 0.0604705 | 0.111734 |     0 | 0.00425249 | 0.0102915 | 0.0665855 |     1 |
## 🧠 Advanced Feature Suggestions
| Feature | Description |
|---------|-------------|
| 🔄 Skewness Fix | Identify and suggest log/sqrt transformations for skewed data |
| 🧮 Feature Engineering | Generate interaction terms, polynomial features (optional) |
| 🪄 Auto Normalization | StandardScaler or MinMaxScaler summaries |
| 📊 PCA Visualization | Optional: PCA plot for numeric data |
| 💡 Insights | Flag features with very high correlation or constant values |
| ✅ Data Quality Score | Rate datasets (e.g., based on missing % and outlier % ) |

