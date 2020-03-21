## Alarm using Raspberry Pi and Face Recognition
As is shown on the title, we will be applying face recognition technology with an amazing Raspberry Pi equipped with a camera and an alarm. Everytime someone that is not on the database appears for a given time, the alarm will ring to notify the owner!

### Requirements
```
opencv-python 4.1.1
numpy
```

### Structure

- buzzer.py: the link to the Raspberry Pi's alarm
- face_detection.py: simple script for face detection using haarcascade in opencv
- face_recognition.py: script for recognition and training of model in opencv
- get_face.py: script to store the training images
- haarcascade_frontalface_default.xml: pre-trained model for face detection 
- main.py: main script

### How to use
In order to set this software part up, first run the get_face.py script and follow the printed instructions on console. Then after that, you are good to go to run the main script, main.py.

### Contact
Contact us on this website https://aitechfordummies.com for any specific questions, or bugs.