# Nanofluid Heat Transfer Analysis

This repository contains Python scripts and visualizations for analyzing nanofluid heat transfer datasets. It includes data processing, visualization, and unit testing for two main tasks.

## Workspace Structure

```
CSV/
    ideal.csv
    train.csv
Task_01/
    Python_task01.py
    best_fit.html
    ideal_functions.html
    training_data.html
Task_02/
    Python_task_02.py
    scatter_plot.html
Task_02_seg_def/
    Task_02_seg_def.py
best_fit.html
ideal_functions.html
scatter_plot.html
training_data.html
```

## Setup Instructions

### 1. Clone the Repository

```sh
git clone <your-repo-url>
cd <your-repo-directory>
```

### 2. Create and Activate a Virtual Environment (Recommended)

```sh
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Required Packages

```sh
pip install pandas numpy matplotlib seaborn bokeh plotly sqlalchemy
```

## Data Files

Place the following CSV files in the `CSV/` directory:
- `ideal.csv`
- `train.csv`
- (For Task 02) `nanofluid_heat_transfer_dataset.csv` (update the path in scripts if needed)

## Running the Scripts

### Task 01

- **Script:** [`Task_01/Python_task01.py`](Task_01/Python_task01.py)
- **Description:** Loads `ideal.csv` and `train.csv`, finds best fit functions, generates Bokeh plots, and runs unit tests.
- **Run:**
  ```sh
  python Task_01/Python_task01.py
  ```
- **Outputs:** HTML plots in `Task_01/` and project root.

### Task 02

- **Script:** [`Task_02/Python_task_02.py`](Task_02/Python_task_02.py)
- **Description:** Loads and analyzes `nanofluid_heat_transfer_dataset.csv`, generates various plots, and runs unit tests.
- **Run:**
  ```sh
  python Task_02/Python_task_02.py
  ```
- **Outputs:** Plots such as `scatter_plot.html` in `Task_02/`.

### Task 02 (Segmented/Definitive)

- **Script:** [`Task_02_seg_def/Task_02_seg_def.py`](Task_02_seg_def/Task_02_seg_def.py)
- **Description:** Modular functions for loading, preprocessing, testing, and visualizing the nanofluid dataset.
- **Run:**
  ```sh
  python Task_02_seg_def/Task_02_seg_def.py
  ```
- **Outputs:** Plots displayed interactively.

## Notes

- Update file paths in scripts if your dataset locations differ.
- All scripts include unit tests for data integrity and plotting.
- Generated HTML plots can be opened in any web browser.

## Requirements

- Python 3.7+
- See `pip install` command above for required packages.

---

For any issues, please check file paths and ensure all dependencies are installed.