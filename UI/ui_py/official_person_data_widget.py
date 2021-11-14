# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'official_person_data_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_official_person_data(object):
    def setupUi(self, official_person_data):
        if not official_person_data.objectName():
            official_person_data.setObjectName(u"official_person_data")
        official_person_data.resize(320, 304)
        font = QFont()
        font.setPointSize(10)
        official_person_data.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(official_person_data)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.oficial_person_lb = QLabel(official_person_data)
        self.oficial_person_lb.setObjectName(u"oficial_person_lb")
        self.oficial_person_lb.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.oficial_person_lb)

        self.acting_cb = QCheckBox(official_person_data)
        self.acting_cb.setObjectName(u"acting_cb")

        self.verticalLayout.addWidget(self.acting_cb)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.label = QLabel(official_person_data)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(official_person_data)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(official_person_data)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.rank_le = QLineEdit(official_person_data)
        self.rank_le.setObjectName(u"rank_le")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rank_le.sizePolicy().hasHeightForWidth())
        self.rank_le.setSizePolicy(sizePolicy)
        self.rank_le.setMaximumSize(QSize(150, 21))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.rank_le)

        self.label_4 = QLabel(official_person_data)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.name_le = QLineEdit(official_person_data)
        self.name_le.setObjectName(u"name_le")
        sizePolicy.setHeightForWidth(self.name_le.sizePolicy().hasHeightForWidth())
        self.name_le.setSizePolicy(sizePolicy)
        self.name_le.setMaximumSize(QSize(150, 21))

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.name_le)

        self.department_te = QTextEdit(official_person_data)
        self.department_te.setObjectName(u"department_te")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.department_te.sizePolicy().hasHeightForWidth())
        self.department_te.setSizePolicy(sizePolicy1)
        self.department_te.setMaximumSize(QSize(209, 73))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.department_te)

        self.post_te = QTextEdit(official_person_data)
        self.post_te.setObjectName(u"post_te")
        sizePolicy1.setHeightForWidth(self.post_te.sizePolicy().hasHeightForWidth())
        self.post_te.setSizePolicy(sizePolicy1)
        self.post_te.setMaximumSize(QSize(209, 74))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.post_te)


        self.verticalLayout.addLayout(self.formLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.choice_pb = QPushButton(official_person_data)
        self.choice_pb.setObjectName(u"choice_pb")

        self.horizontalLayout.addWidget(self.choice_pb)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(official_person_data)

        QMetaObject.connectSlotsByName(official_person_data)
    # setupUi

    def retranslateUi(self, official_person_data):
        official_person_data.setWindowTitle(QCoreApplication.translate("official_person_data", u"Form", None))
        self.oficial_person_lb.setText("")
        self.acting_cb.setText(QCoreApplication.translate("official_person_data", u"\u0412\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.label.setText(QCoreApplication.translate("official_person_data", u"\u0414\u0435\u043f\u0435\u0440\u0442\u0430\u043c\u0435\u043d\u0442:", None))
        self.label_2.setText(QCoreApplication.translate("official_person_data", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c:", None))
        self.label_3.setText(QCoreApplication.translate("official_person_data", u"\u0421\u043f\u0435\u0446. \u0437\u0432\u0430\u043d\u0438\u0435:", None))
        self.label_4.setText(QCoreApplication.translate("official_person_data", u"\u0424\u0418\u041e:", None))
        self.choice_pb.setText(QCoreApplication.translate("official_person_data", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
    # retranslateUi

