This file focuses on building a deep learning model for classifying audio files as either genuine (bonafide) or manipulated (spoof). The objective is to detect audio deepfakes, which are manipulated audio recordings designed to impersonate a genuine audio source. Our solution is a way to augment deepfake detection datasets using Autoencoders.

*Model Architecture*
 1. Gathered audio samples from the internet, preprocessed them into a suitable format, and extracted features. Split the dataset into training and testing sets.
 2. Designed an autoencoder that encodes audio features into a lower-dimensional representation and then decodes them to reconstruct the original features.
 3. Trained the bottleneck autoencoder using genuine voice samples from the training set, optimizing parameters to minimize the reconstruction error.
 4. Applied the trained autoencoder to both genuine and suspected deepfake voice samples from the testing set and calculateed the reconstruction error for each sample.
 5. Then we set a threshold for the reconstruction error. Samples with errors above this threshold are flagged as potential deepfakes.
 6. Evaluated the model's performance using accuracy as the parameter. The accuracy came out to be ~96%.

Below diagram shows the process flow of used autoencoder.
![image](https://github.com/Hackathon2024-March/sherlocked/assets/72347511/7929179b-62bc-4424-ad27-09639e5106f1)

Result from the above model.

![image](https://github.com/Hackathon2024-March/sherlocked/assets/72347511/a6c28eaf-4733-4e6d-940e-4df0b79b51eb)

