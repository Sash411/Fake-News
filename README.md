# Fake News Prediction App

This is a web application that uses machine learning to predict whether a news article is fake or real. It is built with Python and Flask framework.

## Installation

1. Clone the repository: `git clone https://github.com/Sash411/Fake-News.git`
2. Navigate to the project directory: `cd Fake-News`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - For Windows: `venv\Scripts\activate`
   - For Linux/Mac: `source venv/bin/activate`
5. Install the required dependencies: `pip install -r requirements.txt`

## Usage

1. Start the Flask development server: `flask run`
2. Open your web browser and go to `http://localhost:5000`
3. You should see the home page of the application.
4. Enter the news article text in the provided input field.
5. Click the "Predict" button to get the prediction result.
6. The app will display whether the news is "Fake" or "Real" based on the machine learning model's prediction.

## Model Training

If you want to train your own machine learning model:

1. Prepare your training data by collecting a dataset of labeled fake and real news articles.
2. Update the dataset path in the `train_model.py` script.
3. Run the `train_model.py` script: `python train_model.py`
4. The script will train a machine learning model using the provided dataset.
5. The trained model will be saved as a file for later use in the Flask app.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License].
