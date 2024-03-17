# Identity Impersonation Detection
Design document

## Development team:

1. Gulshan Kumar - Software Engineer (DTI)
2. Shivesh Dixit - Software Engineer (EFT)
3. Shreerang Bhatt - Software Engineer (EFT)
4. Srivatsh Agarwal - Software Engineer (CCIBT)

## Brief description of the project:
The primary objective of this project is to develop effective countermeasures against identity personification using AI-generated voice prints. This project seeks to address the growing threat of voice-based fraud and protect individuals and organizations from unauthorized access and impersonation. 

## Analyzing audio signals

![image](https://github.com/Hackathon2024-March/sherlocked/assets/72347511/8186a52c-b189-4a2f-b838-16f8b320fb24)

## Requirements of the project:

### Dataset:-
#### For Emotion Prediction  
1. *RAVDESS (Ryerson Audio-Visual Database of Emotional Speech and Song)*:
   - RAVDESS is a dataset designed for research on emotional speech and song. It contains audio and video recordings of 24 professional actors (12 male, 12 female) performing various scripted emotions.

2. *CESS (Chinese Emotional Speeches Dataset)*:
   - CESS is a dataset aimed at studying emotional speech in the Chinese language. It consists of audio recordings of speakers expressing various emotions in Mandarin Chinese.

3. *TESS (Toronto Emotional Speech Set)*:
   - TESS is a dataset containing audio recordings of emotional speech in English.

4. *SAVEE (Surrey Audio-Visual Expressed Emotion)*:
   - SAVEE is a dataset containing audio recordings of spoken English sentences representing different emotions.
  
#### For DeepFake Prediction  
1. The real voice dataset provided from https://commonvoice.mozilla.org/en/datasets which contains the common voice of real users in different languages, We took the english(~1GB) and spanish (~800 MB) voice data
2. For the fake ai voice dataset we took the data provided by the team in the repo and some other were taken by writing a script for api calls to elevenlabs (We could get only handlful of data from here as it is limited to certain number of free calls)

#### For background Intensity Detection
1. Here we recorded custom voice from our phone and then we extracted the noise signal using noisereduce python library.
2. We then compared the intensity of background noise with the audio without noise to decide the background sound level.

#### For Liveliness detection  
Primarily based on the ASVspoof 2017 Version 2.0 dataset.
In addition to the ASVspoof dataset, the authors introduced a self-built replay attack dataset, as well as various other attack methods including hidden speech, ultrasonic speech commands, and synthesized speech, to validate the effectiveness of the Void system.


## Setup
1. Git Clone this repository.

```bash
$ https://github.com/Hackathon2024-March/sherlocked.git
$ cd code/Server Microservice_with3 models working
```
2. Start Services

 ```bash
$ python app.py
```
3. If the build and run went without problems, then you can follow the link http://127.0.0.1:5000/.

