import os
import shutil

def organize():
    file_type = {
        'Pictures': ['.jpeg', '.jpg', '.png', '.JPG', '.PNG'],
        'Videos': ['.wmv', '.mov', '.mp4', '.avi'],
        'Compressed': ['.iso', '.tar', '.rz', '.7z','.dmg', '.rar', '.zip'],
        'Music': ['.mp3', '.wav'],
        'Shortcuts': ['.url','.lnk','.cda'],
        'Documents': ['.doc', '.docx', '.pdf', '.odt', '.xls', '.xlsx', '.ods', '.ppt', '.pptx', '.txt', '.PDF'],
        'Dev': ['.py', '.html', '.htm', '.cs', '.class', '.jar', '.cpp', '.c', '.sc', '.cc', '.java', '.mm', '.swift',
                '.r', '.yaml', '.cxx'],
        'Installers': ['.exe']}
    for key in file_type:
        if os.path.exists(os.path.normpath('C:/Users/szwed/Desktop/' + key)) != True:
            os.makedirs(os.path.normpath('C:/Users/szwed/Desktop/' + key))
        extension_list = file_type[key]
        for file in os.scandir(os.path.normpath('C:/Users/szwed/Desktop/')):
            extension = os.path.splitext(file)[1]
            dir, file = os.path.split(file)
            from_ = os.path.normpath('C:/Users/szwed/Desktop/' + file)
            to = os.path.normpath('C:/Users/szwed/Desktop/' + key)
            if extension in extension_list:
                shutil.move(from_, to)

organize()