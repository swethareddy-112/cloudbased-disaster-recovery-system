import os
import shutil


CLOUD_FOLDER = "cloud_storage"
RESTORE_FOLDER = "restored_data"


def restore_backup():

    os.makedirs(RESTORE_FOLDER, exist_ok=True)

    files = os.listdir(CLOUD_FOLDER)

    if not files:
        print("No backup files found.")
        return

    for filename in files:

        source_path = os.path.join(
            CLOUD_FOLDER,
            filename
        )

        destination_path = os.path.join(
            RESTORE_FOLDER,
            filename
        )

        if os.path.isfile(source_path):

            shutil.copy2(
                source_path,
                destination_path
            )

            print(
                f"Restored successfully: {filename}"
            )


if __name__ == "__main__":
    restore_backup()