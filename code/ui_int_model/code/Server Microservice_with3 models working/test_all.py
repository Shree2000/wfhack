from speec2emotion import predict
from noiseIntensityDetection import findIntensity
from deepfakeDetection import predictDeepFake
path=r'F:\Hackathon_2024\Server Integration Models\Server Microservice_with3 models working\aud5.mp3'
print("started")
# print(findIntensity(path))
print(predict(path))
# print(predictDeepFake(path))
