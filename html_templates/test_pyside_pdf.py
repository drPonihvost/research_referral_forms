import os
import sys

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import QMarginsF
from PySide6.QtGui import QPageLayout, QPageSize
from PySide6.QtWebEngineCore import QWebEnginePage
from faker import Faker
from jinja2 import Environment, FileSystemLoader, select_autoescape


def create_persons(number):
    fake = Faker(['ru_RU'])
    fake.date_between(start_date='-60y', end_date='-20y')
    persons = []
    for i in range(number):
        person = {
            'number': i + 1,
            'surname': fake.last_name(),
            'name': fake.first_name(),
            'patronymic': fake.middle_name(),
            'birthday': fake.date(),
            'birthplace': fake.address(),
            'qr_person_img': 'img/qr_image.png'
        }
        persons.append(person)
    return persons


data = dict(
    name='МВД РОССИИ',
    plot_qr_image="img/qr_image.png",
    persons=create_persons(10)
)

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html'])
)
template = env.get_template('research_template.html')
rendered_page = template.render(**data)

with open("my_new_file.html", "w", encoding="UTF-8") as fh:
    fh.write(rendered_page)


def html_to_pdf(html, pdf):
    app = QtWidgets.QApplication(sys.argv)

    page = QWebEnginePage()

    def handle_print_finished(filename, status):
        print("finished", filename, status)
        QtWidgets.QApplication.quit()

    def handle_load_finished(status):
        if status:
            param = QPageLayout(QPageSize(QPageSize.A4), QPageLayout.Portrait, QMarginsF())
            param.setUnits(QPageLayout.Millimeter)
            param.setRightMargin(20.0)
            param.setLeftMargin(20.0)
            param.setTopMargin(20.0)
            param.setBottomMargin(15.0)

            page.printToPdf(pdf, param)
        else:
            print("Failed")
            QtWidgets.QApplication.quit()

    page.pdfPrintingFinished.connect(handle_print_finished)
    page.loadFinished.connect(handle_load_finished)
    page.load(QtCore.QUrl.fromLocalFile(html))
    app.exec()


if __name__ == "__main__":
    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(CURRENT_DIR, "my_new_file.html")
    print(filename)

    html_to_pdf(filename, "test.pdf")

# # def loadCSS(view, path, name):
# #     path = QtCore.QFile(path)
# #     if not path.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text):
# #         return
# #     css = path.readAll().data().decode("utf-8")
# #     SCRIPT = """
# #     (function() {
# #     css = document.createElement('style');
# #     css.type = 'text/css';
# #     css.id = "%s";
# #     document.head.appendChild(css);
# #     css.innerText = `%s`;
# #     })()
# #     """ % (name, css)
# #
# #     script = QtWebEngineCore.QWebEngineScript()
# #     view.runJavaScript(SCRIPT, QtWebEngineCore.QWebEngineScript.ApplicationWorld)
# #     script.setName(name)
# #     script.setSourceCode(SCRIPT)
# #     script.setInjectionPoint(QtWebEngineCore.QWebEngineScript.DocumentReady)
# #     script.setRunsOnSubFrames(True)
# #     script.setWorldId(QtWebEngineCore.QWebEngineScript.ApplicationWorld)
# #     view.scripts().insert(script)
