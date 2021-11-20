# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'research_main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QHeaderView,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_research_main_window(object):
    def setupUi(self, research_main_window):
        if not research_main_window.objectName():
            research_main_window.setObjectName(u"research_main_window")
        research_main_window.resize(1024, 768)
        font = QFont()
        font.setPointSize(10)
        research_main_window.setFont(font)
        self.centralwidget = QWidget(research_main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add_person = QPushButton(self.centralwidget)
        self.add_person.setObjectName(u"add_person")
        self.add_person.setMinimumSize(QSize(50, 0))

        self.horizontalLayout.addWidget(self.add_person)

        self.change_pb = QPushButton(self.centralwidget)
        self.change_pb.setObjectName(u"change_pb")

        self.horizontalLayout.addWidget(self.change_pb)

        self.form_pb = QPushButton(self.centralwidget)
        self.form_pb.setObjectName(u"form_pb")

        self.horizontalLayout.addWidget(self.form_pb)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.remember_cb = QCheckBox(self.centralwidget)
        self.remember_cb.setObjectName(u"remember_cb")

        self.horizontalLayout_2.addWidget(self.remember_cb)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.research_person_table_tw = QTableWidget(self.centralwidget)
        if (self.research_person_table_tw.columnCount() < 10):
            self.research_person_table_tw.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.research_person_table_tw.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.research_person_table_tw.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.research_person_table_tw.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.research_person_table_tw.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.research_person_table_tw.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.research_person_table_tw.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.research_person_table_tw.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.research_person_table_tw.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.research_person_table_tw.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.research_person_table_tw.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.research_person_table_tw.setObjectName(u"research_person_table_tw")
        self.research_person_table_tw.setWordWrap(True)
        self.research_person_table_tw.horizontalHeader().setCascadingSectionResizes(False)
        self.research_person_table_tw.horizontalHeader().setMinimumSectionSize(30)
        self.research_person_table_tw.horizontalHeader().setProperty("showSortIndicator", False)
        self.research_person_table_tw.horizontalHeader().setStretchLastSection(False)
        self.research_person_table_tw.verticalHeader().setVisible(False)
        self.research_person_table_tw.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout.addWidget(self.research_person_table_tw)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.addressee_lo = QVBoxLayout()
        self.addressee_lo.setObjectName(u"addressee_lo")

        self.verticalLayout_2.addLayout(self.addressee_lo)

        self.initiator_lo = QVBoxLayout()
        self.initiator_lo.setObjectName(u"initiator_lo")

        self.verticalLayout_2.addLayout(self.initiator_lo)

        self.executor_lo = QVBoxLayout()
        self.executor_lo.setObjectName(u"executor_lo")

        self.verticalLayout_2.addLayout(self.executor_lo)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        research_main_window.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(research_main_window)
        self.statusbar.setObjectName(u"statusbar")
        research_main_window.setStatusBar(self.statusbar)

        self.retranslateUi(research_main_window)

        QMetaObject.connectSlotsByName(research_main_window)
    # setupUi

    def retranslateUi(self, research_main_window):
        research_main_window.setWindowTitle(QCoreApplication.translate("research_main_window", u"MainWindow", None))
        self.add_person.setText(QCoreApplication.translate("research_main_window", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.change_pb.setText(QCoreApplication.translate("research_main_window", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.form_pb.setText(QCoreApplication.translate("research_main_window", u"\u0421\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.remember_cb.setText(QCoreApplication.translate("research_main_window", u"\u0417\u0430\u043f\u043e\u043c\u043d\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        ___qtablewidgetitem = self.research_person_table_tw.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("research_main_window", u"\u2116 \u043f/\u043f", None));
        ___qtablewidgetitem1 = self.research_person_table_tw.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("research_main_window", u"\u0414\u0430\u0442\u0430 \u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f", None));
        ___qtablewidgetitem2 = self.research_person_table_tw.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("research_main_window", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None));
        ___qtablewidgetitem3 = self.research_person_table_tw.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("research_main_window", u"\u0418\u043c\u044f", None));
        ___qtablewidgetitem4 = self.research_person_table_tw.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("research_main_window", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None));
        ___qtablewidgetitem5 = self.research_person_table_tw.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("research_main_window", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None));
        ___qtablewidgetitem6 = self.research_person_table_tw.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("research_main_window", u"\u041c\u0435\u0441\u0442\u043e \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None));
        ___qtablewidgetitem7 = self.research_person_table_tw.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("research_main_window", u"\u041c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u044b", None));
        ___qtablewidgetitem8 = self.research_person_table_tw.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("research_main_window", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u043e", None));
        ___qtablewidgetitem9 = self.research_person_table_tw.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("research_main_window", u"\u0421\u043e\u0431\u044b\u0442\u0438\u0435", None));
    # retranslateUi

