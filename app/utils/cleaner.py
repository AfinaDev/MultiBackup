import os
import shutil

def clear_storage():
    storage_path = "storage"

    if os.path.exists(storage_path):
        shutil.rmtree(storage_path)

    os.makedirs(storage_path)

    os.makedirs(os.path.join(storage_path, "backup_db"))
    os.makedirs(os.path.join(storage_path, "backup_folders"))