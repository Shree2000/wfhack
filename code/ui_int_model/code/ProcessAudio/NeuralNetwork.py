from sklearn.externals import joblib
import os
import numpy as np
# Get the directory where the current Python script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

def process(audio_data):
    #Call different models with audio data and obtain their predictions
    model1_predictions = call_model1(audio_data)
    model2_predictions = call_model2(audio_data)
    #Add more model calls as needed

    # Combine predictions into a single feature vector
    combined_features = np.concatenate((model1_predictions, model2_predictions), axis=0)
    # Load another model
    neuralnet_model = joblib.load(os.path.join(script_directory,"models", "neuralnet_model.pkl"))

    # Use the combined features as input to the loaded model
    final_predictions = neuralnet_model.predict(combined_features)

    return final_predictions