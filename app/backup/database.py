import os
import subprocess
import threading

from app.progress.spinner import spinner


def database_backup(db_data, filepath):
    stop_event = threading.Event()
    thread = threading.Thread(target=spinner, args=("Backing up PostgreSQL...", stop_event))
    thread.start()

    if db_data['db_type'] == 'postgres':
        cmd = [
            "pg_dump",
            "-h", db_data["db_host"],
            "-U", db_data["db_user"],
            "-F", "c",
            "-b",
            "-v",
            "-f", filepath,
            db_data["db_name"],
        ]

        env = os.environ.copy()
        env["PGPASSWORD"] = db_data["db_pass"]

        subprocess.run(cmd, env=env, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    elif db_data['db_type'] == 'mysql':
        pass

    stop_event.set()
    thread.join()

    print(f'PostgreSQL backup ({db_data["name"]}) completed ✔')
    return