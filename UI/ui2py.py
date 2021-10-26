import os
import re

def generate_all_ui2py(path):
    files = os.listdir(path)
    pattern = re.compile(r'.*\.ui')
    ui_list = [i for i in files if pattern.match(i)]
    new_path = r'{}\\ui_py'.format(os.path.dirname(os.path.abspath(__file__)))

    for i in ui_list:
        file_path = os.path.join(path, i)
        file_name_without_extension = file_path.split(os.sep)[-1].removesuffix('.ui')
        cmd = f'pyside6-uic {file_path} > {new_path}{os.sep}{file_name_without_extension}.py'
        os.popen(cmd)

if __name__ == '__main__':
    path = r'{}\\ui_ui'.format(os.path.dirname(os.path.abspath(__file__)))
    generate_all_ui2py(path)

