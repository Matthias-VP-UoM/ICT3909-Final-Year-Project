# ICT3909 - Final Year Project: Using Computer Vision to Analyse Emotions in a Two-Person Interview

**Author:** Matthias Vassallo Pulis

**Supervisor:** Dr Dylan Seychell
<br>
**Co-supervisor**: Dr Konstantinos Makantasis

## Project Overview
This project aims to limit subjectivity bias and increase transparency in emotional awareness by creating a system that can analyse temporal changes in emotions by both the interviewer and interviewee in two-person interviews, utilising various Computer Vision and Machine Learning techniques. This framework utilises a dataset consisting of 24 videos of Maltese podcasts, 22 from Jon Mallia and 2 from Mark Laurence Zammit via Times Talk. These videos are fully extracted from the YouTube platform. Following this, individual frames are extracted from the videos given a predefined time frame, from which facial ROIs are extracted. The frames and ROIs are saved into separate folders, thus making them 2 separate datasets. From the ROIs, person and emotion classification is performed, utilising facial recognition to recognise the individual and assign a person label (i.e. interviewer or interviewee), and emotion prediction to predict the emotion conveyed by the facial expression by the person in the ROI image. This information is saved into a data file per video, which is then used by the program to visualise the results, both in the form of graphs and processed frames. The former makes use of bar and pie charts to visualise the distribution of the emotions classified by each labelled person throughout the video, whilst the latter integrates bounding boxes around the detected faces in a given frame, while also including displaying the person and emotion labels.

## Tested Models/Backends

The Person Classification Process was evaluated by testing and comparing the results from the following 3 facial recognition models:
- **ArcFace**
- **VGG-Face**
- **FaceNet-512**

The Emotion Classification Process was evaluated by testing and comparing the results from the following 3 backend detectors:
- **YOLOv8**
- **RetinaFace**
- **MTCNN**

Following the whole evaluation process, the combination of **FaceNet-512** for Person Classification and **RetinaFace** for Emotion Classification achieved the best overall results. The final version of the implementation makes use of this combination.

## Main Technologies Used

<i>NOTE: All the dependencies that are used by the program can be installed using the provided requirements.txt file. More information about how to install them is provided below.</i>

This project primarily makes use of the following technologies in its implementation:
- **OpenCV**
- **Pillow**
- **DeepFace**
- **PyTube** (this project makes use of the **pytube-fix** package, which is a version of the main package which fixes some weird bugs)
- **Numpy**
- **Pandas**
- **Translate** (for translating video titles/author)
- **Google Translate** (for translating video descriptions)
- **Spacy** (for extracting names) (the model utilised is the **"en_core_web_trf"** English model, which can be installed by following this site: https://spacy.io/models/en#en_core_web_trf
- **Sckit-Learn** (for evaluating the classification processes)

## Repository Structre

### Folders
- **data** - This folder contains the core data responsible for running the entire implementation, including video URLs lists, intermission data. It also stores the analysis results and the interviewer and interviewee names for each video.
- **evaluation** - This folder contains the code, data and results generated from the evaluation process.
- **experiment-data** - This folder contains the extra analysis results during testing, which was also used during evaluation.
- **face_rois_dt** - The main facial ROIs database folder
- **face_rois_dt_ml** - A copy of the above ROIs database folder which was used to differentiate between Mark Laurence Zammit videos (Times Talk) and Jon Mallia videos. <i>This can be avoided when using the main part of the program</i>.
- **frame_visuals** - This folder stores a copy of video frames with visualised results from the generated analysis
- **reference_imgs** - This folder stores known faces for each interviewer and interviewee, which is used for Person Classification
- <b>vid_frames*</b> - The main video frames database folder
- <b>vid_frames_ml*</b> - A copy of the above frames database folder which was used to differentiate between Mark Laurence Zammit videos (Times Talk) and Jon Mallia videos. <i>This can be avoided when using the main part of the program</i>.
- <b>videos_dt**</b> - The main videos database folder
- <b>videos_dt_ml**</b> - A copy of the above videos database folder which was used to differentiate between Mark Laurence Zammit videos (Times Talk) and Jon Mallia videos. <i>This can be avoided when using the main part of the program</i>.

<b>*</b> Due to size constraints, only the frames from the videos used in the evaluation set can be seen in this repository. The full frames database can be accessed by using the below Google Drive link.

<b>**</b> Due to size constraints, the Videos Database is not hosted directly in this repository. The full Videos Database can be accessed by using the below Google Drive link.

**NOTE: Despite the above difficulties, all the facial ROI images from all the videos are still available in the repository, as they weren't affected by size contraints.**

### Files
- **1 - video_data_extraction.ipynb** - Downloads and stores interview videos from the URLs list in the **data** folder and extracts and stores interviewer and interviewee names for every downloaded video.
- **2 - facial_image_extraction.ipynb** - The first part (Frame Extraction) Extracts and stores video frames from **all** the downloaded videos whilst the second part (Facial ROI Extraction) extracts images containing the region of the detected faces from the frames previously extracted from a **single** downloaded video.
- **3 - person_and_emotion_classification.ipynb** - Performs person and emotion classification from a selected video and stores the results in the **data** folder.
- **4.1 - visualisation_create_table.ipynb** - Converts the generated analysis results from a given video from JSON to CSV and utilises them to visualise the results.
- **4.2 - visualisation_load_table.ipynb** - Similar to the above file but loads an already created CSV file instead of creating one from scratch.
- **4.3 - frame_analysis.ipynb** - Provides a visual feedback of the video analysis results by inserting them into individual video frames.
- **common_functionality.py** - Contains any common functionality that is used throughout the code provided.
- **face_rec.py** - Used to load and preprocess images (taken from the face_recognition Python package, which is included in the requirements.txt file)

## Ethics & Data Usage

- All data used in this project is sourced from a publicly available video platform (i.e. YouTube) under fair use for research purposes.
- No personal/private data is collected or stored.
- The system is **NOT** intended to be used in sensitive environments.

## Getting Started with the Application

### Prerequisities
- Python 3.10+

### 1. Clone the repository
The first step is to clone the entire repository, ensuring you have the available code to start the program:

```bash
git clone https://github.com/Matthias-VP-UoM/ICT3909-Final-Year-Project.git
```

### 2. Install package dependencies
In order to use the program, the correct dependencies must be installed. These can be installed using the provided requirements.txt file, which can be done using the below command:

```bash
pip install -r requirements.txt
```

### 3. Gather the datasets
As mentioned above, this GitHub repository does not include the entire Videos Database and the majority of the Video Frames Database.

These can be accessed by using the following Google Drive link: https://drive.google.com/drive/folders/1dIUKnuIl9bYR1NTiaXzUD0ud5LXUfG-e?usp=sharing

The contents of the provided zip files should be extracted and placed in the working directory where the project is saved.

<i>Alternatively, the full Videos Database can be obtained by running the first part of the "video_data_extraction" notebook, while the full Video Frames Database can be extracted following this process by executing the first part of the "facial_image_extraction" notebook. This can be done as the list of video URLs that were used during the project's development is made available inside the **data** folder.</i>

## Important Note

This was developed as part of the <b><i>ARI3333</i></b> study unit, which is titled <b><i>Final Year Project in Artificial Intelligence</i></b>. The project was submitted in partial fulfilment of the requirements for the B.Sc. in IT (Honours) (Artificial Intelligence) course at the University of Malta.
