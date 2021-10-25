# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qr_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(765, 550)
        self.formLayout_2 = QFormLayout(Form)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.initiator = QLineEdit(Form)
        self.initiator.setObjectName(u"initiator")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.initiator)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.post = QLineEdit(Form)
        self.post.setObjectName(u"post")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.post)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.agency = QLineEdit(Form)
        self.agency.setObjectName(u"agency")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.agency)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.surname = QLineEdit(Form)
        self.surname.setObjectName(u"surname")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.surname)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.name = QLineEdit(Form)
        self.name.setObjectName(u"name")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.name)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.middle_name = QLineEdit(Form)
        self.middle_name.setObjectName(u"middle_name")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.middle_name)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_7)

        self.date_of_birth = QDateEdit(Form)
        self.date_of_birth.setObjectName(u"date_of_birth")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.date_of_birth)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_8)

        self.birthplace = QLineEdit(Form)
        self.birthplace.setObjectName(u"birthplace")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.birthplace)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_9)

        self.case_number = QLineEdit(Form)
        self.case_number.setObjectName(u"case_number")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.case_number)

        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_10)

        self.fable = QPlainTextEdit(Form)
        self.fable.setObjectName(u"fable")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.fable)

        self.article = QLineEdit(Form)
        self.article.setObjectName(u"article")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.article)

        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_11)


        self.formLayout_2.setLayout(0, QFormLayout.LabelRole, self.formLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.qr_label = QLabel(Form)
        self.qr_label.setObjectName(u"qr_label")
        self.qr_label.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qr_label.sizePolicy().hasHeightForWidth())
        self.qr_label.setSizePolicy(sizePolicy)
        self.qr_label.setMinimumSize(QSize(350, 350))
        self.qr_label.setMaximumSize(QSize(350, 350))

        self.verticalLayout.addWidget(self.qr_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.form_button = QPushButton(Form)
        self.form_button.setObjectName(u"form_button")

        self.horizontalLayout.addWidget(self.form_button)

        self.clear_button = QPushButton(Form)
        self.clear_button.setObjectName(u"clear_button")

        self.horizontalLayout.addWidget(self.clear_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.formLayout_2.setLayout(0, QFormLayout.FieldRole, self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0418\u043d\u0438\u0446\u0438\u0430\u0442\u043e\u0440 (\u0424\u0418\u041e) ", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041e\u0440\u0433\u0430\u043d", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u041c\u0435\u0441\u0442\u043e \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u2116 \u0443/\u0434", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0441\u0442\u0430\u0432", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u0441\u0442\u0430\u0442\u044c\u044f \u0423\u041a \u0420\u0424", None))
        self.qr_label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.form_button.setText(QCoreApplication.translate("Form", u"\u0421\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.clear_button.setText(QCoreApplication.translate("Form", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
    # retranslateUi

