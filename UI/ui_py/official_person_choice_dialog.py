# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'official_person_choice_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_official_person_choice(object):
    def setupUi(self, official_person_choice):
        if not official_person_choice.objectName():
            official_person_choice.setObjectName(u"official_person_choice")
        official_person_choice.resize(857, 307)
        font = QFont()
        font.setPointSize(10)
        official_person_choice.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(official_person_choice)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget = QWidget(official_person_choice)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.official_person_tw = QTableWidget(self.widget)
        if (self.official_person_tw.columnCount() < 5):
            self.official_person_tw.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.official_person_tw.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.official_person_tw.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.official_person_tw.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.official_person_tw.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.official_person_tw.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.official_person_tw.setObjectName(u"official_person_tw")

        self.verticalLayout_4.addWidget(self.official_person_tw)


        self.horizontalLayout_2.addWidget(self.widget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.add_pb = QPushButton(official_person_choice)
        self.add_pb.setObjectName(u"add_pb")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_pb.sizePolicy().hasHeightForWidth())
        self.add_pb.setSizePolicy(sizePolicy)
        self.add_pb.setMinimumSize(QSize(75, 25))
        self.add_pb.setMaximumSize(QSize(100, 25))

        self.verticalLayout.addWidget(self.add_pb)

        self.change_pb = QPushButton(official_person_choice)
        self.change_pb.setObjectName(u"change_pb")
        sizePolicy.setHeightForWidth(self.change_pb.sizePolicy().hasHeightForWidth())
        self.change_pb.setSizePolicy(sizePolicy)
        self.change_pb.setMinimumSize(QSize(75, 25))
        self.change_pb.setMaximumSize(QSize(100, 25))

        self.verticalLayout.addWidget(self.change_pb)

        self.delete_pb = QPushButton(official_person_choice)
        self.delete_pb.setObjectName(u"delete_pb")
        sizePolicy.setHeightForWidth(self.delete_pb.sizePolicy().hasHeightForWidth())
        self.delete_pb.setSizePolicy(sizePolicy)
        self.delete_pb.setMinimumSize(QSize(75, 25))
        self.delete_pb.setMaximumSize(QSize(100, 25))

        self.verticalLayout.addWidget(self.delete_pb)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.select_pb = QPushButton(official_person_choice)
        self.select_pb.setObjectName(u"select_pb")

        self.horizontalLayout.addWidget(self.select_pb)

        self.cancel_pb = QPushButton(official_person_choice)
        self.cancel_pb.setObjectName(u"cancel_pb")

        self.horizontalLayout.addWidget(self.cancel_pb)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        QWidget.setTabOrder(self.select_pb, self.cancel_pb)

        self.retranslateUi(official_person_choice)

        QMetaObject.connectSlotsByName(official_person_choice)
    # setupUi

    def retranslateUi(self, official_person_choice):
        official_person_choice.setWindowTitle(QCoreApplication.translate("official_person_choice", u"Dialog", None))
        ___qtablewidgetitem = self.official_person_tw.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("official_person_choice", u"id", None));
        ___qtablewidgetitem1 = self.official_person_tw.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("official_person_choice", u"\u0424\u0418\u041e", None));
        ___qtablewidgetitem2 = self.official_person_tw.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("official_person_choice", u"\u0414\u0435\u043f\u0430\u0440\u0442\u0430\u043c\u0435\u043d\u0442", None));
        ___qtablewidgetitem3 = self.official_person_tw.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("official_person_choice", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None));
        ___qtablewidgetitem4 = self.official_person_tw.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("official_person_choice", u"\u0421\u043f\u0435\u0446. \u0437\u0432\u0430\u043d\u0438\u0435", None));
        self.add_pb.setText(QCoreApplication.translate("official_person_choice", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.change_pb.setText(QCoreApplication.translate("official_person_choice", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.delete_pb.setText(QCoreApplication.translate("official_person_choice", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.select_pb.setText(QCoreApplication.translate("official_person_choice", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.cancel_pb.setText(QCoreApplication.translate("official_person_choice", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi

