The dataset for speech emotion detection was compiled by aggregating four publicly available datasets, each containing live audio recordings from individuals. These datasets include the CREMA (Crowd-sourced Emotional Multimodal Actors), SAVEE (Surrey Audio-Visual Expressed Emotion), RAVDESS (Ryerson Audio-Visual Database of Emotional Speech and Song), and TESS (Toronto Emotional Speech Set) datasets.

![image](https://github.com/Hackathon2024-March/sherlocked/assets/72347511/8186a52c-b189-4a2f-b838-16f8b320fb24)

Using the collected dataset, audio samples are preprocessed into suitable feature representations such as Mel-frequency cepstral coefficients (MFCCs) and spectrograms. These audio features were extracted using the librosa library. Subsequently, the Long Short-Term Memory (LSTM) model was deployed for analysis.  The LSTM architecture consists of sequential input data fed into one or more LSTM layers, followed by optional dropout layers for regularization. Dense (fully connected) layers are utilized for classification, culminating in an output layer with softmax activation for emotion prediction. Training involves optimizing the model parameters using categorical cross-entropy loss and a chosen optimizer.  This model achieved an impressive accuracy rate of approximately 91% in identifying and classifying the emotional content within the speech data.

Below is the flow diagram of the used model.

![image](https://github.com/Hackathon2024-March/sherlocked/assets/72347511/ab7391d6-9280-4b03-8a5c-28d70adce41b)

Results:- 

![image](https://github.com/Hackathon2024-March/sherlocked/assets/72347511/3a62497a-7598-4adf-bcff-f30e92c9f895)

![image](https://github.com/Hackathon2024-March/sherlocked/assets/72347511/143a667a-88a6-4ff4-ab05-586b101bfc2a)

