# Sensor Collocation Study

This repository contains code and datasets for a comprehensive sensor collocation study examining indoor air quality and environmental parameters across various controlled experiments.

## Overview

The project involves collecting and analyzing data from multiple sensors placed in indoor and outdoor environments to compare their performance and understanding air quality dynamics during various household activities and scenarios.

## Repository Structure

- **Data Processing**:
  - [`Data_downloading.ipynb`](Data_downloading.ipynb): Jupyter notebook for downloading and processing the dataset from Google Drive
  - Data will be stored in the `./data` directory

- **Visualization and Analysis**:
  - [`graphs.ipynb`](graphs.ipynb): Jupyter notebook for visualizing sensor data across different experiments and comparing readings from various sensors

- **Experiment Documentation**:
  - [`experiments.json`](experiments.json): JSON file containing the timing information for all experiments conducted during the study

## Experiments

The study includes a wide range of environmental experiments including:

| Experiment Type | Description | Number of Trials |
|----------------|-------------|-----------------|
| Door Operations | Opening to garden, hallway, both | 3 |
| Exercise | Rowing with closed/open door | 2 |
| Human Presence | Occupancy effects | 2 |
| Diffuser | Water and oil diffusion | 3 |
| Vehicle Emissions | Car running at 3m and 5m distances | 2 |
| Cooking | Gas burner operation with closed/open door | 2 |
| Combustion | Candle burning (regular/scented) | 4 |
| Cleaning | Vacuum cleaning | 1 |
| Environmental | Odor from neighbors, heating, air exchange | 6 |
| VOC Testing | Controlled VOC tube experiments | 6 |

## Dataset

The data collected includes:
- Temperature readings
- Humidity measurements
- PM2.5 and PM10 particulate matter
- CO2 and VOC levels
- Air flow velocity

## Getting Started

1. Clone the repository:

```git clone https://github.com/yourusername/collocation_study.git cd collocation_study```

2. Install required dependencies:

```pip install -r requirements.txt```

3. Download the dataset:
- Run the `Data_downloading.ipynb` notebook to fetch and organize the data files
- The data will be downloaded from Google Drive and stored in the `./data` directory

4. Explore and visualize experiments:
- Open the `graphs.ipynb` notebook
- Select an experiment from the available options
- Generate comparison charts for CO2 and PM10 measurements
- The charts show data from all sensors alongside the reference device


