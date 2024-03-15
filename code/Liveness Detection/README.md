This Liveliness detection for voice samples helps in identifying whether the voice is recorded or not and hence helps in speaker verification and fraud prevention It implements a Support Vector Machine (SVM) machine learning model for determining the authenticity of voice recordings. The SVM model is trained on a dataset consisting of both genuine and spoofed voice samples and it creates the best line or decision boundary that segregates n-dimensional space into classes. This best decision boundary is called a hyperplane. 
SVM chooses the extreme points/vectors that help in creating the hyperplane.

<img src="https://github.com/Hackathon2024-March/sherlocked/assets/72347511/28bb7967-a0ef-4a23-9f66-330e72e64b7e" alt="Image" width="400" height="200">




     +-------------------------------------+
     | Data preparation and preprocessing  |
     +--------+----------------------------+
                      |
                      v
           +--------------------+
           | Feature Extraction |
           +--------+-----------+
                      |
                      v
         +----------------------------+
         | Audio Liveliness Detection |
         +--------+-------------------+
                      |
                      v
               +-------------+
               | Prediction  |
               +------+------+
