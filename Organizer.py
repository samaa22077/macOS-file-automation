import os
import shutil
import time

source_dir = "/Users/sama/Downloads"

def organize_files():
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        if os.path.isfile(file_path):
            name_lower = filename.lower()

        if filename.endswith(('.png','.jpg','.jpeg')) and ('screenshot' in name_lower or 'لقطة' in name_lower):
           target_dir = os.path.join(source_dir, "Screenshots") 
        
        elif filename.endswith(('.mp4','.mov')) and ('screen recording' in name_lower or 'تسجيل' in name_lower):
            target_dir = os.path.join(source_dir, "Screen Recordings")

        elif filename.endswith(('.docx','.doc')):
            target_dir = os.path.join(source_dir, "Documents word")

        elif filename.endswith(('.pdf')):
            target_dir = os.path.join(source_dir, "PDFs")
        
        elif filename.endswith(('.mp4','.mov')):
            target_dir = os.path.join(source_dir, "Videos")

        elif filename.endswith(('.png','.jpg','.JPG','HEIC','.jpeg','heic','JPEG')):
            target_dir = os.path.join(source_dir, "Images")

        else:
           continue

        os.makedirs(target_dir, exist_ok=True)
        shutil.move(file_path, os.path.join(target_dir, filename))
        print(f"Moved: {filename} to {target_dir}")





        

os.system("osascript -e 'display dialog \"كل الملفات راحت مكانها!\" buttons {\"ممتاز\"} default button 1 with title \"SAMA File Organizer\"'")