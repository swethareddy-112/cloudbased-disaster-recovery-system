from flask import Flask, render_template
from database import create_database, get_backups
from backup import create_backup
from restore import restore_backup
import os


app = Flask(__name__)

create_database()


@app.route("/")
def home():

    backups = get_backups()

    total_backups = len(backups)

    successful_backups = sum(
        1 for backup in backups
        if backup["status"] == "Backup Successful"
    )

    cloud_files = 0

    if os.path.exists("cloud_storage"):
        cloud_files = len(
            [
                file
                for file in os.listdir("cloud_storage")
                if os.path.isfile(
                    os.path.join("cloud_storage", file)
                )
            ]
        )

    return render_template(
        "index.html",
        backups=backups,
        total_backups=total_backups,
        successful_backups=successful_backups,
        cloud_files=cloud_files
    )


@app.route("/backup")
def backup():

    create_backup()

    return """
    <h2>☁️ Backup completed successfully!</h2>
    <p>Your files have been copied to cloud storage.</p>
    <a href="/">Go back to dashboard</a>
    """


@app.route("/restore")
def restore():

    restore_backup()

    return """
    <h2>🔄 Restore completed successfully!</h2>
    <p>Your files have been recovered.</p>
    <a href="/">Go back to dashboard</a>
    """


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )