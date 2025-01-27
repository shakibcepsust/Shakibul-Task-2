
# Resource Management in Catalytic Conversion for Biofuel Production

### Data Analysis Project
#### 2025 Resource Management Analysis Assignment

GitHub repository at:
[Repository Link](https://github.com/your-username/resource-management-biofuel.git)

- Python script: **resource_management.py**
- Dataset: **extra_3.csv**

---

## Table of Contents
1. [Introduction](#introduction)
2. [Dataset Description](#dataset-description)
3. [Analysis and Visualization Steps](#analysis-and-visualization-steps)
    1. [Data Import and Preprocessing](#data-import-and-preprocessing)
    2. [Resource Utilization Calculation](#resource-utilization-calculation)
    3. [Efficiency Analysis](#efficiency-analysis)
    4. [Visualization](#visualization)
4. [Technologies Used](#technologies-used)
5. [How to Run](#how-to-run)

---

## Introduction
This project analyzes resource management in the catalytic conversion process for biofuel production. By evaluating the usage of catalysts, energy, and raw materials, the program calculates production efficiency and visualizes key trends to aid decision-making in sustainable biofuel production.

---

## Dataset Description
The dataset includes details about resource usage and biofuel production, such as:
- **Catalyst Usage (kg)**: Quantity of catalysts used in each production run.
- **Energy Consumption (kWh)**: Energy used for the catalytic conversion process.
- **Raw Material Input (kg)**: Raw materials used for biofuel production.
- **Biofuel Yield (L)**: Volume of biofuel produced in liters.
- **Production Run**: Identifies individual production processes.

---

## Analysis and Visualization Steps

### Data Import and Preprocessing
1. Import the dataset from a CSV file into a pandas DataFrame.
2. Standardize column names by removing extra spaces and replacing them with underscores.
3. Clean the dataset by handling missing or inconsistent values.

### Resource Utilization Calculation
1. Calculate the total resource input for each production run:
   $$
   \text{Total Resource Input} = \text{Catalyst Usage} + \text{Energy Consumption} + \text{Raw Material Input}
   $$
2. Compute the biofuel yield for each run.

### Efficiency Analysis
- Calculate resource efficiency for each run:
  $$
  \text{Resource Efficiency} = \frac{\text{Biofuel Yield}}{\text{Total Resource Input}}
  $$

### Visualization
1. **Bar Chart**: Compare the usage of catalysts, energy, and raw materials for each production run.
2. **Scatter Plot**: Show the relationship between total resource input and biofuel yield.

---

## Technologies Used
- **Python**: Programming language for analysis and visualization.
- **Pandas**: Data manipulation and preprocessing.
- **Matplotlib**: Library for creating visualizations.

---

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/shakibcepsust/Shakibul-Task-2
   ```
2. Navigate to the project directory:
   ```bash
   cd Shakibul-Task-task_2
   ```
3. Ensure the dataset `extra_3.csv` is present in the project directory.
4. Run the Python script:
   ```bash
   python task_2.py
   ```

---