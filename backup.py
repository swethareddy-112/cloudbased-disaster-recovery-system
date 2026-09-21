import os
import shutil
from database import add_backup


SOURCE_FOLDER = "source_data"
CLOUD_FOLDER = "cloud_storage"


def create_backup():

    os.makedirs(SOURCE_FOLDER, exist_ok=True)
    os.makedirs(CLOUD_FOLDER, exist_ok=True)

    files = os.listdir(SOURCE_FOLDER)

    if not files:
        print("No files available for backup.")
        return

    for filename in files:

        source_path = os.path.join(
            SOURCE_FOLDER,
            filename
        )

        destination_path = os.path.join(
            CLOUD_FOLDER,
            filename
        )

        if os.path.isfile(source_path):

            shutil.copy2(
                source_path,
                destination_path
            )

            add_backup(
                filename,
                "Backup Successful"
            )

            print(
                f"Backup completed: {filename}"
            )


if __name__ == "__main__":
    create_backup()