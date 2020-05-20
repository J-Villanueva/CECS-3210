# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ambient.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.setEnabled(True)
        Form.resize(749, 391)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(749, 391))
        Form.setMaximumSize(QtCore.QSize(749, 391))
        Form.setSizeIncrement(QtCore.QSize(1, 1))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        Form.setFont(font)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Form.setMouseTracking(True)
        Form.setTabletTracking(False)
        Form.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        Form.setAcceptDrops(True)
        Form.setAutoFillBackground(True)
        self.Ambient_Frame = QtWidgets.QFrame(Form)
        self.Ambient_Frame.setGeometry(QtCore.QRect(0, 0, 749, 391))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Ambient_Frame.sizePolicy().hasHeightForWidth())
        self.Ambient_Frame.setSizePolicy(sizePolicy)
        self.Ambient_Frame.setAutoFillBackground(False)
        self.Ambient_Frame.setStyleSheet("background-color: rgb(16, 128, 128);")
        self.Ambient_Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Ambient_Frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Ambient_Frame.setLineWidth(0)
        self.Ambient_Frame.setObjectName("Ambient_Frame")
        self.minutes_label = QtWidgets.QLCDNumber(self.Ambient_Frame)
        self.minutes_label.setGeometry(QtCore.QRect(660, 10, 41, 41))
        self.minutes_label.setInputMethodHints(QtCore.Qt.ImhTime)
        self.minutes_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.minutes_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.minutes_label.setDigitCount(2)
        self.minutes_label.setProperty("intValue", 88)
        self.minutes_label.setObjectName("minutes_label")
        self.hour_label = QtWidgets.QLCDNumber(self.Ambient_Frame)
        self.hour_label.setGeometry(QtCore.QRect(610, 10, 41, 41))
        self.hour_label.setAutoFillBackground(False)
        self.hour_label.setInputMethodHints(QtCore.Qt.ImhTime)
        self.hour_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.hour_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.hour_label.setDigitCount(2)
        self.hour_label.setProperty("intValue", 88)
        self.hour_label.setObjectName("hour_label")
        self.ambient_screen_title_label = QtWidgets.QLabel(self.Ambient_Frame)
        self.ambient_screen_title_label.setGeometry(QtCore.QRect(250, 90, 241, 101))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.ambient_screen_title_label.setFont(font)
        self.ambient_screen_title_label.setObjectName("ambient_screen_title_label")
        self.time_separator_label = QtWidgets.QLabel(self.Ambient_Frame)
        self.time_separator_label.setGeometry(QtCore.QRect(650, 20, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.time_separator_label.setFont(font)
        self.time_separator_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.time_separator_label.setObjectName("time_separator_label")
        self.am_pm_label = QtWidgets.QLabel(self.Ambient_Frame)
        self.am_pm_label.setGeometry(QtCore.QRect(700, 30, 31, 21))
        self.am_pm_label.setObjectName("am_pm_label")
        self.date_label = QtWidgets.QLabel(self.Ambient_Frame)
        self.date_label.setGeometry(QtCore.QRect(630, 40, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.date_label.setFont(font)
        self.date_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.date_label.setInputMethodHints(QtCore.Qt.ImhDate)
        self.date_label.setTextInteractionFlags(QtCore.Qt.TextEditable)
        self.date_label.setObjectName("date_label")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.Ambient_Frame)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 230, 191, 141))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lighting_widget_title = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lighting_widget_title.setFont(font)
        self.lighting_widget_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lighting_widget_title.setObjectName("lighting_widget_title")
        self.verticalLayout_4.addWidget(self.lighting_widget_title)
        self.lighting_percentage_label_ = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lighting_percentage_label_.setFont(font)
        self.lighting_percentage_label_.setAlignment(QtCore.Qt.AlignCenter)
        self.lighting_percentage_label_.setObjectName("lighting_percentage_label_")
        self.verticalLayout_4.addWidget(self.lighting_percentage_label_)
        self.lighting_slider = QtWidgets.QSlider(self.verticalLayoutWidget_3)
        self.lighting_slider.setProperty("value", 84)
        self.lighting_slider.setOrientation(QtCore.Qt.Horizontal)
        self.lighting_slider.setObjectName("lighting_slider")
        self.verticalLayout_4.addWidget(self.lighting_slider)
        self.light_color_selector = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.light_color_selector.setFont(font)
        self.light_color_selector.setObjectName("light_color_selector")
        self.light_color_selector.addItem("")
        self.light_color_selector.addItem("")
        self.light_color_selector.addItem("")
        self.light_color_selector.addItem("")
        self.light_color_selector.addItem("")
        self.light_color_selector.addItem("")
        self.light_color_selector.addItem("")
        self.light_color_selector.addItem("")
        self.light_color_selector.addItem("")
        self.verticalLayout_4.addWidget(self.light_color_selector)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.Ambient_Frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(490, 230, 235, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.audio_widget_title = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.audio_widget_title.setFont(font)
        self.audio_widget_title.setAlignment(QtCore.Qt.AlignCenter)
        self.audio_widget_title.setObjectName("audio_widget_title")
        self.verticalLayout_2.addWidget(self.audio_widget_title, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.skip_back_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.skip_back_button.setObjectName("skip_back_button")
        self.horizontalLayout.addWidget(self.skip_back_button)
        self.play_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.play_button.setObjectName("play_button")
        self.horizontalLayout.addWidget(self.play_button)
        self.skip_fwd_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.skip_fwd_button.setObjectName("skip_fwd_button")
        self.horizontalLayout.addWidget(self.skip_fwd_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.volume_slider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.volume_slider.setProperty("value", 40)
        self.volume_slider.setOrientation(QtCore.Qt.Horizontal)
        self.volume_slider.setObjectName("volume_slider")
        self.verticalLayout_2.addWidget(self.volume_slider)
        self.temp_units_selector_2 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.temp_units_selector_2.setFont(font)
        self.temp_units_selector_2.setObjectName("temp_units_selector_2")
        self.temp_units_selector_2.addItem("")
        self.temp_units_selector_2.addItem("")
        self.temp_units_selector_2.addItem("")
        self.temp_units_selector_2.setItemText(2, "")
        self.verticalLayout_2.addWidget(self.temp_units_selector_2)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Ambient_Frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(250, 230, 195, 141))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.temperature_widget_title = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.temperature_widget_title.setFont(font)
        self.temperature_widget_title.setAlignment(QtCore.Qt.AlignCenter)
        self.temperature_widget_title.setObjectName("temperature_widget_title")
        self.verticalLayout_3.addWidget(self.temperature_widget_title)
        self.temperature_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.temperature_label.setFont(font)
        self.temperature_label.setObjectName("temperature_label")
        self.verticalLayout_3.addWidget(self.temperature_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.temperature_slider = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.temperature_slider.setFont(font)
        self.temperature_slider.setMinimum(0)
        self.temperature_slider.setProperty("value", 70)
        self.temperature_slider.setOrientation(QtCore.Qt.Horizontal)
        self.temperature_slider.setObjectName("temperature_slider")
        self.verticalLayout_3.addWidget(self.temperature_slider)
        self.temp_units_selector = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.temp_units_selector.setFont(font)
        self.temp_units_selector.setObjectName("temp_units_selector")
        self.temp_units_selector.addItem("")
        self.temp_units_selector.addItem("")
        self.verticalLayout_3.addWidget(self.temp_units_selector)
        self.ambient_room_selector = QtWidgets.QComboBox(self.Ambient_Frame)
        self.ambient_room_selector.setGeometry(QtCore.QRect(290, 0, 165, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ambient_room_selector.setFont(font)
        self.ambient_room_selector.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.ambient_room_selector.setAcceptDrops(True)
        self.ambient_room_selector.setFrame(True)
        self.ambient_room_selector.setObjectName("ambient_room_selector")
        self.ambient_room_selector.addItem("")
        self.ambient_room_selector.addItem("")
        self.ambient_room_selector.addItem("")
        self.ambient_room_selector.addItem("")
        self.ambient_room_selector.addItem("")
        self.ambient_room_selector.addItem("")
        self.ambient_room_selector.addItem("")
        self.ambient_room_selector.addItem("")
        self.ambient_room_selector.addItem("")
        self.ambient_room_selector.addItem("")
        self.ambient_room_selector.addItem("")
        self.ambient_room_selector.addItem("")
        self.ambient_room_selector.addItem("")
        self.ambient_room_selector.addItem("")
        self.ambient_room_selector.addItem("")
        self.ambient_room_selector.addItem("")
        self.ambient_room_selector.addItem("")
        self.back_button = QtWidgets.QPushButton(self.Ambient_Frame)
        self.back_button.setGeometry(QtCore.QRect(0, 0, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.back_button.setFont(font)
        self.back_button.setObjectName("back_button")
        self.minutes_label.raise_()
        self.hour_label.raise_()
        self.ambient_screen_title_label.raise_()
        self.time_separator_label.raise_()
        self.date_label.raise_()
        self.am_pm_label.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.ambient_room_selector.raise_()
        self.back_button.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ambient_screen_title_label.setText(_translate("Form", "Ambient"))
        self.time_separator_label.setText(_translate("Form", ":"))
        self.am_pm_label.setText(_translate("Form", "AM"))
        self.date_label.setText(_translate("Form", "mm/dd/year"))
        self.lighting_widget_title.setText(_translate("Form", "Lighting"))
        self.lighting_percentage_label_.setText(_translate("Form", "0%"))
        self.light_color_selector.setItemText(0, _translate("Form", "White"))
        self.light_color_selector.setItemText(1, _translate("Form", "Yellow"))
        self.light_color_selector.setItemText(2, _translate("Form", "Green"))
        self.light_color_selector.setItemText(3, _translate("Form", "Blue"))
        self.light_color_selector.setItemText(4, _translate("Form", "Light Blue"))
        self.light_color_selector.setItemText(5, _translate("Form", "Red"))
        self.light_color_selector.setItemText(6, _translate("Form", "Pink"))
        self.light_color_selector.setItemText(7, _translate("Form", "Purple"))
        self.light_color_selector.setItemText(8, _translate("Form", "Magenta"))
        self.audio_widget_title.setText(_translate("Form", "Audio"))
        self.skip_back_button.setText(_translate("Form", "<<"))
        self.play_button.setText(_translate("Form", "►||"))
        self.skip_fwd_button.setText(_translate("Form", ">>"))
        self.temp_units_selector_2.setItemText(0, _translate("Form", "General Intercom"))
        self.temp_units_selector_2.setItemText(1, _translate("Form", "Room"))
        self.temperature_widget_title.setText(_translate("Form", "Temperature"))
        self.temperature_label.setText(_translate("Form", "0ºC"))
        self.temp_units_selector.setItemText(0, _translate("Form", "Fahrenheit"))
        self.temp_units_selector.setItemText(1, _translate("Form", "Celcius"))
        self.ambient_room_selector.setCurrentText(_translate("Form", "Whole House"))
        self.ambient_room_selector.setItemText(0, _translate("Form", "Whole House"))
        self.ambient_room_selector.setItemText(1, _translate("Form", "Master"))
        self.ambient_room_selector.setItemText(2, _translate("Form", "Bedroom1"))
        self.ambient_room_selector.setItemText(3, _translate("Form", "Bedroom2"))
        self.ambient_room_selector.setItemText(4, _translate("Form", "Living"))
        self.ambient_room_selector.setItemText(5, _translate("Form", "Family"))
        self.ambient_room_selector.setItemText(6, _translate("Form", "Guest"))
        self.ambient_room_selector.setItemText(7, _translate("Form", "Kitchen"))
        self.ambient_room_selector.setItemText(8, _translate("Form", "Dining"))
        self.ambient_room_selector.setItemText(9, _translate("Form", "Game"))
        self.ambient_room_selector.setItemText(10, _translate("Form", "Bathroom 1"))
        self.ambient_room_selector.setItemText(11, _translate("Form", "Bathroom 2"))
        self.ambient_room_selector.setItemText(12, _translate("Form", "Basement"))
        self.ambient_room_selector.setItemText(13, _translate("Form", "Library"))
        self.ambient_room_selector.setItemText(14, _translate("Form", "Gym"))
        self.ambient_room_selector.setItemText(15, _translate("Form", "Storage"))
        self.ambient_room_selector.setItemText(16, _translate("Form", "Garage"))
        self.back_button.setText(_translate("Form", "🔙"))
