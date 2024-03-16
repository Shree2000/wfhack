import librosa
from tensorflow.keras.models import Sequential, model_from_json

from pydub import AudioSegment, effects
import numpy as np

def preprocess_audio(path):
    _, sr = librosa.load(path)
    # raw_audio = AudioSegment.from_file(path)
    
    samples = np.array(_, dtype=np.float32)
    trimmed, _ = librosa.effects.trim(samples, top_db=25)
    
    padded = np.pad(trimmed, (0, 180000-len(trimmed)), 'constant')
    return padded, sr

emotion_dic = {
    0:'neutral',
    1   : 'happy',
    2:'sad'     , 
    3:'angry', 
    4: 'fear', 
    5: 'disgust'
}

def encode(label):
    return emotion_dic.get(label)

def loadModel():
    json_file = open('F:\Hackathon_2024\Server Integration Models\Server Microservice_with3 models working\Models\CNN_model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("F:\Hackathon_2024\Server Integration Models\Server Microservice_with3 models working\Models\CNN_model_.weights.h5")
    print("Loaded model from disk")
    return loaded_model


def predict(path1):
    zcr_list = []
    rms_list = []
    mfccs_list = []
    emotion_list = []

    FRAME_LENGTH = 2048
    HOP_LENGTH = 512
    
    y, sr = preprocess_audio(path1)
    # print("hey")
    # return
    zcr = librosa.feature.zero_crossing_rate(y, frame_length=FRAME_LENGTH, hop_length=HOP_LENGTH)
    rms = librosa.feature.rms(y=y, frame_length=FRAME_LENGTH, hop_length=HOP_LENGTH)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13, hop_length=HOP_LENGTH)

    zcr_list.append(zcr)
    rms_list.append(rms)
    mfccs_list.append(mfccs)
    X = np.concatenate((
        np.swapaxes(zcr_list, 1, 2), 
        np.swapaxes(rms_list, 1, 2), 
        np.swapaxes(mfccs_list, 1, 2)), 
        axis=2
    )
    X = X.astype('float32')
    model=loadModel()
    y_pred = np.argmax(model.predict(X), axis=1)
    return emotion_dic.get(y_pred[0])



