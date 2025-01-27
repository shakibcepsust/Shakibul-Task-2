import pandas as pd
import matplotlib.pyplot as plt

def main():
    """
    Main function to analyze resource management in catalytic conversion for biofuel production.

    This program imports data from a CSV file, preprocesses it to remove missing entries, 
    calculates resource utilization, and evaluates resource efficiency for each production run.
    Additionally, it visualizes resource usage and the relationship between resource input 
    and biofuel yield using bar and scatter plots.
    """

    # File path of the input data
    file_path = 'extra_3.csv'

    # Load and preprocess data
    data = load_and_preprocess_data(file_path)

    # Calculate total resource input and efficiency
    calculate_metrics(data)

    # Visualize resource usage and efficiency
    visualize_data(data)

def load_and_preprocess_data(file_path):
    """
    Load data from a CSV file and preprocess it.

    Args:
        file_path (str): Path to the input CSV file.

    Returns:
        pandas.DataFrame: Cleaned and preprocessed data.
    """
    # Load data into a DataFrame
    data = pd.read_csv(file_path)

    # Clean column names by stripping spaces and replacing spaces with underscores
    data.columns = [col.strip().replace(" ", "_") for col in data.columns]

    # Drop rows with missing values
    data = data.dropna()

    return data

def calculate_metrics(data):
    """
    Calculate resource utilization and efficiency metrics.

    Args:
        data (pandas.DataFrame): The input data containing resource usage and biofuel yield.

    Returns:
        None: Modifies the DataFrame in place by adding new columns.
    """
    # Calculate the total resource input for each production run
    data['Total_Resource_Input'] = (
        data['Catalyst_Usage_(kg)'] +
        data['Energy_Consumption_(kWh)'] +
        data['Raw_Material_Input_(kg)']
    )

    # Calculate resource efficiency as biofuel yield divided by total resource input
    data['Resource_Efficiency'] = data['Biofuel_Yield_(L)'] / data['Total_Resource_Input']

def visualize_data(data):
    """
    Generate visualizations for resource usage and efficiency.

    Args:
        data (pandas.DataFrame): The input data with calculated metrics.

    Returns:
        None: Displays bar and scatter plots.
    """
    # Create subplots for the visualizations
    fig, axes = plt.subplots(2, 1, figsize=(10, 12))

    # Bar chart for resource usage comparison
    data[['Catalyst_Usage_(kg)', 'Energy_Consumption_(kWh)', 'Raw_Material_Input_(kg)']].plot(
        kind='bar', ax=axes[0]
    )
    axes[0].set_title("Comparison of Resource Usage")
    axes[0].set_xlabel("Production Run")
    axes[0].set_ylabel("Resource Amount")
    axes[0].legend(["Catalyst", "Energy", "Raw Material"])

    # Scatter plot for total resource input vs biofuel yield
    data.plot.scatter(
        x='Total_Resource_Input',
        y='Biofuel_Yield_(L)',
        ax=axes[1],
        color='orange'
    )
    axes[1].set_title("Resource Input vs Biofuel Yield")
    axes[1].set_xlabel("Total Resource Input (kg/kWh)")
    axes[1].set_ylabel("Biofuel Yield (L)")

    # Adjust layout and display the plots
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
