from cx_Freeze import setup, Executable

executables = [Executable("main.py")]

options = {
    'build_exe': {
        'includes': [
            'base_widgets',
            'add_event_dialog',
            'division_form',
            'error_widget',
            'event_form',
            'event_widget',
            'form_blank_wizard',
            'html_templates',
            'main_window',
            'models',
            'official_person_form',
            'official_person_widget',
            'person_to_check_form',
            'person_to_check_widget',
            'person_to_check_widget_for_wizard',
            'research_widget',
            'research_wizard'
        ]
    }
}

setup(name='Research Referral Form',
      version='0.0.1',
      description='Программа для создания направлений на исследование ДНК',
      executables=executables,
      options=options)
