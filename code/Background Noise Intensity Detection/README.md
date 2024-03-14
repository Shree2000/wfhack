 This file aims to develop a model for removing background noise intensity from audio recordings and subsequently detecting the presence of background noise. The model utilizes python library "noisereduce" to achieve accurate noise removal and detection. After detecting the intensity of the noise, the voice sample will be passed to liveliness voice detector microservice.

                +----------------+
                 |  Preprocessing |
                 +--------+-------+
                          |
                          v
              +-------------------------+
              | Background Noise Removal|
              +------------+------------+
                           |
                           v
             +----------------------------+
             | background Noise Extraction |
             +------------+---------------+
                            |
                            v
               +-----------------------+
               |  intensity Detection  |
               +------------+----------+
                            |
                            v
         +-----------------------------------------+
         | Liveliness voice detection microservice |
         +------------+----------------------------+
                            |
                            v
                           End

![image](https://github.com/Hackathon2024-March/sherlocked/assets/116094109/708f01f0-55f6-4ff9-8128-b02a19541d1e)



