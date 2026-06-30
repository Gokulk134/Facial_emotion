# Facial Emotion Recognition using OpenCV

## Overview

This project performs **real-time facial emotion recognition** using a webcam. It captures live video through OpenCV, detects faces, predicts emotions using a pre-trained emotion recognition model, and displays the detected emotion on the video feed.

## Features

- Real-time webcam capture
- Face detection
- Emotion recognition
- Displays predicted emotion on live video
- Runs on CPU

## Technologies Used

- Python
- OpenCV
- facial_emotion_recognition
- NumPy

## Project Structure

```
.
├── emotion_detection.py
├── README.md
└── requirements.txt
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/facial-emotion-recognition.git
```

### 2. Navigate to the project directory

```bash
cd facial-emotion-recognition
```

### 3. Install the required packages

```bash
pip install opencv-python
pip install facial-emotion-recognition
```

Or install all dependencies using:

```bash
pip install -r requirements.txt
```

## Code

```python
from facial_emotion_recognition import EmotionRecognition
import cv2

ver = EmotionRecognition(device='cpu')
cam = cv2.VideoCapture(0)

while True:
    success, frame = cam.read()

    if not success:
        break

    frame = ver.recognise_emotion(frame, return_type='BGR')

    cv2.imshow("Emotion Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cam.release()
cv2.destroyAllWindows()
```

## How It Works

1. Loads the emotion recognition model.
2. Opens the webcam using OpenCV.
3. Captures live video frames.
4. Detects faces in each frame.
5. Predicts the facial emotion.
6. Displays the emotion label on the video feed.
7. Press **Esc** to exit the application.

## Supported Emotions

The model can recognize emotions such as:

- Happy 😊
- Sad 😢
- Angry 😠
- Neutral 😐
- Fear 😨
- Surprise 😲
- Disgust 🤢

*(The exact emotions depend on the model used by the library.)*

## Requirements

- Python 3.8 or later
- Webcam
- OpenCV
- facial_emotion_recognition package

## Output

The application opens a webcam window similar to:

```
+----------------------------------+
|                                  |
|   😀 Happy                        |
|  ┌──────────────┐                |
|  │              │                |
|  │    Face      │                |
|  │              │                |
|  └──────────────┘                |
|                                  |
+----------------------------------+
```

## Future Improvements

- GPU support
- Multiple face detection
- Emotion statistics
- Emotion logging
- Real-time emotion graphs
- GUI using Tkinter or PyQt

## License

This project is licensed under the MIT License.

## Author

Gokul

GitHub: https://github.com/Gokulk134
