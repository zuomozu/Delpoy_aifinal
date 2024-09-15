
#  Data Analysis Flask Application

## Overview

This Flask application allows users to upload CSV files for basic data analysis. The application performs data preprocessing, Principal Component Analysis (PCA), and a feature importance analysis using a Random Forest Classifier. The results are then displayed as HTML.

## Features

- **File Upload:** Users can upload a CSV file from their local system.
- **Data Preprocessing:** Standardizes numerical features for consistent scaling.
- **PCA Analysis:** Reduces dimensionality to 2 components for visualization.
- **Feature Importance:** Computes and displays feature importance using a Random Forest Classifier (for binary classification).
- **Data Summary:** Provides a summary of the dataset including statistical descriptions of all features.

## Prerequisites

Ensure you have Docker installed on your machine. This application uses Docker to containerize the Flask app.

## Getting Started

### Building the Docker Image

1. Clone this repository or download the source code.
2. Navigate to the directory containing the Dockerfile.
3. Build the Docker image:

   ```bash
   docker build -t data-analysis-app .
   ```

### Running the Docker Container

1. Run the Docker container from the image:

   ```bash
   docker run -p 5000:5000 data-analysis-app
   ```

2. Open your web browser and go to `http://localhost:5000` to access the application.

### Usage

1. **Home Page:** Visit the home page to upload a CSV file.
2. **Upload File:** Use the file upload form to select and upload your CSV file.
3. **Analysis Results:** Once uploaded, the application processes the file and displays:
   - A summary of the dataset.
   - PCA components (if numerical features are present).
   - Feature importances (if the target variable is binary).

## Code Overview

- **Dockerfile:** Defines the Docker image for the application, installs dependencies, and sets up the environment.
- **app.py:** Main Flask application file containing routes for handling file uploads and performing data analysis.
- **requirements.txt:** Specifies the Python packages required for the application.

## Dependencies

- Flask
- pandas
- scikit-learn

Make sure to install the required packages by running:

```bash
pip install -r requirements.txt
```

