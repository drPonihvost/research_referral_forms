import os
import PyInstaller.__main__

path = os.path.dirname(__file__) + '/venv/Lib/site-packages/PySide6/QtWebEngineProcess.exe'
PyInstaller.__main__.run([
    'main.py',
    '--onedir',
    '--console',
    '--add-data=db_SQLite3.db;.',
    f'--add-data={path};.'
])
