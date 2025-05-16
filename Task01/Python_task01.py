import pandas as pd
import matplotlib.pyplot as plt
import unittest
from sqlalchemy import create_engine
from bokeh.plotting import figure, show, output_file

class DataHandler:
    """Handles loading and processing of datasets."""
    def __init__(self, ideal_file, train_file):
        self.ideal_df = pd.read_csv(ideal_file)
        self.train_df = pd.read_csv(train_file)
    
    def get_best_fit_functions(self):
        """Selects four ideal functions that best fit the training data using Least-Square criterion."""
        best_fit = {}
        for col in self.train_df.columns[1:]:
            deviations = {ideal_col: ((self.train_df[col] - self.ideal_df[ideal_col])**2).sum() for ideal_col in self.ideal_df.columns[1:]}
            best_fit[col] = min(deviations, key=deviations.get)
        print("Best fit functions:", best_fit)  # Debugging
        return best_fit
    
    def validate_test_data(self, test_file, best_fit):
        """Validates test data by checking deviations against sqrt(2) times max deviation of training set."""
        test_df = pd.read_csv(test_file)
        results = []
        for _, row in test_df.iterrows():
            x_val = row["x"]
            y_val = row["y"]
            if x_val not in self.ideal_df["x"].values:
                continue  # Skip if x-value not in ideal dataset
            for train_col, ideal_col in best_fit.items():
                max_dev = abs(self.train_df[train_col] - self.ideal_df[ideal_col]).max()
                ideal_y_values = self.ideal_df.loc[self.ideal_df["x"] == x_val, ideal_col]
                if not ideal_y_values.empty:
                    ideal_y = ideal_y_values.values[0]
                    deviation = abs(y_val - ideal_y)
                    if deviation <= max_dev * (2**0.5):
                        results.append((x_val, y_val, ideal_col, deviation))
        print("Validated test data (first 10 results):", results[:10])  # Debugging - show first 10 results
        return results

# Visualization with Bokeh
def plot_data(df, title, filename):
    output_file(filename)
    p = figure(title=title, x_axis_label='x', y_axis_label='y')
    for col in df.columns[1:5]:
        p.line(df['x'], df[col], legend_label=col, line_width=2)
    show(p)

def plot_best_fit(best_fit, train_df, ideal_df):
    output_file("best_fit.html")
    p = figure(title="Best Fit Functions", x_axis_label='x', y_axis_label='y')
    for train_col, ideal_col in best_fit.items():
        p.scatter(train_df['x'], train_df[train_col], legend_label=f"Train: {train_col}", color="blue")
        p.line(ideal_df['x'], ideal_df[ideal_col], legend_label=f"Ideal: {ideal_col}", line_width=2, color="red")
    show(p)

# Unit Testing
class TestDatasetIntegrity(unittest.TestCase):
    def test_no_missing_values(self):
        """Check if there are any missing values in both datasets."""
        self.assertFalse(data_handler.ideal_df.isnull().values.any(), "ideal.csv contains missing values")
        self.assertFalse(data_handler.train_df.isnull().values.any(), "train.csv contains missing values")

    def test_correct_data_types(self):
        """Ensure all columns are numeric."""
        self.assertTrue(data_handler.ideal_df.dtypes.apply(lambda x: x.kind in 'if').all(), "ideal.csv has non-numeric values")
        self.assertTrue(data_handler.train_df.dtypes.apply(lambda x: x.kind in 'if').all(), "train.csv has non-numeric values")

    def test_x_value_ranges(self):
        """Ensure x values are within expected range."""
        self.assertGreaterEqual(data_handler.ideal_df["x"].min(), -20, "ideal.csv x values out of expected range")
        self.assertLessEqual(data_handler.ideal_df["x"].max(), 20, "ideal.csv x values out of expected range")
        self.assertGreaterEqual(data_handler.train_df["x"].min(), -20, "train.csv x values out of expected range")
        self.assertLessEqual(data_handler.train_df["x"].max(), 20, "train.csv x values out of expected range")

# Initialize and Run
if __name__ == "__main__":
    data_handler = DataHandler(r"E:\PYTHON\AI_Python_code_31stJan\ideal.csv", r"E:\PYTHON\AI_Python_code_31stJan\Python_Project\dataset\train.csv")
    best_fit = data_handler.get_best_fit_functions()
    plot_data(data_handler.ideal_df, "Ideal Functions", "ideal_functions.html")
    plot_data(data_handler.train_df, "Training Data", "training_data.html")
    plot_best_fit(best_fit, data_handler.train_df, data_handler.ideal_df)
    unittest.main()
