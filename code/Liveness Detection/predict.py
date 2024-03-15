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

def predict(audioFile):
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