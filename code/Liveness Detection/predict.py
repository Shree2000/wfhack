# Section 5.3
# Contains the extraction process of 4 features used in Void system
# feature extraction

# !pip install pydub

import numpy as np
import scipy.io.wavfile as wav
import scipy.signal as ssig
import scipy.stats as stats
from scipy.signal import find_peaks
import os
import matplotlib.pyplot as plt
import math
import librosa
import librosa
from sklearn import svm
from sklearn import svm
import pickle
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import NearestCentroid
from pydub import AudioSegment
from data_preparation import data_preparation

def convert_to_wav_if_needed(audio_data, file_format):
    """
    Convert audio data to WAV format if it's in MP3 format.

    Parameters:
    - audio_data: Audio data as bytes or as a buffer.
    - file_format: File format of the audio data.

    Returns:
    - wav_data: WAV audio data as bytes if conversion was done, else None.
    """
    # Convert audio data to PyDub AudioSegment
    audio = AudioSegment.from_file(audio_data, format=file_format)

    # Check if the file format is MP3
    if file_format.lower() == 'mp3':
        # Export to WAV format
        wav_data = audio.export(format="wav").read()
        return wav_data
    elif file_format.lower() == 'wav':
        # It's already in WAV format, no conversion needed
        return None
    else:
        # Unsupported file format, raise an error
        raise ValueError("Unsupported file format. Only MP3 and WAV are supported.")


def predict(audioFile, format):
    audioFile= convert_to_wav_if_needed(audioFile,format)
    x_eval=data_preparation(audioFile)
    # Load the the SVM classifier model:
    file_model = os.path.join(os.getcwd(),'models','svm.pkl')
    if os.path.isfile(file_model):
        # Load the extracted features and corresponding labels:
        with open(file_model, 'rb') as f:
            classifier=pickle.load(f)
    else:
        print('Model Not Found')

    # Prediction result of SVM classifier on EVALUATION set of ASVspoof 2017 v2 dataset:
    print("Results")
    result_pred = classifier.predict(x_eval)
    probabilities = classifier.predict_proba(x_eval)
    print("predicted result", result_pred)
    return probabilities

if __name__ == '__main__':
    audio_folder = os.path.join(os.getcwd(), 'audio')
    for file in os.listdir(audio_folder):
        # Check if the file has an audio extension
        if file.endswith('.wav') or file.endswith('.mp3') or file.endswith('.ogg'):
            filename = os.path.basename(file)
            file_path = os.path.join(audio_folder, file)
            
            # Determine the file format
            file_format = file.split('.')[-1]

            # Load the audio data
            with open(file_path, 'rb') as audio_file:
                audio_data = audio_file.read()

            # Call the predict function with the audio data and file format
            probability = predict(audio_data, file_format)

            print("Probability , fileName" , probability, filename)
