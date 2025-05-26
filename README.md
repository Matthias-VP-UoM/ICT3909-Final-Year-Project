# ICT3909 - Final Year Project: Using Computer Vision to Analyse Emotions in a Two-Person Interview

## Project Overview
The main aim of this project was to design and implement a facial emotion recognition system that which can analyse emotional dynamics in two-person interviews, utilising various Computer Vision and Machine Learning techniques. This framework utilises a dataset consisting of 24 videos of Maltese podcasts, 22 from Jon Mallia and 2 from Mark Laurence Zammit via Times Talk. These videos are fully extracted from the YouTube platform. Following this, individual frames are extracted from the videos given a predefined time frame, from which facial ROIs are extracted. The frames and ROIs are saved into separate folders, thus making them 2 separate datasets. From the ROIs, person and emotion classification is performed, utilising facial recognition to recognise the individual and assign a person label (i.e. interviewer or interviewee), and emotion prediction to predict the emotion conveyed by the facial expression by the person in the ROI image. This information is saved into a data file per video, which is then used by the program to visualise the results, both in the form of graphs and processed frames. The former makes use of bar and pie charts to visualise the distribution of the emotions classified by each labelled person throughout the video, whilst the latter integrates bounding boxes around the detected faces in a given frame, while also including displaying the person and emotion labels.

## Tested Models/Backends

The Person Classification Process was evaluated by testing and comparing the results from the following 3 facial recognition models:
- ArcFace
- VGG-Face
- FaceNet-512

The Emotion Classification Process was evaluated by testing and comparing the results from the following 3 backend detectors:
- YOLOv8
- RetinaFace
- MTCNN

Following the whole evaluation process, the combination of **FaceNet-512** for Person Classification and **MTCNN** for Emotion Classification achieved the best overall results. The final version of the implementation makes use of this combination.

## Main Technologies Used

<i>NOTE: All the dependencies that are used by the program can be installed using the provided requirements.txt file. More information about how to install them will be provided soon.</i>

This project primarily makes use of the following technologies in its implementation:
- **OpenCV**
- **Pillow**
- **DeepFace**
- **PyTube** (this project makes use of the **pytube-fix** package, which is a version of the main package which fixes some weird bugs)
- **Numpy**
- **Pandas**
- **Translate** (for extracting names from video titles/author)
- **Google Translate** (for extracting names from video descriptions)
- **Spacy** (the model utilised is the **"en_core_web_trf"** English model, which can be installed by following this site: https://spacy.io/models/en#en_core_web_trf
- **Sckit-Learn** (for evaluating the classification processes)

