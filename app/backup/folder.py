import os
import tarfile


def folders_backup(folder: str, out_path: str):
    folder_path = folder

    with tarfile.open(out_path, "w:gz") as tar:
        for root, dirs, files in os.walk(folder_path):

            dirs[:] = [d for d in dirs if d != "venv"]

            for file in files:
                if file == "nohup.out":
                    continue

                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, folder_path)

                tar.add(full_path, arcname=rel_path)