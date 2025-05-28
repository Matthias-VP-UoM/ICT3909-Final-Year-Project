# Importing packages used throughout each of the below functions
import os
import json
import shutil

# Function which clears a specified folder
def clear_folder(folderName):
    try:
        #Iterating through the files in the folder
        for filename in os.listdir(folderName):
            file_path = os.path.join(folderName, filename)
            try:
                #Checking if the file is a file or a folder
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')
    except FileNotFoundError:
        print("Folder not found")
        exit(1)
    else:
        print("Folder cleared")

# Function that checks if a specified data file exists
def check_if_data_file_exists(vid_name):
    vid_data_full_path = os.path.join('data', 'video_data')
    if not os.path.exists(vid_data_full_path):
        return False
    else:
        items_in_path = os.listdir(vid_data_full_path)
        file_name_to_search = f'{vid_name}.json'
        if file_name_to_search not in items_in_path:
            return False
        else:
            return True

# Function to check that the video that is about to be processed contains a list of extracted frames
def validate_data_file(data_path):
    with open(data_path, 'r+') as f:
        processed_data = json.load(f)
        if 'frames_list' not in processed_data.keys():
            return False
        else:
            return True


# Function to check that the video that is about to be processed contains a list of extracted facial rois from the frames extracted
def validate_roi_list_exists(data_path):
    flag = True
    with open(data_path, 'r+') as f:
        processed_data = json.load(f)
        if 'frames_list' not in processed_data.keys():
            return False
        else:
            for frame in processed_data['frames_list']:
                if 'rois_list' not in frame.keys():
                    flag = False
                    break
                else:
                    flag = True
            return flag