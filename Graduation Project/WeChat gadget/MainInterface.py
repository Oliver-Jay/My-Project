# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainInterface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Interface_Main(object):
    def setupUi(self, Interface_Main):
        Interface_Main.setObjectName("Interface_Main")
        Interface_Main.resize(900, 600)
        self.DataShow = QtWidgets.QWidget(Interface_Main)
        self.DataShow.setGeometry(QtCore.QRect(0, 40, 901, 241))
        self.DataShow.setObjectName("DataShow")
        self.label1 = QtWidgets.QLabel(self.DataShow)
        self.label1.setGeometry(QtCore.QRect(370, 10, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label1.setFont(font)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label1")
        self.progressBar = QtWidgets.QProgressBar(self.DataShow)
        self.progressBar.setGeometry(QtCore.QRect(170, 130, 571, 31))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.GdataShow = QtWidgets.QFrame(self.DataShow)
        self.GdataShow.setGeometry(QtCore.QRect(400, 40, 91, 31))
        self.GdataShow.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.GdataShow.setFrameShadow(QtWidgets.QFrame.Raised)
        self.GdataShow.setObjectName("GdataShow")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.GdataShow)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_Gdata = QtWidgets.QLabel(self.GdataShow)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_Gdata.setFont(font)
        self.label_Gdata.setStyleSheet("color: rgb(6, 176, 37);")
        self.label_Gdata.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Gdata.setObjectName("label_Gdata")
        self.horizontalLayout_3.addWidget(self.label_Gdata)
        self.label_G = QtWidgets.QLabel(self.GdataShow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_G.sizePolicy().hasHeightForWidth())
        self.label_G.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_G.setFont(font)
        self.label_G.setAlignment(QtCore.Qt.AlignCenter)
        self.label_G.setObjectName("label_G")
        self.horizontalLayout_3.addWidget(self.label_G)
        self.PercentShow = QtWidgets.QFrame(self.DataShow)
        self.PercentShow.setGeometry(QtCore.QRect(340, 80, 241, 31))
        self.PercentShow.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PercentShow.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PercentShow.setObjectName("PercentShow")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.PercentShow)
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label2 = QtWidgets.QLabel(self.PercentShow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label2.sizePolicy().hasHeightForWidth())
        self.label2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label2.setFont(font)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label2")
        self.horizontalLayout_4.addWidget(self.label2)
        self.label_percent = QtWidgets.QLabel(self.PercentShow)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_percent.setFont(font)
        self.label_percent.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_percent.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_percent.setObjectName("label_percent")
        self.horizontalLayout_4.addWidget(self.label_percent)
        self.label_Psymbol = QtWidgets.QLabel(self.PercentShow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Psymbol.sizePolicy().hasHeightForWidth())
        self.label_Psymbol.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_Psymbol.setFont(font)
        self.label_Psymbol.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Psymbol.setObjectName("label_Psymbol")
        self.horizontalLayout_4.addWidget(self.label_Psymbol)
        self.Legend = QtWidgets.QFrame(self.DataShow)
        self.Legend.setGeometry(QtCore.QRect(250, 160, 381, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Legend.sizePolicy().hasHeightForWidth())
        self.Legend.setSizePolicy(sizePolicy)
        self.Legend.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Legend.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Legend.setObjectName("Legend")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.Legend)
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.legend1 = QtWidgets.QFrame(self.Legend)
        self.legend1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.legend1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.legend1.setObjectName("legend1")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.legend1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.color1 = QtWidgets.QLabel(self.legend1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.color1.sizePolicy().hasHeightForWidth())
        self.color1.setSizePolicy(sizePolicy)
        self.color1.setStyleSheet("background-color: rgb(6, 176, 37);")
        self.color1.setText("")
        self.color1.setObjectName("color1")
        self.horizontalLayout_5.addWidget(self.color1)
        self.label_l1 = QtWidgets.QLabel(self.legend1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_l1.sizePolicy().hasHeightForWidth())
        self.label_l1.setSizePolicy(sizePolicy)
        self.label_l1.setObjectName("label_l1")
        self.horizontalLayout_5.addWidget(self.label_l1)
        self.horizontalLayout_8.addWidget(self.legend1)
        self.legend2 = QtWidgets.QFrame(self.Legend)
        self.legend2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.legend2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.legend2.setObjectName("legend2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.legend2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.color2 = QtWidgets.QLabel(self.legend2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.color2.sizePolicy().hasHeightForWidth())
        self.color2.setSizePolicy(sizePolicy)
        self.color2.setStyleSheet("background-color: rgb(208, 208, 208);")
        self.color2.setText("")
        self.color2.setObjectName("color2")
        self.horizontalLayout_6.addWidget(self.color2)
        self.label_l2 = QtWidgets.QLabel(self.legend2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_l2.sizePolicy().hasHeightForWidth())
        self.label_l2.setSizePolicy(sizePolicy)
        self.label_l2.setObjectName("label_l2")
        self.horizontalLayout_6.addWidget(self.label_l2)
        self.horizontalLayout_8.addWidget(self.legend2)
        self.legend3 = QtWidgets.QFrame(self.Legend)
        self.legend3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.legend3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.legend3.setObjectName("legend3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.legend3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.color3 = QtWidgets.QLabel(self.legend3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.color3.sizePolicy().hasHeightForWidth())
        self.color3.setSizePolicy(sizePolicy)
        self.color3.setStyleSheet("background-color: rgb(254, 254, 254);")
        self.color3.setText("")
        self.color3.setObjectName("color3")
        self.horizontalLayout_7.addWidget(self.color3)
        self.label_l3 = QtWidgets.QLabel(self.legend3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_l3.sizePolicy().hasHeightForWidth())
        self.label_l3.setSizePolicy(sizePolicy)
        self.label_l3.setObjectName("label_l3")
        self.horizontalLayout_7.addWidget(self.label_l3)
        self.horizontalLayout_8.addWidget(self.legend3)
        self.FuctionArea = QtWidgets.QWidget(Interface_Main)
        self.FuctionArea.setGeometry(QtCore.QRect(0, 279, 901, 321))
        self.FuctionArea.setObjectName("FuctionArea")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.FuctionArea)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pictureArea = QtWidgets.QFrame(self.FuctionArea)
        self.pictureArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pictureArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pictureArea.setObjectName("pictureArea")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.pictureArea)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_picture = QtWidgets.QPushButton(self.pictureArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_picture.sizePolicy().hasHeightForWidth())
        self.button_picture.setSizePolicy(sizePolicy)
        self.button_picture.setText("")
        self.button_picture.setObjectName("button_picture")
        self.verticalLayout.addWidget(self.button_picture)
        self.label_picture = QtWidgets.QLabel(self.pictureArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_picture.sizePolicy().hasHeightForWidth())
        self.label_picture.setSizePolicy(sizePolicy)
        self.label_picture.setAlignment(QtCore.Qt.AlignCenter)
        self.label_picture.setObjectName("label_picture")
        self.verticalLayout.addWidget(self.label_picture)
        self.horizontalLayout_2.addWidget(self.pictureArea)
        self.fileArea = QtWidgets.QFrame(self.FuctionArea)
        self.fileArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fileArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fileArea.setObjectName("fileArea")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fileArea)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.button_file = QtWidgets.QPushButton(self.fileArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_file.sizePolicy().hasHeightForWidth())
        self.button_file.setSizePolicy(sizePolicy)
        self.button_file.setText("")
        self.button_file.setObjectName("button_file")
        self.verticalLayout_2.addWidget(self.button_file)
        self.label_file = QtWidgets.QLabel(self.fileArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_file.sizePolicy().hasHeightForWidth())
        self.label_file.setSizePolicy(sizePolicy)
        self.label_file.setAlignment(QtCore.Qt.AlignCenter)
        self.label_file.setObjectName("label_file")
        self.verticalLayout_2.addWidget(self.label_file)
        self.horizontalLayout_2.addWidget(self.fileArea)
        self.videoArea = QtWidgets.QFrame(self.FuctionArea)
        self.videoArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.videoArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.videoArea.setObjectName("videoArea")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.videoArea)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.button_video = QtWidgets.QPushButton(self.videoArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_video.sizePolicy().hasHeightForWidth())
        self.button_video.setSizePolicy(sizePolicy)
        self.button_video.setText("")
        self.button_video.setObjectName("button_video")
        self.verticalLayout_3.addWidget(self.button_video)
        self.label_video = QtWidgets.QLabel(self.videoArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_video.sizePolicy().hasHeightForWidth())
        self.label_video.setSizePolicy(sizePolicy)
        self.label_video.setAlignment(QtCore.Qt.AlignCenter)
        self.label_video.setObjectName("label_video")
        self.verticalLayout_3.addWidget(self.label_video)
        self.horizontalLayout_2.addWidget(self.videoArea)
        self.autoArea = QtWidgets.QFrame(self.FuctionArea)
        self.autoArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.autoArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.autoArea.setObjectName("autoArea")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.autoArea)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.button_auto = QtWidgets.QPushButton(self.autoArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_auto.sizePolicy().hasHeightForWidth())
        self.button_auto.setSizePolicy(sizePolicy)
        self.button_auto.setText("")
        self.button_auto.setObjectName("button_auto")
        self.verticalLayout_4.addWidget(self.button_auto)
        self.label_auto = QtWidgets.QLabel(self.autoArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_auto.sizePolicy().hasHeightForWidth())
        self.label_auto.setSizePolicy(sizePolicy)
        self.label_auto.setAlignment(QtCore.Qt.AlignCenter)
        self.label_auto.setObjectName("label_auto")
        self.verticalLayout_4.addWidget(self.label_auto)
        self.horizontalLayout_2.addWidget(self.autoArea)
        self.NavigationBar = QtWidgets.QWidget(Interface_Main)
        self.NavigationBar.setGeometry(QtCore.QRect(0, 0, 901, 41))
        self.NavigationBar.setObjectName("NavigationBar")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.NavigationBar)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.ProfilePhoto = QtWidgets.QLabel(self.NavigationBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProfilePhoto.sizePolicy().hasHeightForWidth())
        self.ProfilePhoto.setSizePolicy(sizePolicy)
        self.ProfilePhoto.setMaximumSize(QtCore.QSize(41, 41))
        self.ProfilePhoto.setAlignment(QtCore.Qt.AlignCenter)
        self.ProfilePhoto.setObjectName("ProfilePhoto")
        self.horizontalLayout_9.addWidget(self.ProfilePhoto)
        self.gap = QtWidgets.QFrame(self.NavigationBar)
        self.gap.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gap.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gap.setObjectName("gap")
        self.horizontalLayout_9.addWidget(self.gap)
        self.FormControl_2 = QtWidgets.QFrame(self.NavigationBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FormControl_2.sizePolicy().hasHeightForWidth())
        self.FormControl_2.setSizePolicy(sizePolicy)
        self.FormControl_2.setMaximumSize(QtCore.QSize(125, 16777215))
        self.FormControl_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FormControl_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FormControl_2.setLineWidth(0)
        self.FormControl_2.setObjectName("FormControl_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.FormControl_2)
        self.horizontalLayout_10.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.button_minimize_2 = QtWidgets.QPushButton(self.FormControl_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_minimize_2.sizePolicy().hasHeightForWidth())
        self.button_minimize_2.setSizePolicy(sizePolicy)
        self.button_minimize_2.setText("")
        self.button_minimize_2.setObjectName("button_minimize_2")
        self.horizontalLayout_10.addWidget(self.button_minimize_2)
        self.button_maximize_2 = QtWidgets.QPushButton(self.FormControl_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_maximize_2.sizePolicy().hasHeightForWidth())
        self.button_maximize_2.setSizePolicy(sizePolicy)
        self.button_maximize_2.setText("")
        self.button_maximize_2.setObjectName("button_maximize_2")
        self.horizontalLayout_10.addWidget(self.button_maximize_2)
        self.button_close_2 = QtWidgets.QPushButton(self.FormControl_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_close_2.sizePolicy().hasHeightForWidth())
        self.button_close_2.setSizePolicy(sizePolicy)
        self.button_close_2.setText("")
        self.button_close_2.setObjectName("button_close_2")
        self.horizontalLayout_10.addWidget(self.button_close_2)
        self.horizontalLayout_9.addWidget(self.FormControl_2)

        self.retranslateUi(Interface_Main)
        QtCore.QMetaObject.connectSlotsByName(Interface_Main)

    def retranslateUi(self, Interface_Main):
        _translate = QtCore.QCoreApplication.translate
        Interface_Main.setWindowTitle(_translate("Interface_Main", "WeChat Gadget"))
        self.label1.setText(_translate("Interface_Main", "微信已用空间"))
        self.label_Gdata.setText(_translate("Interface_Main", "20"))
        self.label_G.setText(_translate("Interface_Main", "G"))
        self.label2.setText(_translate("Interface_Main", "占据电脑存储"))
        self.label_percent.setText(_translate("Interface_Main", "24"))
        self.label_Psymbol.setText(_translate("Interface_Main", "%"))
        self.label_l1.setText(_translate("Interface_Main", "微信已用空间"))
        self.label_l2.setText(_translate("Interface_Main", "电脑已用空间"))
        self.label_l3.setText(_translate("Interface_Main", "电脑可用空间"))
        self.label_picture.setText(_translate("Interface_Main", "聊天图片"))
        self.label_file.setText(_translate("Interface_Main", "聊天文件"))
        self.label_video.setText(_translate("Interface_Main", "聊天视频"))
        self.label_auto.setText(_translate("Interface_Main", "自动保存"))
        self.ProfilePhoto.setText(_translate("Interface_Main", "头像"))
