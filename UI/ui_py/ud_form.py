# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ud_form.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_ud_form(object):
    def setupUi(self, ud_form):
        if not ud_form.objectName():
            ud_form.setObjectName(u"ud_form")
        ud_form.resize(300, 244)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ud_form.sizePolicy().hasHeightForWidth())
        ud_form.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        ud_form.setFont(font)
        self.verticalLayout = QVBoxLayout(ud_form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(ud_form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)

        self.label_4 = QLabel(ud_form)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 2)

        self.number_cb = QLineEdit(ud_form)
        self.number_cb.setObjectName(u"number_cb")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.number_cb.sizePolicy().hasHeightForWidth())
        self.number_cb.setSizePolicy(sizePolicy1)
        self.number_cb.setMinimumSize(QSize(180, 22))
        self.number_cb.setMaximumSize(QSize(16777215, 22))

        self.gridLayout.addWidget(self.number_cb, 1, 0, 1, 2)

        self.item_de = QComboBox(ud_form)
        self.item_de.setObjectName(u"item_de")
        self.item_de.setMinimumSize(QSize(180, 22))
        self.item_de.setMaximumSize(QSize(16777215, 22))

        self.gridLayout.addWidget(self.item_de, 5, 0, 1, 2)

        self.label_3 = QLabel(ud_form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 2)

        self.formation_date_le = QDateEdit(ud_form)
        self.formation_date_le.setObjectName(u"formation_date_le")
        self.formation_date_le.setCurrentSection(QDateTimeEdit.DaySection)
        self.formation_date_le.setCalendarPopup(False)
        self.formation_date_le.setDate(QDate(2000, 1, 1))

        self.gridLayout.addWidget(self.formation_date_le, 3, 0, 1, 1)

        self.label = QLabel(ud_form)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.number_cb_2 = QLineEdit(ud_form)
        self.number_cb_2.setObjectName(u"number_cb_2")
        sizePolicy1.setHeightForWidth(self.number_cb_2.sizePolicy().hasHeightForWidth())
        self.number_cb_2.setSizePolicy(sizePolicy1)
        self.number_cb_2.setMinimumSize(QSize(180, 22))
        self.number_cb_2.setMaximumSize(QSize(16777215, 22))

        self.gridLayout.addWidget(self.number_cb_2, 7, 0, 1, 2)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ud_form)

        QMetaObject.connectSlotsByName(ud_form)
    # setupUi

    def retranslateUi(self, ud_form):
        ud_form.setWindowTitle(QCoreApplication.translate("ud_form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("ud_form", u"\u0412\u043e\u0437\u0431\u0443\u0436\u0434\u0435\u043d\u043d\u043e\u0435 \u043e\u0442:", None))
        self.label_4.setText(QCoreApplication.translate("ud_form", u"\u0410\u0434\u0440\u0435\u0441 \u043c\u0435\u0441\u0442\u0430 \u043f\u0440\u043e\u0438\u0441\u0448\u0435\u0441\u0442\u0432\u0438\u044f:", None))
        self.label_3.setText(QCoreApplication.translate("ud_form", u"\u041f\u043e \u0441\u0442\u0430\u0442\u044c\u0435:", None))
        self.formation_date_le.setDisplayFormat(QCoreApplication.translate("ud_form", u"dd.MM.yyyy", None))
        self.label.setText(QCoreApplication.translate("ud_form", u"\u0423\u0433\u043e\u043b\u043e\u0432\u043d\u043e\u0435 \u0434\u0435\u043b\u043e \u2116:", None))
    # retranslateUi

