import os
import PyInstaller.__main__

path = os.path.dirname(__file__) + '/venv/Lib/site-packages/PySide2/QtWebEngineProcess.exe'
ico_path = os.path.join(os.path.dirname(__file__), 'resources/icon/dna_icon.ico')
PyInstaller.__main__.run([
    'ResearchReferralForm.py',
    '--onedir',
    '--noconsole',
    f'--icon={ico_path}',
    '--add-data=db_SQLite3.db;.',
    f'--add-data={path};.',
    '--add-data=initial_data.json;.'
])
