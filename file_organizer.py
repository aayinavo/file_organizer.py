import os
import shutil

folderpath = input("Enter folder path: ")

if not os.path.exists(folderpath):
    print("Folder does not exist!")
    exit()

extensions = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Documents": [".pdf", ".docx", ".txt", ".xls"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Others": []
}

for file in os.listdir(folderpath):
    file_path = os.path.join(folderpath, file
