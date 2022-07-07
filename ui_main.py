# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1156, 700)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenuBg.sizePolicy().hasHeightForWidth())
        self.leftMenuBg.setSizePolicy(sizePolicy)
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setStyleSheet(u"background-image: url(:/icons/resources/icons/brand_logo.png);")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy1)
        self.toggleButton.setMinimumSize(QSize(0, 50))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/resources/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy1.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy1)
        self.btn_home.setMinimumSize(QSize(0, 50))
        self.btn_home.setBaseSize(QSize(0, 0))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/resources/icons/icons8-home-24.png);\n"
"")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_attendance = QPushButton(self.topMenu)
        self.btn_attendance.setObjectName(u"btn_attendance")
        sizePolicy1.setHeightForWidth(self.btn_attendance.sizePolicy().hasHeightForWidth())
        self.btn_attendance.setSizePolicy(sizePolicy1)
        self.btn_attendance.setMinimumSize(QSize(0, 50))
        self.btn_attendance.setFont(font)
        self.btn_attendance.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_attendance.setLayoutDirection(Qt.LeftToRight)
        self.btn_attendance.setStyleSheet(u"background-image: url(:/icons/resources/icons/icons8-true-false-24.png);")

        self.verticalLayout_8.addWidget(self.btn_attendance)

        self.btn_register = QPushButton(self.topMenu)
        self.btn_register.setObjectName(u"btn_register")
        sizePolicy1.setHeightForWidth(self.btn_register.sizePolicy().hasHeightForWidth())
        self.btn_register.setSizePolicy(sizePolicy1)
        self.btn_register.setMinimumSize(QSize(0, 50))
        self.btn_register.setFont(font)
        self.btn_register.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_register.setLayoutDirection(Qt.LeftToRight)
        self.btn_register.setStyleSheet(u"background-image: url(:/icons/resources/icons/icons8-facial-recognition-24.png);")

        self.verticalLayout_8.addWidget(self.btn_register)

        self.btn_training = QPushButton(self.topMenu)
        self.btn_training.setObjectName(u"btn_training")
        sizePolicy1.setHeightForWidth(self.btn_training.sizePolicy().hasHeightForWidth())
        self.btn_training.setSizePolicy(sizePolicy1)
        self.btn_training.setMinimumSize(QSize(0, 50))
        self.btn_training.setStyleSheet(u"background-image: url(:/icons/resources/icons/icons8-bot-24.png);")

        self.verticalLayout_8.addWidget(self.btn_training)

        self.btn_report = QPushButton(self.topMenu)
        self.btn_report.setObjectName(u"btn_report")
        sizePolicy1.setHeightForWidth(self.btn_report.sizePolicy().hasHeightForWidth())
        self.btn_report.setSizePolicy(sizePolicy1)
        self.btn_report.setMinimumSize(QSize(0, 50))
        self.btn_report.setFont(font)
        self.btn_report.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_report.setLayoutDirection(Qt.LeftToRight)
        self.btn_report.setStyleSheet(u"background-image: url(:/icons/resources/icons/icons8-graph-report-24.png);")

        self.verticalLayout_8.addWidget(self.btn_report)

        self.btn_attendance.raise_()
        self.btn_register.raise_()
        self.btn_report.raise_()
        self.btn_training.raise_()
        self.btn_home.raise_()

        self.verticalMenuLayout.addWidget(self.topMenu)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.title_left_box = QFrame(self.contentTopBg)
        self.title_left_box.setObjectName(u"title_left_box")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.title_left_box.sizePolicy().hasHeightForWidth())
        self.title_left_box.setSizePolicy(sizePolicy2)
        self.title_left_box.setFrameShape(QFrame.NoFrame)
        self.title_left_box.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.title_left_box)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.title_info = QLabel(self.title_left_box)
        self.title_info.setObjectName(u"title_info")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.title_info.sizePolicy().hasHeightForWidth())
        self.title_info.setSizePolicy(sizePolicy3)
        self.title_info.setMaximumSize(QSize(16777215, 45))
        font3 = QFont()
        font3.setFamilies([u"Segoe Print"])
        font3.setPointSize(15)
        font3.setBold(True)
        font3.setItalic(False)
        self.title_info.setFont(font3)
        self.title_info.setStyleSheet(u"font: 700 15pt \"Segoe Print\";")
        self.title_info.setTextFormat(Qt.AutoText)
        self.title_info.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.title_info)


        self.horizontalLayout.addWidget(self.title_left_box)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimizeAppBtn.setStyleSheet(u"background-image: url(:/icons/resources/icons/cil-window-minimize.png);\n"
"background-repeat:no-repeat;\n"
"background-position:center;")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font4)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.maximizeRestoreAppBtn.setStyleSheet(u"background-image: url(:/icons/resources/icons/cil-window-restore.png);\n"
"background-repeat:no-repeat;\n"
"background-position:center;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon1)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setStyleSheet(u"background-image: url(:/icons/resources/icons/cil-x.png);\n"
"background-repeat:no-repeat;\n"
"background-position:center;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon2)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home_panel = QWidget()
        self.home_panel.setObjectName(u"home_panel")
        self.home_panel.setAutoFillBackground(False)
        self.home_panel.setStyleSheet(u"")
        self.verticalLayout_14 = QVBoxLayout(self.home_panel)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.home_base_frame = QFrame(self.home_panel)
        self.home_base_frame.setObjectName(u"home_base_frame")
        self.home_base_frame.setStyleSheet(u"")
        self.home_base_frame.setFrameShape(QFrame.StyledPanel)
        self.home_base_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.home_base_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.home_left_frame = QFrame(self.home_base_frame)
        self.home_left_frame.setObjectName(u"home_left_frame")
        self.home_left_frame.setStyleSheet(u"background:none;")
        self.home_left_frame.setFrameShape(QFrame.StyledPanel)
        self.home_left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.home_left_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.home_title_label = QLabel(self.home_left_frame)
        self.home_title_label.setObjectName(u"home_title_label")
        self.home_title_label.setMinimumSize(QSize(100, 0))
        self.home_title_label.setStyleSheet(u"QLabel{\n"
"font:700 16pt \"Segoe Print\";\n"
"word-wrap: break-word;\n"
"}")
        self.home_title_label.setTextFormat(Qt.AutoText)
        self.home_title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.home_title_label)


        self.horizontalLayout_7.addWidget(self.home_left_frame)

        self.home_bg_frame = QFrame(self.home_base_frame)
        self.home_bg_frame.setObjectName(u"home_bg_frame")
        self.home_bg_frame.setMinimumSize(QSize(400, 0))
        self.home_bg_frame.setStyleSheet(u"background-image: url(:/images/resources/images/face.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"background-size:contain;")
        self.home_bg_frame.setFrameShape(QFrame.StyledPanel)
        self.home_bg_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.home_bg_frame)


        self.verticalLayout_14.addWidget(self.home_base_frame)

        self.stackedWidget.addWidget(self.home_panel)
        self.training_panel = QWidget()
        self.training_panel.setObjectName(u"training_panel")
        self.gridLayout_5 = QGridLayout(self.training_panel)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.training_heading = QLabel(self.training_panel)
        self.training_heading.setObjectName(u"training_heading")
        self.training_heading.setStyleSheet(u"font: 700 15pt \"Segoe Print\";")
        self.training_heading.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.training_heading, 0, 0, 1, 1, Qt.AlignTop)

        self.training_base_frame = QFrame(self.training_panel)
        self.training_base_frame.setObjectName(u"training_base_frame")
        sizePolicy3.setHeightForWidth(self.training_base_frame.sizePolicy().hasHeightForWidth())
        self.training_base_frame.setSizePolicy(sizePolicy3)
        self.training_base_frame.setFrameShape(QFrame.StyledPanel)
        self.training_base_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.training_base_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.training_left_frame = QFrame(self.training_base_frame)
        self.training_left_frame.setObjectName(u"training_left_frame")
        self.training_left_frame.setMinimumSize(QSize(350, 300))
        self.training_left_frame.setFrameShape(QFrame.StyledPanel)
        self.training_left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.training_left_frame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.start_training_button = QPushButton(self.training_left_frame)
        self.start_training_button.setObjectName(u"start_training_button")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.start_training_button.sizePolicy().hasHeightForWidth())
        self.start_training_button.setSizePolicy(sizePolicy4)
        self.start_training_button.setMinimumSize(QSize(200, 200))
        self.start_training_button.setMaximumSize(QSize(200, 200))
        self.start_training_button.setBaseSize(QSize(200, 200))
        self.start_training_button.setStyleSheet(u"QPushButton{\n"
"    display: inline-block;\n"
"	text-shadow: 2px 2px #bd93f9;\n"
"	background: #44475a;\n"
"    color: #85e3fc;\n"
"    width: 200px;\n"
"    height: 200px;\n"
"    line-height: 200px;\n"
"    border-radius: 100px;\n"
"    text-align: center;\n"
"    vertical-align: middle;\n"
"    overflow: hidden;\n"
"    font: 700 15px \"Segoe Print\";\n"
"    border-color: #6272a4;\n"
"    text-shadow: 1px 1px 1px rgba(255, 255, 255, 0.65);\n"
"    box-shadow: 0 1px 1px rgba(0, 0, 0, 0.28);\n"
"}\n"
"\n"
"QPushButton:active{\n"
"    -ms-transform: translateY(2px);\n"
"    -webkit-transform: translateY(2px);\n"
"    transform: translateY(2px);\n"
"    box-shadow: 0 0 2px rgba(0, 0, 0, 0.35);\n"
"    border-bottom: none;\n"
"}\n"
"")

        self.verticalLayout_12.addWidget(self.start_training_button, 0, Qt.AlignHCenter)


        self.horizontalLayout_6.addWidget(self.training_left_frame, 0, Qt.AlignVCenter)

        self.training_right_frame = QFrame(self.training_base_frame)
        self.training_right_frame.setObjectName(u"training_right_frame")
        self.training_right_frame.setFrameShape(QFrame.StyledPanel)
        self.training_right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.training_right_frame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.training_frame_right_top = QFrame(self.training_right_frame)
        self.training_frame_right_top.setObjectName(u"training_frame_right_top")
        sizePolicy3.setHeightForWidth(self.training_frame_right_top.sizePolicy().hasHeightForWidth())
        self.training_frame_right_top.setSizePolicy(sizePolicy3)
        self.training_frame_right_top.setFrameShape(QFrame.StyledPanel)
        self.training_frame_right_top.setFrameShadow(QFrame.Raised)

        self.verticalLayout_13.addWidget(self.training_frame_right_top)

        self.training_text_label = QLabel(self.training_right_frame)
        self.training_text_label.setObjectName(u"training_text_label")
        self.training_text_label.setMinimumSize(QSize(0, 50))
        self.training_text_label.setStyleSheet(u"font: 9pt \"Segoe Print\";")
        self.training_text_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.training_text_label, 0, Qt.AlignBottom)

        self.training_frame_right_bottom = QFrame(self.training_right_frame)
        self.training_frame_right_bottom.setObjectName(u"training_frame_right_bottom")
        self.training_frame_right_bottom.setMinimumSize(QSize(0, 150))
        self.training_frame_right_bottom.setFrameShape(QFrame.StyledPanel)
        self.training_frame_right_bottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_13.addWidget(self.training_frame_right_bottom, 0, Qt.AlignBottom)


        self.horizontalLayout_6.addWidget(self.training_right_frame)


        self.gridLayout_5.addWidget(self.training_base_frame, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.training_panel)
        self.reports_panel = QWidget()
        self.reports_panel.setObjectName(u"reports_panel")
        self.reports_panel.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.reports_panel)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.reports_heading = QLabel(self.reports_panel)
        self.reports_heading.setObjectName(u"reports_heading")
        self.reports_heading.setStyleSheet(u"font: 700 15pt \"Segoe Print\";")
        self.reports_heading.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.reports_heading, 0, Qt.AlignTop)

        self.report_table_frame = QFrame(self.reports_panel)
        self.report_table_frame.setObjectName(u"report_table_frame")
        sizePolicy.setHeightForWidth(self.report_table_frame.sizePolicy().hasHeightForWidth())
        self.report_table_frame.setSizePolicy(sizePolicy)
        self.report_table_frame.setMinimumSize(QSize(0, 200))
        self.report_table_frame.setFrameShape(QFrame.StyledPanel)
        self.report_table_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.report_table_frame)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.report_table = QTableWidget(self.report_table_frame)
        if (self.report_table.columnCount() < 4):
            self.report_table.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.report_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.report_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.report_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.report_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.report_table.setObjectName(u"report_table")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.report_table.sizePolicy().hasHeightForWidth())
        self.report_table.setSizePolicy(sizePolicy5)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.report_table.setPalette(palette)
        self.report_table.setFrameShape(QFrame.NoFrame)
        self.report_table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.report_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.report_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.report_table.setAutoScroll(True)
        self.report_table.setAutoScrollMargin(5)
        self.report_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.report_table.setAlternatingRowColors(False)
        self.report_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.report_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.report_table.setShowGrid(True)
        self.report_table.setGridStyle(Qt.SolidLine)
        self.report_table.setSortingEnabled(True)
        self.report_table.setRowCount(0)
        self.report_table.horizontalHeader().setVisible(True)
        self.report_table.horizontalHeader().setCascadingSectionResizes(True)
        self.report_table.horizontalHeader().setDefaultSectionSize(200)
        self.report_table.horizontalHeader().setStretchLastSection(True)
        self.report_table.verticalHeader().setVisible(False)
        self.report_table.verticalHeader().setCascadingSectionResizes(False)
        self.report_table.verticalHeader().setHighlightSections(False)
        self.report_table.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.report_table)


        self.verticalLayout.addWidget(self.report_table_frame)

        self.stackedWidget.addWidget(self.reports_panel)
        self.register_panel = QWidget()
        self.register_panel.setObjectName(u"register_panel")
        self.verticalLayout_5 = QVBoxLayout(self.register_panel)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.register_heading = QLabel(self.register_panel)
        self.register_heading.setObjectName(u"register_heading")
        self.register_heading.setStyleSheet(u"font: 700 15pt \"Segoe Print\";")
        self.register_heading.setTextFormat(Qt.AutoText)
        self.register_heading.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.register_heading, 0, Qt.AlignTop)

        self.register_base_frame = QFrame(self.register_panel)
        self.register_base_frame.setObjectName(u"register_base_frame")
        sizePolicy3.setHeightForWidth(self.register_base_frame.sizePolicy().hasHeightForWidth())
        self.register_base_frame.setSizePolicy(sizePolicy3)
        self.register_base_frame.setFrameShape(QFrame.StyledPanel)
        self.register_base_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.register_base_frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.register_left_frame = QFrame(self.register_base_frame)
        self.register_left_frame.setObjectName(u"register_left_frame")
        sizePolicy.setHeightForWidth(self.register_left_frame.sizePolicy().hasHeightForWidth())
        self.register_left_frame.setSizePolicy(sizePolicy)
        self.register_left_frame.setMinimumSize(QSize(0, 0))
        self.register_left_frame.setStyleSheet(u"")
        self.register_left_frame.setFrameShape(QFrame.StyledPanel)
        self.register_left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.register_left_frame)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.register_input_frame = QFrame(self.register_left_frame)
        self.register_input_frame.setObjectName(u"register_input_frame")
        sizePolicy.setHeightForWidth(self.register_input_frame.sizePolicy().hasHeightForWidth())
        self.register_input_frame.setSizePolicy(sizePolicy)
        self.register_input_frame.setMinimumSize(QSize(350, 300))
        self.register_input_frame.setFrameShape(QFrame.StyledPanel)
        self.register_input_frame.setFrameShadow(QFrame.Raised)
        self.register_capture_button = QPushButton(self.register_input_frame)
        self.register_capture_button.setObjectName(u"register_capture_button")
        self.register_capture_button.setGeometry(QRect(0, 200, 351, 61))
        self.registerid_label = QLabel(self.register_input_frame)
        self.registerid_label.setObjectName(u"registerid_label")
        self.registerid_label.setGeometry(QRect(0, 70, 111, 31))
        self.register_id_input = QLineEdit(self.register_input_frame)
        self.register_id_input.setObjectName(u"register_id_input")
        self.register_id_input.setGeometry(QRect(109, 70, 231, 31))
        self.register_name_label = QLabel(self.register_input_frame)
        self.register_name_label.setObjectName(u"register_name_label")
        self.register_name_label.setGeometry(QRect(0, 130, 111, 31))
        self.register_name_input = QLineEdit(self.register_input_frame)
        self.register_name_input.setObjectName(u"register_name_input")
        self.register_name_input.setGeometry(QRect(109, 130, 231, 31))

        self.verticalLayout_16.addWidget(self.register_input_frame)


        self.horizontalLayout_8.addWidget(self.register_left_frame)

        self.register_right_frame = QFrame(self.register_base_frame)
        self.register_right_frame.setObjectName(u"register_right_frame")
        sizePolicy5.setHeightForWidth(self.register_right_frame.sizePolicy().hasHeightForWidth())
        self.register_right_frame.setSizePolicy(sizePolicy5)
        self.register_right_frame.setMinimumSize(QSize(640, 480))
        self.register_right_frame.setFrameShape(QFrame.StyledPanel)
        self.register_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.register_right_frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.register_live_feed = QLabel(self.register_right_frame)
        self.register_live_feed.setObjectName(u"register_live_feed")
        sizePolicy.setHeightForWidth(self.register_live_feed.sizePolicy().hasHeightForWidth())
        self.register_live_feed.setSizePolicy(sizePolicy)
        self.register_live_feed.setMinimumSize(QSize(320, 200))
        self.register_live_feed.setStyleSheet(u"")
        self.register_live_feed.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.register_live_feed)


        self.horizontalLayout_8.addWidget(self.register_right_frame)


        self.verticalLayout_5.addWidget(self.register_base_frame)

        self.stackedWidget.addWidget(self.register_panel)
        self.attendance_panel = QWidget()
        self.attendance_panel.setObjectName(u"attendance_panel")
        self.verticalLayout_10 = QVBoxLayout(self.attendance_panel)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.attendance_heading = QLabel(self.attendance_panel)
        self.attendance_heading.setObjectName(u"attendance_heading")
        sizePolicy.setHeightForWidth(self.attendance_heading.sizePolicy().hasHeightForWidth())
        self.attendance_heading.setSizePolicy(sizePolicy)
        self.attendance_heading.setStyleSheet(u"font: 700 15pt \"Segoe Print\";")
        self.attendance_heading.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.attendance_heading, 0, Qt.AlignTop)

        self.attendance_base_frame = QFrame(self.attendance_panel)
        self.attendance_base_frame.setObjectName(u"attendance_base_frame")
        sizePolicy3.setHeightForWidth(self.attendance_base_frame.sizePolicy().hasHeightForWidth())
        self.attendance_base_frame.setSizePolicy(sizePolicy3)
        self.attendance_base_frame.setFrameShape(QFrame.StyledPanel)
        self.attendance_base_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.attendance_base_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.attendance_left_frame = QFrame(self.attendance_base_frame)
        self.attendance_left_frame.setObjectName(u"attendance_left_frame")
        sizePolicy.setHeightForWidth(self.attendance_left_frame.sizePolicy().hasHeightForWidth())
        self.attendance_left_frame.setSizePolicy(sizePolicy)
        self.attendance_left_frame.setMinimumSize(QSize(350, 300))
        self.attendance_left_frame.setFrameShape(QFrame.StyledPanel)
        self.attendance_left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.attendance_left_frame)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.attendance_display_frame = QFrame(self.attendance_left_frame)
        self.attendance_display_frame.setObjectName(u"attendance_display_frame")
        sizePolicy3.setHeightForWidth(self.attendance_display_frame.sizePolicy().hasHeightForWidth())
        self.attendance_display_frame.setSizePolicy(sizePolicy3)
        self.attendance_display_frame.setMinimumSize(QSize(350, 300))
        self.attendance_display_frame.setFrameShape(QFrame.StyledPanel)
        self.attendance_display_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.attendance_display_frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.attendance_details_box = QGroupBox(self.attendance_display_frame)
        self.attendance_details_box.setObjectName(u"attendance_details_box")
        self.attendance_details_box.setMinimumSize(QSize(330, 150))
        self.gridLayout_2 = QGridLayout(self.attendance_details_box)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.attendance_date_label = QLabel(self.attendance_details_box)
        self.attendance_date_label.setObjectName(u"attendance_date_label")
        self.attendance_date_label.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.attendance_date_label, 0, 0, 1, 1)

        self.attendance_date_result_label = QLabel(self.attendance_details_box)
        self.attendance_date_result_label.setObjectName(u"attendance_date_result_label")
        self.attendance_date_result_label.setStyleSheet(u"")
        self.attendance_date_result_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.attendance_date_result_label, 0, 1, 1, 1)

        self.attendance_time_label = QLabel(self.attendance_details_box)
        self.attendance_time_label.setObjectName(u"attendance_time_label")
        self.attendance_time_label.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.attendance_time_label, 1, 0, 1, 1)

        self.attendance_time_result_label = QLabel(self.attendance_details_box)
        self.attendance_time_result_label.setObjectName(u"attendance_time_result_label")
        self.attendance_time_result_label.setStyleSheet(u"")
        self.attendance_time_result_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.attendance_time_result_label, 1, 1, 1, 1)

        self.attendance_id_label = QLabel(self.attendance_details_box)
        self.attendance_id_label.setObjectName(u"attendance_id_label")
        self.attendance_id_label.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.attendance_id_label, 2, 0, 1, 1)

        self.attendance_id_result_label = QLabel(self.attendance_details_box)
        self.attendance_id_result_label.setObjectName(u"attendance_id_result_label")
        self.attendance_id_result_label.setStyleSheet(u"font: 700 9pt \"Segoe Print\";")
        self.attendance_id_result_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.attendance_id_result_label, 2, 1, 1, 1)

        self.attendance_name_label = QLabel(self.attendance_details_box)
        self.attendance_name_label.setObjectName(u"attendance_name_label")
        self.attendance_name_label.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.attendance_name_label, 3, 0, 1, 1)

        self.attendance_name_result_label = QLabel(self.attendance_details_box)
        self.attendance_name_result_label.setObjectName(u"attendance_name_result_label")
        self.attendance_name_result_label.setStyleSheet(u"font: 700 9pt \"Segoe Print\";")
        self.attendance_name_result_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.attendance_name_result_label, 3, 1, 1, 1)


        self.verticalLayout_9.addWidget(self.attendance_details_box, 0, Qt.AlignBottom)

        self.attendance_information_box = QGroupBox(self.attendance_display_frame)
        self.attendance_information_box.setObjectName(u"attendance_information_box")
        self.attendance_information_box.setMinimumSize(QSize(0, 80))
        self.gridLayout = QGridLayout(self.attendance_information_box)
        self.gridLayout.setObjectName(u"gridLayout")
        self.attendance_student_count_label = QLabel(self.attendance_information_box)
        self.attendance_student_count_label.setObjectName(u"attendance_student_count_label")
        self.attendance_student_count_label.setStyleSheet(u"")

        self.gridLayout.addWidget(self.attendance_student_count_label, 0, 0, 1, 1)

        self.attendance_student_count_result = QLabel(self.attendance_information_box)
        self.attendance_student_count_result.setObjectName(u"attendance_student_count_result")
        self.attendance_student_count_result.setStyleSheet(u"font: 700 9pt \"Segoe Print\";")
        self.attendance_student_count_result.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.attendance_student_count_result, 0, 1, 1, 1)

        self.attendance_last_result = QLabel(self.attendance_information_box)
        self.attendance_last_result.setObjectName(u"attendance_last_result")
        self.attendance_last_result.setStyleSheet(u"font: 700 9pt \"Segoe Print\";")
        self.attendance_last_result.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.attendance_last_result, 1, 1, 1, 1)

        self.attendance_last_label = QLabel(self.attendance_information_box)
        self.attendance_last_label.setObjectName(u"attendance_last_label")
        self.attendance_last_label.setStyleSheet(u"")

        self.gridLayout.addWidget(self.attendance_last_label, 1, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.attendance_information_box)

        self.start_attendance_button = QPushButton(self.attendance_display_frame)
        self.start_attendance_button.setObjectName(u"start_attendance_button")
        self.start_attendance_button.setMinimumSize(QSize(0, 80))

        self.verticalLayout_9.addWidget(self.start_attendance_button, 0, Qt.AlignBottom)

        self.stop_attendance_button = QPushButton(self.attendance_display_frame)
        self.stop_attendance_button.setObjectName(u"stop_attendance_button")
        self.stop_attendance_button.setMinimumSize(QSize(0, 80))

        self.verticalLayout_9.addWidget(self.stop_attendance_button, 0, Qt.AlignBottom)


        self.verticalLayout_19.addWidget(self.attendance_display_frame)


        self.horizontalLayout_9.addWidget(self.attendance_left_frame)

        self.attendance_right_frame = QFrame(self.attendance_base_frame)
        self.attendance_right_frame.setObjectName(u"attendance_right_frame")
        self.attendance_right_frame.setMinimumSize(QSize(640, 480))
        self.attendance_right_frame.setFrameShape(QFrame.StyledPanel)
        self.attendance_right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.attendance_right_frame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.attendance_live_feed = QLabel(self.attendance_right_frame)
        self.attendance_live_feed.setObjectName(u"attendance_live_feed")
        sizePolicy5.setHeightForWidth(self.attendance_live_feed.sizePolicy().hasHeightForWidth())
        self.attendance_live_feed.setSizePolicy(sizePolicy5)
        self.attendance_live_feed.setMinimumSize(QSize(320, 200))
        self.attendance_live_feed.setStyleSheet(u"")
        self.attendance_live_feed.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.attendance_live_feed)


        self.horizontalLayout_9.addWidget(self.attendance_right_frame)


        self.verticalLayout_10.addWidget(self.attendance_base_frame)

        self.stackedWidget.addWidget(self.attendance_panel)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setBold(False)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"RannLab Technologies", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"verion 1.0.0", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_attendance.setText(QCoreApplication.translate("MainWindow", u"Mark Attendance", None))
        self.btn_register.setText(QCoreApplication.translate("MainWindow", u"Register Student", None))
        self.btn_training.setText(QCoreApplication.translate("MainWindow", u"Model Training", None))
        self.btn_report.setText(QCoreApplication.translate("MainWindow", u"Daily Report", None))
        self.title_info.setText(QCoreApplication.translate("MainWindow", u"Smart Attendance System", None))
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.home_title_label.setText(QCoreApplication.translate("MainWindow", u"Smart Attendance System", None))
        self.training_heading.setText(QCoreApplication.translate("MainWindow", u"Model Training Page", None))
        self.start_training_button.setText(QCoreApplication.translate("MainWindow", u"Start\n"
"Model\n"
"Training", None))
        self.training_text_label.setText(QCoreApplication.translate("MainWindow", u"Click 'Start Model Training' !", None))
        self.reports_heading.setText(QCoreApplication.translate("MainWindow", u"Daily Attendance Report Page", None))
        ___qtablewidgetitem = self.report_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.report_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.report_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem3 = self.report_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Time", None));
        self.register_heading.setText(QCoreApplication.translate("MainWindow", u"New Student Registration Page", None))
        self.register_capture_button.setText(QCoreApplication.translate("MainWindow", u"Start Image Capture", None))
        self.registerid_label.setText(QCoreApplication.translate("MainWindow", u"Student ID", None))
        self.register_name_label.setText(QCoreApplication.translate("MainWindow", u"Student Name", None))
        self.register_live_feed.setText("")
        self.attendance_heading.setText(QCoreApplication.translate("MainWindow", u"Mark Student Attendance", None))
        self.attendance_details_box.setTitle(QCoreApplication.translate("MainWindow", u"Details", None))
        self.attendance_date_label.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.attendance_date_result_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.attendance_time_label.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.attendance_time_result_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.attendance_id_label.setText(QCoreApplication.translate("MainWindow", u"Identified Student ID:", None))
        self.attendance_id_result_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.attendance_name_label.setText(QCoreApplication.translate("MainWindow", u"Identified Student Name:", None))
        self.attendance_name_result_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.attendance_information_box.setTitle(QCoreApplication.translate("MainWindow", u"Attendance Information", None))
        self.attendance_student_count_label.setText(QCoreApplication.translate("MainWindow", u"Total Student Count:", None))
        self.attendance_student_count_result.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.attendance_last_result.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.attendance_last_label.setText(QCoreApplication.translate("MainWindow", u"Last Attendance (Today):", None))
        self.start_attendance_button.setText(QCoreApplication.translate("MainWindow", u"Start Attendance", None))
        self.stop_attendance_button.setText(QCoreApplication.translate("MainWindow", u"Stop Attendance", None))
        self.attendance_live_feed.setText("")
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"Powered By: Dream Networks Pvt Ltd", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

