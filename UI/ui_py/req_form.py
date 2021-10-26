# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'req_form.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDateTimeEdit, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(300, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        Form.setFont(font)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.formation_date_le = QDateEdit(Form)
        self.formation_date_le.setObjectName(u"formation_date_le")
        self.formation_date_le.setCurrentSection(QDateTimeEdit.DaySection)
        self.formation_date_le.setCalendarPopup(False)
        self.formation_date_le.setDate(QDate(2000, 1, 1))

        self.gridLayout.addWidget(self.formation_date_le, 3, 0, 1, 1)

        self.number_cb = QLineEdit(Form)
        self.number_cb.setObjectName(u"number_cb")
        sizePolicy.setHeightForWidth(self.number_cb.sizePolicy().hasHeightForWidth())
        self.number_cb.setSizePolicy(sizePolicy)
        self.number_cb.setMinimumSize(QSize(180, 22))
        self.number_cb.setMaximumSize(QSize(180, 22))

        self.gridLayout.addWidget(self.number_cb, 1, 0, 1, 2)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041e\u0442:", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0422\u0440\u0435\u0431\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.formation_date_le.setDisplayFormat(QCoreApplication.translate("Form", u"dd.MM.yyyy", None))
    # retranslateUi

