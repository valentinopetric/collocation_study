# Data Analysis

run read_data.ipynb and air_wings.ipynb to download and preprocess the data.
all analysis are in the notebooks folder.

## Notebooks

Each location was first analyzed individually. A correlation matrix was created at each site to check for potential correlations between pollutant levels and weather data as observed across various sensor readings. Events monitored included: **Doors Opened**, **Hall Opened**, **Indoor Room Air Exchange**, **Rowing (CD)**, **Rowing (OD)**, **Human Presence**, **Diffuser (Water)**, **Diffuser (Oil)**, **Car (3m)**, **Car (5m)**, **Gas Burner (CD)**, **Gas Burner (OD)**, and **Candle**.

For a detailed event analysis, the mean difference percentage was calculated for each event. This metric simulates the change in the target variable due to specific events. Additionally, a correlation matrix for these difference percentages was generated to examine potential correlations between changes induced by different events. 

### airwings

### indoors

![Correlation matrix for airwings indoor](images/air_wings_indoor/corr.png)



