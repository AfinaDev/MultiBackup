from app.backup.database    import database_backup
from app.backup.folder      import folders_backup
from app.cloud.upload       import upload
from app.notify.telegram    import send_backup

from app.utils.cleaner      import clear_storage
from app.utils.current_time import current_time
from app.utils.load_json    import load_json
from app.utils.load_yaml    import load_yaml
from app.utils.scheduler    import scheduler

config = load_yaml('config/settings.yaml')

def main():
    clear_storage()
    time_backup = current_time()

    data_databases = load_json(config['settings']['path_config']['databases_json'])
    data_paths     = load_json(config['settings']['path_config']['folders_json'])

    if data_databases:
        for db in data_databases:
            filepath = f"{config['settings']['path_backup']['databases_backup']}/{db['name']}.sql"
            database_backup(db, filepath)

    if data_paths:
        for folder in data_paths:
            filepath = f"{config['settings']['path_backup']['folders_backup']}/{folder['name']}.tar.gz"
            folders_backup(folder['full_path'], filepath)

    filepath = f"{config['settings']['path_backup']['root_backup']}/{time_backup}.tar.gz"
    folders_backup(config['settings']['path_backup']['root_backup'], filepath)

    response_link = upload(config['settings']['gofile_io']['api_domain'], config['settings']['gofile_io']['api_token'], filepath)
    send_backup(config['settings']['telegram']['api_token'], config['settings']['telegram']['chat_id'], response_link, time_backup)

if __name__ == '__main__':
    scheduler(main, int(config['settings']['delay']))