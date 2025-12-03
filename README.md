# MultiBackup

Сценарий для автоматических бекапов баз данных и папок в чат телеграм с заданной переодичностью

## Структура

```
multibackup/
  app/                # Планировщик, выгрузка в облако, отправка в телеграм, функции
  config/             # YAML и JSON-конфиги (settings/folders/databases)
  main.py             # Точка запуска приложения
  requirements.txt    # Python-зависимости
```

## Запуск

1. Создать виртуальное окружение и установить зависимости:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
   
2. Запустить приложение в фоне:
   ```bash
   nohup python3 main.py &
   ```
   
3. Выйти из виртуального окружения:
   ```bash
   deactivate
   ```