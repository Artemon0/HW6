import glob
import os
import shutil


def sort_files(path: str) -> None:
    files_dict = {'archives': [], 'audio': [], 'documents': [],
                  'images': [], 'unknown': [], 'video': []}

    for filename in os.listdir(path):
        fullpath = os.path.join(path, filename)
        path = glob.glob(path)
        if os.path.isdir(fullpath):
            sort_files(fullpath)
            continue

        ext = os.path.splitext(filename)[1][1:].lower()

        if ext in ('jpeg', 'png', 'jpg', 'svg'):
            files_dict['images'].append(filename)
        elif ext in ('avi', 'mp4', 'mov', 'mkv'):
            files_dict['video'].append(filename)
        elif ext in ('doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'):
            files_dict['documents'].append(filename)
        elif ext in ('mp3', 'ogg', 'wav', 'amr'):
            files_dict['audio'].append(filename)
        elif ext in ('zip', 'gz', 'tar'):
            files_dict['archives'].append(filename)
        else:
            files_dict['unknown'].append(filename)

    for folder in files_dict.keys():
        folder_path = os.path.join(path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    for folder, files in files_dict.items():
        for file in files:
            old_path = os.path.join(path, file)
            new_filename = file
            new_path = os.path.join(path, folder, new_filename)
            if os.path.exists(new_path):
                name, ext = os.path.splitext(new_filename)
                new_filename = f'{name}_1.{ext}'
                new_path = os.path.join(path, folder, new_filename)
            shutil.move(old_path, new_path)

    for folder, files in files_dict.items():
        if len(files) > 0:
            print(f'{folder}:')
            for file in files:
                print(file)
# if __name__ == "__main__":
#     path = "/user/Desktop/Хлам"
#     sort_files(path)