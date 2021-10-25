import json
import sys
import qrcode
from PIL.ImageQt import ImageQt


from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtGui import QFont, QPixmap, QImage
from PySide6.QtCore import Qt
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm



from UI.qr_ui import Ui_Form


# pyinstaller -F -w -i "C:\Users\Philipp\Downloads\dna.ico" main.py для компиляции в exe


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.form_button.clicked.connect(self.read_info)
        self.ui.clear_button.clicked.connect(self.clear)


    def read_info(self):
        info = {
            'initiator': self.ui.initiator.text(),
            'post': self.ui.post.text(),
            'agency': self.ui.agency.text(),
            'surname': self.ui.surname.text(),
            'name': self.ui.name.text(),
            'middle_name': self.ui.middle_name.text(),
            'date_of_birth': self.ui.date_of_birth.text(),
            'birthplace': self.ui.birthplace.text(),
            'case_number': self.ui.case_number.text(),
            'article': self.ui.article.text(),
            'fable': self.ui.fable.toPlainText()
        }
        json_obj = json.dumps(info, indent=4, ensure_ascii=False)
        img = qrcode.make(json_obj)
        img.save('qr_image/qr_image.png')
        qr = ImageQt(img)
        pix = QPixmap.fromImage(qr).scaledToHeight(300)


        self.ui.qr_label.setPixmap(pix)

        doc = DocxTemplate("word_templates/research_referral_person_template.docx")
        image = InlineImage(doc, image_descriptor='qr_image/qr_image.png', width=Mm(50), height=Mm(50))
        context = {
            'organization': info['agency'],
            'address': 'ул. Дорожная-7, г. Саяногорск, 655603 тел.факс 83904262967',
            'case': info['case_number'],
            'qr': image
        }
        doc.render(context)
        docs_name = '{} {} {}'.format(info['surname'], info['name'], info['middle_name'])
        doc.save(f"research_directions/{docs_name}.docx")



    def clear(self):
        self.ui.qr_label.clear()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec())
