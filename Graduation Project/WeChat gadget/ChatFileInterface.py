# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChatFileInterface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Interface_File(object):
    def setupUi(self, Interface_File):
        Interface_File.setObjectName("Interface_File")
        Interface_File.resize(900, 600)
        self.NavigationBar = QtWidgets.QWidget(Interface_File)
        self.NavigationBar.setGeometry(QtCore.QRect(0, 0, 901, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NavigationBar.sizePolicy().hasHeightForWidth())
        self.NavigationBar.setSizePolicy(sizePolicy)
        self.NavigationBar.setMinimumSize(QtCore.QSize(0, 41))
        self.NavigationBar.setObjectName("NavigationBar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.NavigationBar)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_back = QtWidgets.QPushButton(self.NavigationBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_back.sizePolicy().hasHeightForWidth())
        self.button_back.setSizePolicy(sizePolicy)
        self.button_back.setMaximumSize(QtCore.QSize(41, 41))
        self.button_back.setObjectName("button_back")
        self.horizontalLayout_2.addWidget(self.button_back)
        self.titleText = QtWidgets.QLabel(self.NavigationBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleText.sizePolicy().hasHeightForWidth())
        self.titleText.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.titleText.setFont(font)
        self.titleText.setObjectName("titleText")
        self.horizontalLayout_2.addWidget(self.titleText)
        self.gap = QtWidgets.QFrame(self.NavigationBar)
        self.gap.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gap.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gap.setObjectName("gap")
        self.horizontalLayout_2.addWidget(self.gap)
        self.FormControl = QtWidgets.QFrame(self.NavigationBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FormControl.sizePolicy().hasHeightForWidth())
        self.FormControl.setSizePolicy(sizePolicy)
        self.FormControl.setMaximumSize(QtCore.QSize(125, 16777215))
        self.FormControl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FormControl.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FormControl.setLineWidth(0)
        self.FormControl.setObjectName("FormControl")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.FormControl)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_minimize = QtWidgets.QPushButton(self.FormControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_minimize.sizePolicy().hasHeightForWidth())
        self.button_minimize.setSizePolicy(sizePolicy)
        self.button_minimize.setText("")
        self.button_minimize.setObjectName("button_minimize")
        self.horizontalLayout.addWidget(self.button_minimize)
        self.button_maximize = QtWidgets.QPushButton(self.FormControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_maximize.sizePolicy().hasHeightForWidth())
        self.button_maximize.setSizePolicy(sizePolicy)
        self.button_maximize.setText("")
        self.button_maximize.setObjectName("button_maximize")
        self.horizontalLayout.addWidget(self.button_maximize)
        self.button_close = QtWidgets.QPushButton(self.FormControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_close.sizePolicy().hasHeightForWidth())
        self.button_close.setSizePolicy(sizePolicy)
        self.button_close.setText("")
        self.button_close.setObjectName("button_close")
        self.horizontalLayout.addWidget(self.button_close)
        self.horizontalLayout_2.addWidget(self.FormControl)
        self.ToolsBar = QtWidgets.QFrame(Interface_File)
        self.ToolsBar.setGeometry(QtCore.QRect(0, 40, 901, 43))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToolsBar.sizePolicy().hasHeightForWidth())
        self.ToolsBar.setSizePolicy(sizePolicy)
        self.ToolsBar.setMinimumSize(QtCore.QSize(0, 43))
        self.ToolsBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ToolsBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ToolsBar.setObjectName("ToolsBar")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.ToolsBar)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.button_search = QtWidgets.QPushButton(self.ToolsBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_search.sizePolicy().hasHeightForWidth())
        self.button_search.setSizePolicy(sizePolicy)
        self.button_search.setMaximumSize(QtCore.QSize(61, 41))
        self.button_search.setObjectName("button_search")
        self.horizontalLayout_4.addWidget(self.button_search)
        self.DateBar = QtWidgets.QFrame(self.ToolsBar)
        self.DateBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DateBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DateBar.setObjectName("DateBar")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.DateBar)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gap1 = QtWidgets.QFrame(self.DateBar)
        self.gap1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gap1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gap1.setObjectName("gap1")
        self.horizontalLayout_3.addWidget(self.gap1)
        self.lineEdit_year = QtWidgets.QLineEdit(self.DateBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_year.sizePolicy().hasHeightForWidth())
        self.lineEdit_year.setSizePolicy(sizePolicy)
        self.lineEdit_year.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_year.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_year.setObjectName("lineEdit_year")
        self.horizontalLayout_3.addWidget(self.lineEdit_year)
        self.line_2 = QtWidgets.QFrame(self.DateBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setMinimumSize(QtCore.QSize(15, 0))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_3.addWidget(self.line_2)
        self.lineEdit_month = QtWidgets.QLineEdit(self.DateBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_month.sizePolicy().hasHeightForWidth())
        self.lineEdit_month.setSizePolicy(sizePolicy)
        self.lineEdit_month.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_month.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_month.setObjectName("lineEdit_month")
        self.horizontalLayout_3.addWidget(self.lineEdit_month)
        self.line_3 = QtWidgets.QFrame(self.DateBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy)
        self.line_3.setMinimumSize(QtCore.QSize(15, 0))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_3.addWidget(self.line_3)
        self.lineEdit_day = QtWidgets.QLineEdit(self.DateBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_day.sizePolicy().hasHeightForWidth())
        self.lineEdit_day.setSizePolicy(sizePolicy)
        self.lineEdit_day.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_day.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_day.setObjectName("lineEdit_day")
        self.horizontalLayout_3.addWidget(self.lineEdit_day)
        self.gap2 = QtWidgets.QFrame(self.DateBar)
        self.gap2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gap2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gap2.setObjectName("gap2")
        self.horizontalLayout_3.addWidget(self.gap2)
        self.horizontalLayout_4.addWidget(self.DateBar)
        self.button_filter = QtWidgets.QPushButton(self.ToolsBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_filter.sizePolicy().hasHeightForWidth())
        self.button_filter.setSizePolicy(sizePolicy)
        self.button_filter.setMaximumSize(QtCore.QSize(61, 41))
        self.button_filter.setObjectName("button_filter")
        self.horizontalLayout_4.addWidget(self.button_filter)
        self.FileShowArea = QtWidgets.QScrollArea(Interface_File)
        self.FileShowArea.setGeometry(QtCore.QRect(0, 80, 901, 521))
        self.FileShowArea.setWidgetResizable(True)
        self.FileShowArea.setObjectName("FileShowArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 899, 519))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.FileShowArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Interface_File)
        QtCore.QMetaObject.connectSlotsByName(Interface_File)

    def retranslateUi(self, Interface_File):
        _translate = QtCore.QCoreApplication.translate
        Interface_File.setWindowTitle(_translate("Interface_File", "聊天文件"))
        self.button_back.setText(_translate("Interface_File", "<"))
        self.titleText.setText(_translate("Interface_File", "聊天文件"))
        self.button_search.setText(_translate("Interface_File", "搜索"))
        self.lineEdit_year.setText(_translate("Interface_File", "2024"))
        self.lineEdit_month.setText(_translate("Interface_File", "03"))
        self.lineEdit_day.setText(_translate("Interface_File", "01"))
        self.button_filter.setText(_translate("Interface_File", "按日"))
