 This file aims to develop a model for removing background noise intensity from audio recordings and subsequently detecting the presence of background noise. The model utilizes python library "noisereduce" to achieve accurate noise removal and detection. Noisereduce is a noise reduction algorithm in python that reduces noise in time-domain signals like speech, bioacoustics, and physiological signals. The process involves generating a spectrogram of the signal and determining a noise threshold for each frequency band within the signal.

Steps of the Noise Reduction algorithm
1. A spectrogram is calculated over the noise audio clip
2. Statistics are calculated over spectrogram of the the noise
3. A threshold is calculated based upon the statistics of the noise

If the intensity of denoised voice signal closely resembles the intensity of actual human speech, there's a higher likelihood that it is indeed a real human voice, as AI-generated voices typically lack background noise. 
              

![image](https://github.com/Hackathon2024-March/sherlocked/assets/72347511/ac165ead-88f5-4120-a852-5e5834b8ca81)



![image](https://github.com/Hackathon2024-March/sherlocked/assets/116094109/708f01f0-55f6-4ff9-8128-b02a19541d1e)





