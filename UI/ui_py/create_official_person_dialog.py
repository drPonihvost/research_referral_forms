# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_official_person_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_create_official_person_dialog(object):
    def setupUi(self, create_official_person_dialog):
        if not create_official_person_dialog.objectName():
            create_official_person_dialog.setObjectName(u"create_official_person_dialog")
        create_official_person_dialog.resize(403, 278)
        font = QFont()
        font.setPointSize(10)
        create_official_person_dialog.setFont(font)
        self.verticalLayout = QVBoxLayout(create_official_person_dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.create_official_person_widget = QWidget(create_official_person_dialog)
        self.create_official_person_widget.setObjectName(u"create_official_person_widget")
        self.verticalLayout_2 = QVBoxLayout(self.create_official_person_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label = QLabel(self.create_official_person_widget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.create_official_person_widget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.create_official_person_widget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.rank_le = QLineEdit(self.create_official_person_widget)
        self.rank_le.setObjectName(u"rank_le")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.rank_le)

        self.label_4 = QLabel(self.create_official_person_widget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.name_le = QLineEdit(self.create_official_person_widget)
        self.name_le.setObjectName(u"name_le")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.name_le)

        self.department_te = QTextEdit(self.create_official_person_widget)
        self.department_te.setObjectName(u"department_te")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.department_te)

        self.post_te = QTextEdit(self.create_official_person_widget)
        self.post_te.setObjectName(u"post_te")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.post_te)


        self.verticalLayout_2.addLayout(self.formLayout)


        self.verticalLayout.addWidget(self.create_official_person_widget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.accept_pb = QPushButton(create_official_person_dialog)
        self.accept_pb.setObjectName(u"accept_pb")

        self.horizontalLayout.addWidget(self.accept_pb)

        self.cancel_pb = QPushButton(create_official_person_dialog)
        self.cancel_pb.setObjectName(u"cancel_pb")

        self.horizontalLayout.addWidget(self.cancel_pb)


        self.verticalLayout.addLayout(self.horizontalLayout)

        QWidget.setTabOrder(self.department_te, self.post_te)
        QWidget.setTabOrder(self.post_te, self.rank_le)
        QWidget.setTabOrder(self.rank_le, self.name_le)
        QWidget.setTabOrder(self.name_le, self.accept_pb)
        QWidget.setTabOrder(self.accept_pb, self.cancel_pb)

        self.retranslateUi(create_official_person_dialog)

        QMetaObject.connectSlotsByName(create_official_person_dialog)
    # setupUi

    def retranslateUi(self, create_official_person_dialog):
        create_official_person_dialog.setWindowTitle(QCoreApplication.translate("create_official_person_dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("create_official_person_dialog", u"\u0414\u0435\u043f\u0430\u0440\u0442\u0430\u043c\u0435\u043d\u0442:", None))
        self.label_2.setText(QCoreApplication.translate("create_official_person_dialog", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c:", None))
        self.label_3.setText(QCoreApplication.translate("create_official_person_dialog", u"\u0421\u043f\u0435\u0446. \u0437\u0432\u0430\u043d\u0438\u0435:", None))
        self.label_4.setText(QCoreApplication.translate("create_official_person_dialog", u"\u0424\u0418\u041e:", None))
        self.accept_pb.setText(QCoreApplication.translate("create_official_person_dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.cancel_pb.setText(QCoreApplication.translate("create_official_person_dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

