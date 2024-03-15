from speec2emotion import predict
from noiseIntensityDetection import findIntensity
from deepfakeDetection import predictDeepFake
path=r'F:\Hackathon_2024\Server Integration Models\Audios\aud1_ang.wav'
print("started")
# print(findIntensity(path))
print(predict(path))
# print(predictDeepFake(path))
