from flask import Flask, render_template, request, Response
import os
from textSummarizer.pipeline.prediction import PredictionPipeline

app = Flask(__name__)

# Initialize your model's prediction pipeline
prediction_pipeline = PredictionPipeline()

# Route for the Homepage
@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')

# Route for Training the Model
@app.route('/train', methods=["GET"])
def train():
    try:
        # Assuming 'main.py' triggers the model training process
        os.system("python main.py")
        return Response("Training successful!", status=200)
    except Exception as e:
        return Response(f"Error during training: {e}", status=500)

# Route for Predicting (Summarization)
@app.route('/predict', methods=["POST"])
def predict():
    if request.method == "POST":
        input_text = request.form["inputText"]  # Text from the form
        
        try:
            # Use your local PredictionPipeline for summarization
            summary = prediction_pipeline.predict(input_text)  # No length parameters
            # Render the result on the same page
            return render_template('index.html', result=summary)
        except Exception as e:
            return render_template('index.html', result=f"Error: {e}")
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
