import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import unittest
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource
import plotly.graph_objects as go



# ================================
# **1️⃣ Load Dataset Function**
# ================================
def load_data(file_path):
    """ Load the dataset from the given file path """
    return pd.read_csv(file_path)

# ================================
# **2️⃣ Preprocessing Function**
# ================================
def preprocess_data(data):
    """ Preprocess the data to select numeric columns """
    return data.select_dtypes(include=['number'])

# ================================
# **3️⃣ Unit Testing Class**
# ================================
class TestNanofluidDataset(unittest.TestCase):

    def setUp(self):
        """ This method runs before each test. It initializes variables. """
        self.file_path = r"E:\PYTHON\AI_Python_code_31stJan\Python_Project\dataset\nanofluid_heat_transfer_dataset.csv"
        self.data = load_data(self.file_path)  # Load the dataset once here
        self.numeric_data = preprocess_data(self.data)  # Preprocess numeric data

    def test_data_loading(self):
        """ Test if dataset is loaded properly """
        self.assertFalse(self.data.empty, "Dataset is empty!")

    def test_numeric_columns(self):
        """ Test if numeric columns exist """
        self.assertGreater(len(self.numeric_data.columns), 0, "No numeric columns found!")

    def test_missing_values(self):
        """ Check for missing values in dataset """
        missing_count = self.data.isnull().sum().sum()
        self.assertEqual(missing_count, 0, f"Dataset contains {missing_count} missing values!")

    def test_scatter_plot(self):
        """ Test if scatter plot for Flow Velocity vs Heat Transfer Coefficient can be generated """
        try:
            scatter = figure(title="Flow Velocity vs Heat Transfer Coefficient",
                             x_axis_label="Flow Velocity (m/s)",
                             y_axis_label="Heat Transfer Coefficient (W/m²K)",
                             width=800, height=500)
            source = ColumnDataSource(self.data)
            scatter.circle(x="Flow_Velocity (m/s)", y="Heat_Transfer_Coefficient (W/m²K)", 
                           source=source, size=8, color="navy", alpha=0.6)
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Scatter plot generation failed! Error: {e}")

# Run Unit Tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)

# ================================
# **4️⃣ HEATMAP - Feature Correlation**
# ================================
def plot_heatmap(numeric_data):
    """ Plot a heatmap for feature correlation """
    plt.figure(figsize=(10, 6))
    sns.heatmap(numeric_data.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Heatmap of Feature Correlations")
    plt.show()

# ================================
# **5️⃣ SCATTER PLOT (Bokeh)**
# ================================
def plot_scatter_bokeh(data):
    """ Plot a scatter plot for Flow Velocity vs Heat Transfer Coefficient using Bokeh """
    output_file("scatter_plot.html")
    scatter = figure(title="Flow Velocity vs Heat Transfer Coefficient",
                     x_axis_label="Flow Velocity (m/s)",
                     y_axis_label="Heat Transfer Coefficient (W/m²K)",
                     width=800, height=500)

    source = ColumnDataSource(data)
    scatter.circle(x="Flow_Velocity (m/s)", y="Heat_Transfer_Coefficient (W/m²K)", 
                   source=source, size=8, color="navy", alpha=0.6)

    show(scatter)

# ================================
# **6️⃣ HISTOGRAM - Thermal Conductivity**
# ================================
def plot_histogram(data):
    """ Plot a histogram for Thermal Conductivity """
    plt.figure(figsize=(8, 5))
    sns.histplot(data["Thermal_Conductivity (W/mK)"], bins=20, kde=True, color="blue")
    plt.xlabel("Thermal Conductivity (W/mK)")
    plt.ylabel("Frequency")
    plt.title("Distribution of Thermal Conductivity")
    plt.show()

# ================================
# **7️⃣ BAR PLOT - Heat Transfer Coefficient by Nanoparticle Type**
# ================================
def plot_bar(data):
    """ Plot a bar chart for Heat Transfer Coefficient by Nanoparticle Type """
    plt.figure(figsize=(10, 5))
    sns.barplot(x="Nanoparticle_Type", y="Heat_Transfer_Coefficient (W/m²K)", data=data, palette="viridis")
    plt.xticks(rotation=45)
    plt.xlabel("Nanoparticle Type")
    plt.ylabel("Heat Transfer Coefficient (W/m²K)")
    plt.title("Heat Transfer Coefficient by Nanoparticle Type")
    plt.show()

# ================================
# **8️⃣ BOXPLOT - Viscosity Across Nanoparticle Types**
# ================================
def plot_boxplot(data):
    """ Plot a box plot for Viscosity Across Nanoparticle Types """
    plt.figure(figsize=(10, 5))
    sns.boxplot(x="Nanoparticle_Type", y="Viscosity (Pa·s)", data=data, palette="coolwarm")
    plt.xticks(rotation=45)
    plt.xlabel("Nanoparticle Type")
    plt.ylabel("Viscosity (Pa·s)")
    plt.title("Viscosity Distribution Across Nanoparticle Types")
    plt.show()

def plot_3d_scatter_plot(data, x_feature, y_feature, z_feature):
    """ Plot a 3D scatter plot using Plotly """
    # Create a 3D scatter plot with Plotly
    fig = go.Figure(data=[go.Scatter3d(
        x=data[x_feature],
        y=data[y_feature],
        z=data[z_feature],
        mode='markers',
        marker=dict(
            size=5,
            color=data[z_feature],  # Color by the z_feature
            colorscale='Viridis',  # Color scale
            opacity=0.8
        )
    )])

    fig.update_layout(
        title=f'3D Scatter Plot: {x_feature} vs {y_feature} vs {z_feature}',
        scene=dict(
            xaxis_title=x_feature,
            yaxis_title=y_feature,
            zaxis_title=z_feature
        ),
        width=800,
        height=600
    )

    fig.show()

# ================================
# **Main Function to Execute All Plots**
# ================================
def main(file_path):
    """ Main function to load data, run tests, and generate visualizations """
    
    # Load and preprocess the data
    data = load_data(file_path)
    numeric_data = preprocess_data(data)
    
    # Run unit tests
    unittest.main(argv=[''], exit=False)

    # Generate all visualizations
    plot_heatmap(numeric_data)
    plot_scatter_bokeh(data)
    plot_histogram(data)
    plot_bar(data)
    plot_boxplot(data)
    plot_3d_scatter_plot(data, 'Flow_Velocity (m/s)', 'Heat_Transfer_Coefficient (W/m²K)', 'Viscosity (Pa·s)')
    
    print("✅ All visualizations generated successfully!")

# Execute main function
if __name__ == '__main__':
    file_path = r"E:\IU_MSc_AI_Courses_Slides\Semester 1.1\Python task_assignment\nanofluid_heat_transfer_dataset.csv"
    main(file_path)
