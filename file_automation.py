import os
import shutil

folders = {
    'Images': ['.jpg', '.png', '.jpeg'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Videos': ['.mp4', '.mkv'],
    'Archives': ['.zip', '.rar']
}

path = "D:/New folder (2)"

for file in os.listdir(path):
    for folder,extensions in folders.items():
        if any (file.endswith(ext)for ext in extensions):
            folder_path = os.path.join(path,folder)
            os.makedirs(folder_path,exist_ok=True)
            shutil.move(os.path.join(path,file),os.path.join(folder_path))