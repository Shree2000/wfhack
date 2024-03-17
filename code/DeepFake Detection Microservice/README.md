This file focuses on building a deep learning model for classifying audio files as either genuine (bonafide) or manipulated (spoof). The objective is to detect audio deepfakes, which are manipulated audio recordings designed to impersonate a genuine audio source. Our solution is a way to augment deepfake detection datasets using Autoencoders.

We have used two models for deep fake detection and created custom model out of it.

## Deepfake Auoencoder (Model 1)
### Model Architecture
 1. Gathered audio samples from the internet, preprocessed them into a suitable format, and extracted features. Split the dataset into training and testing sets.
 2. Designed an autoencoder that encodes audio features into a lower-dimensional representation and then decodes them to reconstruct the original features.
 3. Trained the bottleneck autoencoder using genuine voice samples from the training set, optimizing parameters to minimize the reconstruction error.
 4. Applied the trained autoencoder to both genuine and suspected deepfake voice samples from the testing set and calculateed the reconstruction error for each sample.
 5. Then we set a threshold for the reconstruction error. Samples with errors above this threshold are flagged as potential deepfakes.
 6. Evaluated the model's performance using accuracy as the parameter. The accuracy came out to be ~96%.

### Process flow of used autoencoder.
![image](https://github.com/Hackathon2024-March/sherlocked/assets/72347511/7929179b-62bc-4424-ad27-09639e5106f1)

### Results

![image](https://github.com/Hackathon2024-March/sherlocked/assets/72347511/a6c28eaf-4733-4e6d-940e-4df0b79b51eb)

## Deepfake CNN (Model 2)
This model aims to detect deep fake audio using a Convolutional Neural Network (CNN) model. 

The dataset used for training and evaluation should consist of genuine audio samples and deep fake audio samples. Ensure a balanced distribution of classes for better training performance.

### Flow Diagram 

![image](https://github.com/Hackathon2024-March/sherlocked/assets/72347511/b365178e-a9ae-4c42-994b-e88fe75106de)

### CNN Model 

![image](https://github.com/Hackathon2024-March/sherlocked/assets/48963206/24bc4805-f923-43db-80fd-076e9efb96a9)

### Results

![image](https://github.com/Hackathon2024-March/sherlocked/assets/48963206/e52e58c0-a662-4c23-a35c-8309626e9a36)

![image](https://github.com/Hackathon2024-March/sherlocked/assets/48963206/0ef34414-d66a-4efa-957b-e4e5b1c91002)



