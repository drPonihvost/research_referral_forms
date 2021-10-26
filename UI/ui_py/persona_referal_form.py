# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'persona_referal_form.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_persona_referal_form(object):
    def setupUi(self, persona_referal_form):
        if not persona_referal_form.objectName():
            persona_referal_form.setObjectName(u"persona_referal_form")
        persona_referal_form.resize(400, 601)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(persona_referal_form.sizePolicy().hasHeightForWidth())
        persona_referal_form.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        persona_referal_form.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(persona_referal_form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(persona_referal_form)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.surname_le = QLineEdit(self.groupBox)
        self.surname_le.setObjectName(u"surname_le")
        self.surname_le.setMinimumSize(QSize(180, 22))

        self.gridLayout.addWidget(self.surname_le, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.name_le = QLineEdit(self.groupBox)
        self.name_le.setObjectName(u"name_le")
        self.name_le.setMinimumSize(QSize(180, 22))

        self.gridLayout.addWidget(self.name_le, 1, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.middle_name_le = QLineEdit(self.groupBox)
        self.middle_name_le.setObjectName(u"middle_name_le")
        self.middle_name_le.setMinimumSize(QSize(180, 22))

        self.gridLayout.addWidget(self.middle_name_le, 2, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.male_rb = QRadioButton(self.groupBox_2)
        self.male_rb.setObjectName(u"male_rb")
        self.male_rb.setChecked(True)

        self.horizontalLayout.addWidget(self.male_rb)

        self.female_rb = QRadioButton(self.groupBox_2)
        self.female_rb.setObjectName(u"female_rb")

        self.horizontalLayout.addWidget(self.female_rb)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.gridLayout.addWidget(self.groupBox_2, 3, 0, 1, 2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.date_of_birth_de = QDateEdit(self.groupBox)
        self.date_of_birth_de.setObjectName(u"date_of_birth_de")
        self.date_of_birth_de.setMinimumSize(QSize(180, 22))

        self.gridLayout.addWidget(self.date_of_birth_de, 4, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)

        self.birthplace_le = QLineEdit(self.groupBox)
        self.birthplace_le.setObjectName(u"birthplace_le")
        self.birthplace_le.setMinimumSize(QSize(180, 22))

        self.gridLayout.addWidget(self.birthplace_le, 5, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.event_gb = QGroupBox(persona_referal_form)
        self.event_gb.setObjectName(u"event_gb")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.event_gb.sizePolicy().hasHeightForWidth())
        self.event_gb.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.event_gb)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ud_rb = QRadioButton(self.event_gb)
        self.ud_rb.setObjectName(u"ud_rb")
        self.ud_rb.setChecked(True)

        self.horizontalLayout_3.addWidget(self.ud_rb)

        self.kusp_rb = QRadioButton(self.event_gb)
        self.kusp_rb.setObjectName(u"kusp_rb")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.kusp_rb.sizePolicy().hasHeightForWidth())
        self.kusp_rb.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.kusp_rb)

        self.req_rb = QRadioButton(self.event_gb)
        self.req_rb.setObjectName(u"req_rb")

        self.horizontalLayout_3.addWidget(self.req_rb)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.event_lo = QVBoxLayout()
        self.event_lo.setObjectName(u"event_lo")

        self.verticalLayout.addLayout(self.event_lo)

        self.plot_te = QTextEdit(self.event_gb)
        self.plot_te.setObjectName(u"plot_te")
        self.plot_te.setMinimumSize(QSize(0, 100))
        self.plot_te.setFocusPolicy(Qt.StrongFocus)

        self.verticalLayout.addWidget(self.plot_te)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.event_gb)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.save_btn = QPushButton(persona_referal_form)
        self.save_btn.setObjectName(u"save_btn")

        self.horizontalLayout_4.addWidget(self.save_btn)

        self.cancel_btn = QPushButton(persona_referal_form)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.horizontalLayout_4.addWidget(self.cancel_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.retranslateUi(persona_referal_form)

        QMetaObject.connectSlotsByName(persona_referal_form)
    # setupUi

    def retranslateUi(self, persona_referal_form):
        persona_referal_form.setWindowTitle(QCoreApplication.translate("persona_referal_form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("persona_referal_form", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u0440\u043e\u0432\u0435\u0440\u044f\u0435\u043c\u043e\u043c \u043b\u0438\u0446\u0435", None))
        self.label.setText(QCoreApplication.translate("persona_referal_form", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("persona_referal_form", u"\u0418\u043c\u044f", None))
        self.label_5.setText(QCoreApplication.translate("persona_referal_form", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("persona_referal_form", u"\u041f\u043e\u043b", None))
        self.male_rb.setText(QCoreApplication.translate("persona_referal_form", u"\u041c\u0443\u0436", None))
        self.female_rb.setText(QCoreApplication.translate("persona_referal_form", u"\u0416\u0435\u043d", None))
        self.label_3.setText(QCoreApplication.translate("persona_referal_form", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.label_4.setText(QCoreApplication.translate("persona_referal_form", u"\u041c\u0435\u0441\u0442\u043e \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.event_gb.setTitle(QCoreApplication.translate("persona_referal_form", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0441\u043e\u0431\u044b\u0442\u0438\u0438", None))
        self.ud_rb.setText(QCoreApplication.translate("persona_referal_form", u"\u0423\u0433\u043e\u043b\u043e\u0432\u043d\u043e\u0435 \u0434\u0435\u043b\u043e", None))
        self.kusp_rb.setText(QCoreApplication.translate("persona_referal_form", u"\u041a\u0423\u0421\u041f", None))
        self.req_rb.setText(QCoreApplication.translate("persona_referal_form", u"\u0422\u0440\u0435\u0431\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.save_btn.setText(QCoreApplication.translate("persona_referal_form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.cancel_btn.setText(QCoreApplication.translate("persona_referal_form", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

