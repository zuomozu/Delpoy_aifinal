from flask import Flask, request, render_template
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# Home page with file upload form
@app.route('/')
def home():
    return render_template('index.html')

# Handle file upload and analysis
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        data = pd.read_csv(file)

        # Example preprocessing: standardize features
        features = data.select_dtypes(include=['float64', 'int64']).columns
        if len(features) > 0:
            scaler = StandardScaler()
            data[features] = scaler.fit_transform(data[features])

        # Example analysis: PCA and RandomForestClassifier
        if len(features) > 0:
            pca = PCA(n_components=min(len(features), 2))
            pca_result = pca.fit_transform(data[features])
            data['PCA1'] = pca_result[:, 0]
            data['PCA2'] = pca_result[:, 1]

            # RandomForestClassifier example (assuming binary classification)
            if len(data['target'].unique()) == 2:
                X = data[features]
                y = data['target']
                clf = RandomForestClassifier()
                clf.fit(X, y)
                feature_importances = clf.feature_importances_
                importance_df = pd.DataFrame({
                    'Feature': features,
                    'Importance': feature_importances
                }).sort_values(by='Importance', ascending=False)
                importance_html = importance_df.to_html()

            else:
                importance_html = "Target variable is not binary or not present."

        else:
            importance_html = "No numerical features to preprocess."

        # Generate a summary of the dataset
        summary = data.describe(include='all').to_html()
        return f"<h1>Data Summary</h1>{summary}<h1>Feature Importances</h1>{importance_html}"

if __name__ == '__main__':
    app.run(debug=True)
