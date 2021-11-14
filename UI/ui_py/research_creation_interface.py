# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'research_creation_interface.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDateTimeEdit,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_ud_form(object):
    def setupUi(self, ud_form):
        if not ud_form.objectName():
            ud_form.setObjectName(u"ud_form")
        ud_form.resize(506, 427)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(12)
        ud_form.setFont(font)
        self.verticalLayout = QVBoxLayout(ud_form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.item_de = QComboBox(ud_form)
        self.item_de.setObjectName(u"item_de")

        self.gridLayout.addWidget(self.item_de, 6, 0, 1, 2)

        self.number_cb = QLineEdit(ud_form)
        self.number_cb.setObjectName(u"number_cb")

        self.gridLayout.addWidget(self.number_cb, 1, 0, 1, 2)

        self.label_2 = QLabel(ud_form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)

        self.label_3 = QLabel(ud_form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 2)

        self.label = QLabel(ud_form)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.formation_date_le = QDateEdit(ud_form)
        self.formation_date_le.setObjectName(u"formation_date_le")
        self.formation_date_le.setCurrentSection(QDateTimeEdit.DaySection)
        self.formation_date_le.setCalendarPopup(False)
        self.formation_date_le.setDate(QDate(2000, 1, 1))

        self.gridLayout.addWidget(self.formation_date_le, 3, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        QWidget.setTabOrder(self.number_cb, self.item_de)

        self.retranslateUi(ud_form)

        QMetaObject.connectSlotsByName(ud_form)
    # setupUi

    def retranslateUi(self, ud_form):
        ud_form.setWindowTitle(QCoreApplication.translate("ud_form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("ud_form", u"\u0412\u043e\u0437\u0431\u0443\u0436\u0434\u0435\u043d\u043d\u043e\u0435 \u043e\u0442", None))
        self.label_3.setText(QCoreApplication.translate("ud_form", u"\u041f\u043e \u0441\u0442\u0430\u0442\u044c\u0435", None))
        self.label.setText(QCoreApplication.translate("ud_form", u"\u0423\u0433\u043e\u043b\u043e\u0432\u043d\u043e\u0435 \u0434\u0435\u043b\u043e \u2116:", None))
        self.formation_date_le.setDisplayFormat(QCoreApplication.translate("ud_form", u"dd.MM.yyyy", None))
    # retranslateUi

