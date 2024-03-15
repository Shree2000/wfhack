Liveliness detection for voice samples is crucial in various applications such as speaker verification, fraud prevention, and security systems. This project implements a Support Vector Machine (SVM) machine learning model for determining the authenticity of voice recordings. The SVM model is trained on a dataset consisting of both genuine and spoofed voice samples.

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
