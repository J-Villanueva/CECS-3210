from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime


class SmartHouse(object):

    # Constructor
    def __init__(self):
        # General variables
        self.screen_title_label = "Title"
        self.lock_button = "🔒"
        self.back_button = "↵"
        self.weekday_label = datetime.now().strftime("%a")
        self.month_label = datetime.now().strftime("%B")
        self.day_label = datetime.now().strftime("%d")
        self.year_label = datetime.now().strftime("%Y")
        self.am_pm_label = datetime.now().strftime("%p")
        self.date_separator_label = ','
        self.time_separator = ':'

        # Lockscreen variables
        self.welcome_button = "Welcome Home!"

        # Homescreen variables
        self.homescreen_temperature_label = "69ºF⛅"
        self.settings_button = "⚙️"
        self.ambient_button = "Ambient"
        self.security_button = "Security"

        # Ambient variables 
        self.lighting_widget_title = "Lighting 🔅"
        self.lighting_label = "84"
        self.light_color_selector = "color"
        self.audio_widget_title = "Audio 🎵"
        self.skip_back_button = "<<"
        self.play_button = "►||"
        self.skip_fwd_button = ">>"
        self.temp_units_selector_2 = "General Intercom"
        self.temperature_widget_title = "Temperature 🌡️"
        self.temperature_label = 70
        self.temp_units_selector = "Fahrenheit"
        self.ambient_room_selector = "Whole House"

        # Security variables
        self.video_feed_widget_lable = "Video Feed"
        self.play_video_label = "Play Feed"
        self.video_room_selector = "Video Room"
        self.arm_away_button = "Arm/Away"
        self.arm_stay_button = "Arm/Stay"
        self.entry_control_widget_label = "Entry Control"
        self.entry_selector = "Entry Selector"

        # Settings variables
        self.open_log_commandLinkButton = "Open Home Activity Log"
        self.wifi_label = "Wi-Fi"
        self.bluetooth_label = "Bluetooth"
        self.language_comboBox = "English"

        
    # LockScreen set up
    def setupUiLS(self, Form, setupUiHS):
        # Sets the whole screen and its size
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
        Form.setMouseTracking(False)
        Form.setTabletTracking(False)
        Form.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        Form.setAcceptDrops(True)
        Form.setAutoFillBackground(False)

        # The frame where all the LockScreen labels are 
        self.Lockscreen_Frame = QtWidgets.QFrame(Form)
        self.Lockscreen_Frame.setGeometry(QtCore.QRect(0, 0, 749, 391))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Lockscreen_Frame.sizePolicy().hasHeightForWidth())
        self.Lockscreen_Frame.setSizePolicy(sizePolicy)
        self.Lockscreen_Frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Lockscreen_Frame.setMouseTracking(True)
        self.Lockscreen_Frame.setAutoFillBackground(False)
        self.Lockscreen_Frame.setStyleSheet("background-color: rgb(16, 128, 128);")
        self.Lockscreen_Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Lockscreen_Frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Lockscreen_Frame.setLineWidth(0)
        self.Lockscreen_Frame.setObjectName("Lockscreen_Frame")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.Lockscreen_Frame)

        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(250, 180, 241, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        # Weekday label
        self.weekday_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.weekday_label.setFont(font)
        self.weekday_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.weekday_label.setObjectName("weekday_label")
        self.horizontalLayout_2.addWidget(self.weekday_label)

        # Month label
        self.month_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.month_label.setFont(font)
        self.month_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.month_label.setObjectName("month_label")
        self.horizontalLayout_2.addWidget(self.month_label)
        
        # Day label
        self.day_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.day_label.setFont(font)
        self.day_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.day_label.setObjectName("day_label")
        self.horizontalLayout_2.addWidget(self.day_label)

        # The coma label that separates the day number and the year
        self.date_separator_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.date_separator_label.setFont(font)
        self.date_separator_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.date_separator_label.setObjectName("date_separator_label")
        self.horizontalLayout_2.addWidget(self.date_separator_label)

        # Year label
        self.year_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.year_label.setFont(font)
        self.year_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.year_label.setObjectName("year_label")
        self.horizontalLayout_2.addWidget(self.year_label)

        # The two dots (:) that separate the hours and the minutes
        self.time_separator = QtWidgets.QLabel(self.Lockscreen_Frame)
        self.time_separator.setGeometry(QtCore.QRect(310, 50, 117, 119))
        font = QtGui.QFont()
        font.setPointSize(70)
        font.setBold(True)
        font.setWeight(75)
        self.time_separator.setFont(font)
        self.time_separator.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.time_separator.setTextFormat(QtCore.Qt.AutoText)
        self.time_separator.setScaledContents(True)
        self.time_separator.setAlignment(QtCore.Qt.AlignCenter)
        self.time_separator.setWordWrap(True)
        self.time_separator.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.time_separator.setObjectName("time_separator")

        
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.Lockscreen_Frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(230, 60, 281, 121))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Hour label
        self.hour_label = QtWidgets.QLCDNumber(self.horizontalLayoutWidget)
        self.hour_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.hour_label.setInputMethodHints(QtCore.Qt.ImhTime)
        self.hour_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.hour_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.hour_label.setDigitCount(2)
        self.hour_label.setProperty("intValue", datetime.now().strftime("%I"))
        self.hour_label.setObjectName("hour_label")
        self.horizontalLayout.addWidget(self.hour_label)

        # Minutes label
        self.minutes_label = QtWidgets.QLCDNumber(self.horizontalLayoutWidget)
        self.minutes_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.minutes_label.setInputMethodHints(QtCore.Qt.ImhTime)
        self.minutes_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.minutes_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.minutes_label.setDigitCount(2)
        self.minutes_label.setProperty("intValue", datetime.now().strftime("%M"))
        self.minutes_label.setObjectName("minutes_label")
        self.horizontalLayout.addWidget(self.minutes_label)

        # am-pm label
        self.am_pm_label = QtWidgets.QLabel(self.Lockscreen_Frame)
        self.am_pm_label.setGeometry(QtCore.QRect(510, 150, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.am_pm_label.setFont(font)
        self.am_pm_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.am_pm_label.setObjectName("am_pm_label")

        # Temperature label
        self.homescreen_temperature_label = QtWidgets.QLabel(self.Lockscreen_Frame)
        self.homescreen_temperature_label.setGeometry(QtCore.QRect(680, 0, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.homescreen_temperature_label.setFont(font)
        self.homescreen_temperature_label.setObjectName("homescreen_temperature_label")

        # Welcome button frame that contains the "Welcome Home!" button inside
        self.welcome_frame = QtWidgets.QFrame(self.Lockscreen_Frame)
        self.welcome_frame.setGeometry(QtCore.QRect(57, 223, 641, 151))
        self.welcome_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.welcome_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.welcome_frame.setObjectName("welcome_frame")

        # Welcome button that takes you to the HomeScreen when pressed
        self.welcome_button = QtWidgets.QPushButton(self.welcome_frame)
        self.welcome_button.setGeometry(QtCore.QRect(12, 7, 621, 141))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.welcome_button.setFont(font)
        self.welcome_button.setObjectName("welcome_button")

        # Lock button that closes the application, ending the program.
        self.lock_button = QtWidgets.QPushButton(self.Lockscreen_Frame)
        self.lock_button.setGeometry(QtCore.QRect(150, 0, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lock_button.setFont(font)
        self.lock_button.setObjectName("lock_button")

        self.horizontalLayoutWidget_2.raise_()
        self.horizontalLayoutWidget.raise_()
        self.am_pm_label.raise_()
        self.homescreen_temperature_label.raise_()
        self.time_separator.raise_()

        self.retranslateUiLS(Form, setupUiHS)

        # Makes the action of going to the HomeScreen
        self.welcome_button.pressed.connect(setupUiHS.show)

        # Makes the action of closing the LockScreen
        self.welcome_button.pressed.connect(Form.close)

        # Makes the action of closing the application
        self.lock_button.pressed.connect(Form.close)


        QtCore.QMetaObject.connectSlotsByName(Form)

        
    # Here we make the change from QtDesigner to Python. Also needed for all the text
    # info in the LockScreen to be displayed correctly
    def retranslateUiLS(self, Form, setupUiHS):

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "LockScreen"))
        self.weekday_label.setText(_translate("Form", datetime.now().strftime("%a")))
        self.month_label.setText(_translate("Form", datetime.now().strftime("%B")))
        self.day_label.setText(_translate("Form", datetime.now().strftime("%d")))
        self.date_separator_label.setText(_translate("Form", ","))
        self.year_label.setText(_translate("Form", datetime.now().strftime("%Y")))
        self.time_separator.setText(_translate("Form", ":"))
        self.am_pm_label.setText(_translate("Form", datetime.now().strftime("%p")))
        self.homescreen_temperature_label.setText(_translate("Form", " 69ºF⛅"))
        self.welcome_button.setText(_translate("Form", "Welcome Home!"))
        self.lock_button.setText(_translate("Form", "🔒"))

    # Home Screen set up
    def setupUiHS(self, Homescreen, setupUiAm, setupUiSec, setupUiSet):
        
        # Sets the whole screen and its size
        Homescreen.setObjectName("Homescreen")
        Homescreen.setWindowModality(QtCore.Qt.WindowModal)
        Homescreen.resize(749, 391)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Homescreen.sizePolicy().hasHeightForWidth())
        Homescreen.setSizePolicy(sizePolicy)
        Homescreen.setSizeIncrement(QtCore.QSize(1, 1))
        Homescreen.setAcceptDrops(True)
        Homescreen.setAutoFillBackground(True)
        Homescreen.setUnifiedTitleAndToolBarOnMac(False)

        # Main Frame containing the settings and lock buttons, as well as the date and time
        # and temperature
        self.centralwidget = QtWidgets.QWidget(Homescreen)
        self.centralwidget.setObjectName("centralwidget")
        self.Main_Frame = QtWidgets.QFrame(self.centralwidget)
        self.Main_Frame.setGeometry(QtCore.QRect(0, 0, 749, 391))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Main_Frame.sizePolicy().hasHeightForWidth())
        self.Main_Frame.setSizePolicy(sizePolicy)
        self.Main_Frame.setAutoFillBackground(False)
        self.Main_Frame.setStyleSheet("background-color: rgb(16, 128, 128);")
        self.Main_Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Main_Frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Main_Frame.setLineWidth(0)
        self.Main_Frame.setObjectName("Main_Frame")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.Main_Frame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(250, 180, 241, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # Weekday label
        self.weekday_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.weekday_label.setFont(font)
        self.weekday_label.setObjectName("weekday_label")
        self.horizontalLayout_2.addWidget(self.weekday_label)

        # Month label
        self.month_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.month_label.setFont(font)
        self.month_label.setObjectName("month_label")
        self.horizontalLayout_2.addWidget(self.month_label)

        # Day label
        self.day_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.day_label.setFont(font)
        self.day_label.setObjectName("day_label")
        self.horizontalLayout_2.addWidget(self.day_label)

        # Coma in between the day number and year
        self.date_separator_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.date_separator_label.setFont(font)
        self.date_separator_label.setObjectName("date_separator_label")
        self.horizontalLayout_2.addWidget(self.date_separator_label)

        # Year label
        self.year_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.year_label.setFont(font)
        self.year_label.setObjectName("year_label")
        self.horizontalLayout_2.addWidget(self.year_label)

        # Layout for the time
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.Main_Frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(230, 60, 281, 121))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Hour Label
        self.hour_label = QtWidgets.QLCDNumber(self.horizontalLayoutWidget)
        self.hour_label.setInputMethodHints(QtCore.Qt.ImhTime)
        self.hour_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.hour_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.hour_label.setDigitCount(2)
        self.hour_label.setProperty("intValue", datetime.now().strftime("%I"))
        self.hour_label.setObjectName("hour_label")
        self.horizontalLayout.addWidget(self.hour_label)

        # Minutes Label
        self.minutes_label = QtWidgets.QLCDNumber(self.horizontalLayoutWidget)
        self.minutes_label.setInputMethodHints(QtCore.Qt.ImhTime)
        self.minutes_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.minutes_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.minutes_label.setDigitCount(2)
        self.minutes_label.setProperty("intValue", datetime.now().strftime("%M"))
        self.minutes_label.setObjectName("minutes_label")
        self.horizontalLayout.addWidget(self.minutes_label)

        # am-pm Label
        self.am_pm_label = QtWidgets.QLabel(self.Main_Frame)
        self.am_pm_label.setGeometry(QtCore.QRect(510, 150, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.am_pm_label.setFont(font)
        self.am_pm_label.setObjectName("am_pm_label")

        # Temperature of Home Screen
        self.homescreen_temperature_label = QtWidgets.QLabel(self.Main_Frame)
        self.homescreen_temperature_label.setGeometry(QtCore.QRect(680, 0, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.homescreen_temperature_label.setFont(font)
        self.homescreen_temperature_label.setObjectName("homescreen_temperature_label")

        # Settings button that takes you to the settings screen when pressed
        self.settings_button = QtWidgets.QPushButton(self.Main_Frame)
        self.settings_button.setGeometry(QtCore.QRect(0, 0, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.settings_button.setFont(font)
        self.settings_button.setObjectName("settings_button")
        
        # Layout containing the Ambient and Security button
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.Main_Frame)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(130, 240, 491, 81))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        # Ambient button that takes you to the Ambient screen when pressed
        self.ambient_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.ambient_button.setObjectName("ambient_button")
        self.horizontalLayout_4.addWidget(self.ambient_button)

        # Security button that takes you to the Security screen when pressed
        self.security_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.security_button.setObjectName("security_button")
        self.horizontalLayout_4.addWidget(self.security_button)
        
        # Lock button that closes the application when pressed, ending the program
        self.lock_button = QtWidgets.QPushButton(self.Main_Frame)
        self.lock_button.setGeometry(QtCore.QRect(150, 0, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lock_button.setFont(font)
        self.lock_button.setObjectName("lock_button")

        Homescreen.setCentralWidget(self.centralwidget)

        self.retranslateUiHS(Homescreen, setupUiAm, setupUiSec, setupUiSet)

        # Makes the action of going to the Ambient screen
        self.ambient_button.pressed.connect(setupUiAm.show)

        # Makes the action of closing the HomeScreen
        self.ambient_button.pressed.connect(Homescreen.close)

        # Makes the action of going to the Security screen
        self.security_button.pressed.connect(setupUiSec.show)

        # Makes the action of closing the HomeScreen
        self.security_button.pressed.connect(Homescreen.close)

        # Makes the action of going to the Settings screen
        self.settings_button.pressed.connect(setupUiSet.show)

        # Makes the action of closing the HomeScreen
        self.settings_button.pressed.connect(Homescreen.close)

        # Makes the action of closing the application, ending the program
        self.lock_button.pressed.connect(Homescreen.close)

        QtCore.QMetaObject.connectSlotsByName(Homescreen)
        
    # Here we make the change from QtDesigner to Python. Also needed for all the text
    # info in the HomeScreen to be displayed correctly
    def retranslateUiHS(self, Homescreen, setupUiAm, setupUiSec, setupUiSet):

        _translate = QtCore.QCoreApplication.translate
        Homescreen.setWindowTitle(_translate("Homescreen", "Home"))
        self.weekday_label.setText(_translate("Homescreen", datetime.now().strftime("%a")))
        self.month_label.setText(_translate("Homescreen", datetime.now().strftime("%B")))
        self.day_label.setText(_translate("Homescreen", datetime.now().strftime("%d")))
        self.date_separator_label.setText(_translate("Homescreen", ","))
        self.year_label.setText(_translate("Homescreen", datetime.now().strftime("%Y")))
        self.time_separator.setText(_translate("Homescreen", ":"))
        self.am_pm_label.setText(_translate("Homescreen", datetime.now().strftime("%p")))
        self.homescreen_temperature_label.setText(_translate("Homescreen", " 69ºF⛅"))
        self.settings_button.setText(_translate("Homescreen", "⚙️"))
        self.ambient_button.setText(_translate("Homescreen", "Ambient"))
        self.security_button.setText(_translate("Homescreen", "Security"))
        self.lock_button.setText(_translate("Homescreen", "🔒"))
        
    # Ambient screen set up
    def setupUiAm(self, Form, setupUiHS):
        
        # Sets the whole screen and its size
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

        # The frame that contains everything in the Ambient screen
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

        # Hour label
        self.hour_label = QtWidgets.QLCDNumber(self.Ambient_Frame)
        self.hour_label.setGeometry(QtCore.QRect(610, 10, 41, 41))
        self.hour_label.setAutoFillBackground(False)
        self.hour_label.setInputMethodHints(QtCore.Qt.ImhTime)
        self.hour_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.hour_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.hour_label.setDigitCount(2)
        self.hour_label.setProperty("intValue", datetime.now().strftime("%I"))
        self.hour_label.setObjectName("hour_label")

        # Minutes label
        self.minutes_label = QtWidgets.QLCDNumber(self.Ambient_Frame)
        self.minutes_label.setGeometry(QtCore.QRect(660, 10, 41, 41))
        self.minutes_label.setInputMethodHints(QtCore.Qt.ImhTime)
        self.minutes_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.minutes_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.minutes_label.setDigitCount(2)
        self.minutes_label.setProperty("intValue", datetime.now().strftime("%M"))
        self.minutes_label.setObjectName("minutes_label")

        # Title label displaying "Ambient"
        self.screen_title_label = QtWidgets.QLabel(self.Ambient_Frame)
        self.screen_title_label.setGeometry(QtCore.QRect(250, 90, 241, 101))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.screen_title_label.setFont(font)
        self.screen_title_label.setObjectName("ambient_title_label")

        # The two dots (:) that separate the hour and minutes labels
        self.time_separator_label = QtWidgets.QLabel(self.Ambient_Frame)
        self.time_separator_label.setGeometry(QtCore.QRect(650, 20, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.time_separator_label.setFont(font)
        self.time_separator_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.time_separator_label.setObjectName("time_separator_label")

        # am-pm label
        self.am_pm_label = QtWidgets.QLabel(self.Ambient_Frame)
        self.am_pm_label.setGeometry(QtCore.QRect(700, 30, 31, 21))
        self.am_pm_label.setObjectName("am_pm_label")

        # Month label
        self.month_label = QtWidgets.QLabel(self.Ambient_Frame)
        self.month_label.setGeometry(QtCore.QRect(600, 60, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.month_label.setFont(font)
        self.month_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.month_label.setObjectName("month_label")

        # Day label
        self.day_label = QtWidgets.QLabel(self.Ambient_Frame)
        self.day_label.setGeometry(QtCore.QRect(660, 60, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.day_label.setFont(font)
        self.day_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.day_label.setObjectName("day_label")

        # Year label
        self.year_label = QtWidgets.QLabel(self.Ambient_Frame)
        self.year_label.setGeometry(QtCore.QRect(690, 60, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.year_label.setFont(font)
        self.year_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.year_label.setObjectName("year_label")

        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.Ambient_Frame)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 230, 191, 141))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
         
        # Lighting label that displays "Lighting 🔅"
        self.lighting_widget_title = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lighting_widget_title.setFont(font)
        self.lighting_widget_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lighting_widget_title.setObjectName("lighting_widget_title")
        self.verticalLayout_4.addWidget(self.lighting_widget_title)

        
        # Lighting label that changes depending on the value that the lighting slider is at
        self.lighting_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lighting_label.setFont(font)
        self.lighting_label.setAlignment(QtCore.Qt.AlignCenter)
        self.lighting_label.setObjectName("lighting_label_")
        self.verticalLayout_4.addWidget(self.lighting_label)

        # Lighting_slider that changes the intensity of the light in the room
        self.lighting_slider = QtWidgets.QSlider(self.verticalLayoutWidget_3)
        self.lighting_slider.setMaximum(100)
        self.lighting_slider.setProperty("value", 84)
        self.lighting_slider.setOrientation(QtCore.Qt.Horizontal)
        self.lighting_slider.setObjectName("lighting_slider")
        self.verticalLayout_4.addWidget(self.lighting_slider)

        # Lighting color select
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

        # Audio label that displays "Audio 🎵"
        self.audio_widget_title = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.audio_widget_title.setFont(font)
        self.audio_widget_title.setAlignment(QtCore.Qt.AlignCenter)
        self.audio_widget_title.setObjectName("audio_widget_title")
        self.verticalLayout_2.addWidget(self.audio_widget_title, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        # Skip backwards button for the song playing
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.skip_back_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.skip_back_button.setObjectName("skip_back_button")
        self.horizontalLayout.addWidget(self.skip_back_button)

        # Play button that pauses or plays the song
        self.play_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.play_button.setObjectName("play_button")
        self.horizontalLayout.addWidget(self.play_button)

        # Skip forward button that moves on to the next song
        self.skip_fwd_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.skip_fwd_button.setObjectName("skip_fwd_button")
        self.horizontalLayout.addWidget(self.skip_fwd_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        # Volume slide that changes how loud the music is playing 
        self.volume_slider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.volume_slider.setProperty("value", 40)
        self.volume_slider.setOrientation(QtCore.Qt.Horizontal)
        self.volume_slider.setObjectName("volume_slider")
        self.verticalLayout_2.addWidget(self.volume_slider)

        # displays the option of choosing between the audio in a room or the general intercom
        self.temp_units_selector_2 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.temp_units_selector_2.setFont(font)
        self.temp_units_selector_2.setObjectName("temp_units_selector_2")
        self.temp_units_selector_2.addItem("")
        self.temp_units_selector_2.addItem("")
        self.verticalLayout_2.addWidget(self.temp_units_selector_2)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Ambient_Frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(250, 230, 195, 141))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        # Temperature label that displays "Temperature 🌡️"
        self.temperature_widget_title = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.temperature_widget_title.setFont(font)
        self.temperature_widget_title.setAlignment(QtCore.Qt.AlignCenter)
        self.temperature_widget_title.setObjectName("temperature_widget_title")
        self.verticalLayout_3.addWidget(self.temperature_widget_title)

        # Displays the temperature number, based on where the temperature slider is sitting at
        self.temperature_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.temperature_label.setFont(font)
        self.temperature_label.setObjectName("temperature_label")
        self.verticalLayout_3.addWidget(self.temperature_label, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        # Temperature slider that can adjust the temperature in a room
        self.temperature_slider = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.temperature_slider.setFont(font)
        self.temperature_slider.setMinimum(50)
        self.temperature_slider.setMaximum(90)
        self.temperature_slider.setProperty("value", 70)
        self.temperature_slider.setOrientation(QtCore.Qt.Horizontal)
        self.temperature_slider.setObjectName("temperature_slider")
        self.verticalLayout_3.addWidget(self.temperature_slider)

        # Lets you select what type of temperature you want, either Fahrenheit or Celsius
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

        # Selects the room of the house that wants to have it's lighting, temperature or audio changed
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

        # Back button that takes you back to the HomeScreen
        self.back_button = QtWidgets.QPushButton(self.Ambient_Frame)
        self.back_button.setGeometry(QtCore.QRect(0, 0, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.back_button.setFont(font)
        self.back_button.setObjectName("back_button")

        # Lock button that closes the application, ending the program
        self.lock_button = QtWidgets.QPushButton(self.Ambient_Frame)
        self.lock_button.setGeometry(QtCore.QRect(150, 0, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lock_button.setFont(font)
        self.lock_button.setObjectName("lock_button")

        self.minutes_label.raise_()
        self.hour_label.raise_()
        self.screen_title_label.raise_()
        self.time_separator_label.raise_()
        self.am_pm_label.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.ambient_room_selector.raise_()
        self.back_button.raise_()
        self.lock_button.raise_()

        self.retranslateUiAm(Form, setupUiHS)

        # Makes the action of going back to the HomeScreen
        self.back_button.pressed.connect(setupUiHS.show)
        
        # Makes the action of closing the Ambient screen
        self.back_button.pressed.connect(Form.close)

        # Makes the action of closing the application, ending the program
        self.lock_button.pressed.connect(Form.close)

        # Makes the action of passing the current value of the slider to the lighting label
        self.lighting_slider.valueChanged['int'].connect(self.lighting_label.setNum)

        # Makes the action of passing the current value of the slider to the temperature label
        self.temperature_slider.valueChanged['int'].connect(self.temperature_label.setNum)

        # Calls the method for updating the temperature, based on Fahrenheit or Celsius 
        self.update_temperature()

        QtCore.QMetaObject.connectSlotsByName(Form)

    # Here we make the change from QtDesigner to Python. Also needed for all the text
    # info in the Ambient screen to be displayed correctly
    def retranslateUiAm(self, Form, setupUiHS):

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ambient"))
        self.screen_title_label.setText(_translate("Form", "Ambient"))
        self.time_separator_label.setText(_translate("Form", ":"))
        self.am_pm_label.setText(_translate("Form", datetime.now().strftime("%p")))
        self.month_label.setText(_translate("Form", datetime.now().strftime("%B")))
        self.day_label.setText(_translate("Form", datetime.now().strftime("%d")))
        self.date_separator_label.setText(_translate("Form", ","))
        self.year_label.setText(_translate("Form", datetime.now().strftime("%Y")))
        self.lighting_widget_title.setText(_translate("Form", "Lighting 🔅"))
        self.lighting_label.setText(_translate("Form", "84"))
        self.light_color_selector.setItemText(0, _translate("Form", "White"))
        self.light_color_selector.setItemText(1, _translate("Form", "Yellow"))
        self.light_color_selector.setItemText(2, _translate("Form", "Green"))
        self.light_color_selector.setItemText(3, _translate("Form", "Blue"))
        self.light_color_selector.setItemText(4, _translate("Form", "Light Blue"))
        self.light_color_selector.setItemText(5, _translate("Form", "Red"))
        self.light_color_selector.setItemText(6, _translate("Form", "Pink"))
        self.light_color_selector.setItemText(7, _translate("Form", "Purple"))
        self.light_color_selector.setItemText(8, _translate("Form", "Magenta"))
        self.audio_widget_title.setText(_translate("Form", "Audio 🎵"))
        self.skip_back_button.setText(_translate("Form", "<<"))
        self.play_button.setText(_translate("Form", "►||"))
        self.skip_fwd_button.setText(_translate("Form", ">>"))
        self.temp_units_selector_2.setItemText(0, _translate("Form", "General Intercom"))
        self.temp_units_selector_2.setItemText(1, _translate("Form", "Room"))
        self.temperature_widget_title.setText(_translate("Form", "Temperature 🌡️"))
        self.temperature_label.setText(_translate("Form", "70"))
        self.temp_units_selector.setItemText(0, _translate("Form", "Fahrenheit"))
        self.temp_units_selector.setItemText(1, _translate("Form", "Celsius"))
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
        self.back_button.setText(_translate("Form", "↵"))
        self.lock_button.setText(_translate("Form", "🔒"))

    # Security screen set up
    def setupUiSec(self, Form, setupUiHS):
        
        # Sets the whole screen and its size
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

        # The frame that contains everything in the Security screen
        self.Security_Frame = QtWidgets.QFrame(Form)
        self.Security_Frame.setGeometry(QtCore.QRect(0, 0, 749, 391))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Security_Frame.sizePolicy().hasHeightForWidth())
        self.Security_Frame.setSizePolicy(sizePolicy)
        self.Security_Frame.setAutoFillBackground(False)
        self.Security_Frame.setStyleSheet("background-color: rgb(16, 128, 128);")
        self.Security_Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Security_Frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Security_Frame.setLineWidth(0)
        self.Security_Frame.setObjectName("Security_Frame")

        # Back to the HomeScreen
        self.back_button = QtWidgets.QPushButton(self.Security_Frame)
        self.back_button.setGeometry(QtCore.QRect(0, 0, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.back_button.setFont(font)
        self.back_button.setObjectName("back_button")

        # Hour label
        self.hour_label = QtWidgets.QLCDNumber(self.Security_Frame)
        self.hour_label.setGeometry(QtCore.QRect(610, 10, 41, 41))
        self.hour_label.setAutoFillBackground(False)
        self.hour_label.setInputMethodHints(QtCore.Qt.ImhTime)
        self.hour_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.hour_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.hour_label.setDigitCount(2)
        self.hour_label.setProperty("intValue", datetime.now().strftime("%I"))
        self.hour_label.setObjectName("hour_label")

        # Minutes label
        self.minutes_label = QtWidgets.QLCDNumber(self.Security_Frame)
        self.minutes_label.setGeometry(QtCore.QRect(660, 10, 41, 41))
        self.minutes_label.setInputMethodHints(QtCore.Qt.ImhTime)
        self.minutes_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.minutes_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.minutes_label.setDigitCount(2)
        self.minutes_label.setProperty("intValue", datetime.now().strftime("%M"))
        self.minutes_label.setObjectName("minutes_label")

        # Title label displaying "Security"
        self.screen_title_label = QtWidgets.QLabel(self.Security_Frame)
        self.screen_title_label.setGeometry(QtCore.QRect(250, 50, 241, 101))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.screen_title_label.setFont(font)
        self.screen_title_label.setObjectName("security_title_label")

        # Displays the two dots (:) in between the hour and the minutes labels
        self.time_separator_label = QtWidgets.QLabel(self.Security_Frame)
        self.time_separator_label.setGeometry(QtCore.QRect(650, 20, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.time_separator_label.setFont(font)
        self.time_separator_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.time_separator_label.setObjectName("time_separator_label")

        # am-pm label
        self.am_pm_label = QtWidgets.QLabel(self.Security_Frame)
        self.am_pm_label.setGeometry(QtCore.QRect(700, 30, 31, 21))
        self.am_pm_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.am_pm_label.setObjectName("am_pm_label")

        # Month label
        self.month_label = QtWidgets.QLabel(self.Security_Frame)
        self.month_label.setGeometry(QtCore.QRect(600, 60, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.month_label.setFont(font)
        self.month_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.month_label.setObjectName("month_label")

        # Day label
        self.day_label = QtWidgets.QLabel(self.Security_Frame)
        self.day_label.setGeometry(QtCore.QRect(660, 60, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.day_label.setFont(font)
        self.day_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.day_label.setObjectName("day_label")

        # Year label
        self.year_label = QtWidgets.QLabel(self.Security_Frame)
        self.year_label.setGeometry(QtCore.QRect(690, 60, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.year_label.setFont(font)
        self.year_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.year_label.setObjectName("year_label")

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Security_Frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(120, 240, 171, 81))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        # Video feed label
        self.video_feed_widget_lable = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.video_feed_widget_lable.setFont(font)
        self.video_feed_widget_lable.setObjectName("video_feed_widget_lable")
        self.verticalLayout_3.addWidget(self.video_feed_widget_lable, 0, QtCore.Qt.AlignHCenter)
        self.play_video_label = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.play_video_label.setObjectName("play_video_label")
        self.verticalLayout_3.addWidget(self.play_video_label)

        # Selects the room of the house that the user wants to see the camera of
        self.video_room_selector = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.video_room_selector.setFont(font)
        self.video_room_selector.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.video_room_selector.setAcceptDrops(True)
        self.video_room_selector.setFrame(True)
        self.video_room_selector.setObjectName("video_room_selector")
        self.video_room_selector.addItem("")
        self.video_room_selector.addItem("")
        self.video_room_selector.addItem("")
        self.video_room_selector.addItem("")
        self.video_room_selector.addItem("")
        self.video_room_selector.addItem("")
        self.video_room_selector.addItem("")
        self.video_room_selector.addItem("")
        self.video_room_selector.addItem("")
        self.video_room_selector.addItem("")
        self.video_room_selector.addItem("")
        self.video_room_selector.addItem("")
        self.video_room_selector.addItem("")
        self.video_room_selector.addItem("")
        self.verticalLayout_3.addWidget(self.video_room_selector)

        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.Security_Frame)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(120, 130, 491, 107))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # Arm away button
        self.arm_away_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.arm_away_button.setObjectName("arm_away_button")
        self.horizontalLayout_3.addWidget(self.arm_away_button)

        # Arm stay button
        self.arm_stay_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.arm_stay_button.setObjectName("arm_stay_button")
        self.horizontalLayout_3.addWidget(self.arm_stay_button)

        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.Security_Frame)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(440, 240, 173, 83))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        # Entry control label
        self.entry_control_widget_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.entry_control_widget_label.setFont(font)
        self.entry_control_widget_label.setObjectName("entry_control_widget_label")
        self.verticalLayout_4.addWidget(self.entry_control_widget_label, 0, QtCore.Qt.AlignHCenter)

        # Locks or unlocks the different entrances of the house
        self.door_lock_button_box = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget_3)
        self.door_lock_button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Close | QtWidgets.QDialogButtonBox.Open)
        self.door_lock_button_box.setCenterButtons(True)
        self.door_lock_button_box.setObjectName("door_lock_button_box")
        self.verticalLayout_4.addWidget(self.door_lock_button_box)

        # Selects which entrance of the house to lcck or unlock
        self.entry_selector = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.entry_selector.setFont(font)
        self.entry_selector.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entry_selector.setAcceptDrops(True)
        self.entry_selector.setFrame(True)
        self.entry_selector.setObjectName("entry_selector")
        self.entry_selector.addItem("")
        self.entry_selector.addItem("")
        self.entry_selector.addItem("")
        self.entry_selector.addItem("")
        self.entry_selector.addItem("")
        self.verticalLayout_4.addWidget(self.entry_selector)

        # Lock button that closes the application, ending the program
        self.lock_button = QtWidgets.QPushButton(self.Security_Frame)
        self.lock_button.setGeometry(QtCore.QRect(150, 0, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lock_button.setFont(font)
        self.lock_button.setObjectName("lock_button")

        self.back_button.raise_()
        self.minutes_label.raise_()
        self.hour_label.raise_()
        self.time_separator_label.raise_()
        self.am_pm_label.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.horizontalLayoutWidget_3.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.screen_title_label.raise_()
        self.lock_button.raise_()

        self.retranslateUiSec(Form, setupUiHS)

        # Makes the action of going back to the HomeScreen
        self.back_button.pressed.connect(setupUiHS.show)

        # Makes the action closing the Security screen
        self.back_button.pressed.connect(Form.close)

        # Makes the action of closing the application, ending the program
        self.lock_button.pressed.connect(Form.close)

        QtCore.QMetaObject.connectSlotsByName(Form)

    # Here we make the change from QtDesigner to Python. Also needed for all the text
    # info in the Ambient screen to be displayed correctly 
    def retranslateUiSec(self, Form, setupUiHS):

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Security"))
        self.screen_title_label.setText(_translate("Form", "Security"))
        self.time_separator_label.setText(_translate("Form", ":"))
        self.am_pm_label.setText(_translate("Form", datetime.now().strftime("%p")))
        self.month_label.setText(_translate("Form", datetime.now().strftime("%B")))
        self.day_label.setText(_translate("Form", datetime.now().strftime("%d")))
        self.date_separator_label.setText(_translate("Form", ","))
        self.year_label.setText(_translate("Form", datetime.now().strftime("%Y")))
        self.video_feed_widget_lable.setText(_translate("Form", "Video Feed"))
        self.play_video_label.setText(_translate("Form", "Play Feed"))
        self.video_room_selector.setCurrentText(_translate("Form", "Master"))
        self.video_room_selector.setItemText(0, _translate("Form", "Master"))
        self.video_room_selector.setItemText(1, _translate("Form", "Bedroom1"))
        self.video_room_selector.setItemText(2, _translate("Form", "Bedroom2"))
        self.video_room_selector.setItemText(3, _translate("Form", "Living"))
        self.video_room_selector.setItemText(4, _translate("Form", "Family"))
        self.video_room_selector.setItemText(5, _translate("Form", "Guest"))
        self.video_room_selector.setItemText(6, _translate("Form", "Kitchen"))
        self.video_room_selector.setItemText(7, _translate("Form", "Dining"))
        self.video_room_selector.setItemText(8, _translate("Form", "Game"))
        self.video_room_selector.setItemText(9, _translate("Form", "Basement"))
        self.video_room_selector.setItemText(10, _translate("Form", "Library"))
        self.video_room_selector.setItemText(11, _translate("Form", "Gym"))
        self.video_room_selector.setItemText(12, _translate("Form", "Storage"))
        self.video_room_selector.setItemText(13, _translate("Form", "Garage"))
        self.arm_away_button.setText(_translate("Form", "Arm/Away"))
        self.arm_stay_button.setText(_translate("Form", "Arm/Stay"))
        self.entry_control_widget_label.setText(_translate("Form", "Entry Control"))
        self.entry_selector.setCurrentText(_translate("Form", "Whole House"))
        self.entry_selector.setItemText(0, _translate("Form", "Whole House"))
        self.entry_selector.setItemText(1, _translate("Form", "Main Entrance Door"))
        self.entry_selector.setItemText(2, _translate("Form", "Kitchen Door"))
        self.entry_selector.setItemText(3, _translate("Form", "Master Bedroom Door"))
        self.entry_selector.setItemText(4, _translate("Form", "Garage Door"))
        self.back_button.setText(_translate("Form", "↵"))
        self.lock_button.setText(_translate("Form", "🔒"))

    # Setting screen set up
    def setupUiSet(self, Form, setupUiHS):

        # Sets the whole screen and its size
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

        # Settings frame that contains the everything in the Settings screen
        self.Settings_Frame = QtWidgets.QFrame(Form)
        self.Settings_Frame.setGeometry(QtCore.QRect(0, 0, 749, 391))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Settings_Frame.sizePolicy().hasHeightForWidth())
        self.Settings_Frame.setSizePolicy(sizePolicy)
        self.Settings_Frame.setAutoFillBackground(False)
        self.Settings_Frame.setStyleSheet("background-color: rgb(16, 128, 128);")
        self.Settings_Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Settings_Frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Settings_Frame.setLineWidth(0)
        self.Settings_Frame.setObjectName("Settings_Frame")

        # Hour label
        self.hour_label = QtWidgets.QLCDNumber(self.Settings_Frame)
        self.hour_label.setGeometry(QtCore.QRect(610, 10, 41, 41))
        self.hour_label.setAutoFillBackground(False)
        self.hour_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.hour_label.setInputMethodHints(QtCore.Qt.ImhTime)
        self.hour_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.hour_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.hour_label.setDigitCount(2)
        self.hour_label.setProperty("intValue", datetime.now().strftime("%I"))
        self.hour_label.setObjectName("hour_label")

        # Minutes label
        self.minutes_label = QtWidgets.QLCDNumber(self.Settings_Frame)
        self.minutes_label.setGeometry(QtCore.QRect(660, 10, 41, 41))
        self.minutes_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n")
        self.minutes_label.setInputMethodHints(QtCore.Qt.ImhTime)
        self.minutes_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.minutes_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.minutes_label.setDigitCount(2)
        self.minutes_label.setProperty("intValue", datetime.now().strftime("%M"))
        self.minutes_label.setObjectName("minutes_label")

        # Title label displaying "Settings"
        self.screen_title_label = QtWidgets.QLabel(self.Settings_Frame)
        self.screen_title_label.setGeometry(QtCore.QRect(250, 20, 241, 101))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.screen_title_label.setFont(font)
        self.screen_title_label.setAutoFillBackground(False)
        self.screen_title_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.screen_title_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.screen_title_label.setLineWidth(0)
        self.screen_title_label.setScaledContents(False)
        self.screen_title_label.setObjectName("settings_title_label")

        # Displays the two dots(:) that separate the hour and minutes labels
        self.time_separator_label = QtWidgets.QLabel(self.Settings_Frame)
        self.time_separator_label.setGeometry(QtCore.QRect(650, 20, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.time_separator_label.setFont(font)
        self.time_separator_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.time_separator_label.setObjectName("time_separator_label")

        # Month label
        self.month_label = QtWidgets.QLabel(self.Settings_Frame)
        self.month_label.setGeometry(QtCore.QRect(600, 60, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.month_label.setFont(font)
        self.month_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.month_label.setObjectName("month_label")

        # Day label
        self.day_label = QtWidgets.QLabel(self.Settings_Frame)
        self.day_label.setGeometry(QtCore.QRect(660, 60, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.day_label.setFont(font)
        self.day_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.day_label.setObjectName("day_label")

        # Year label
        self.year_label = QtWidgets.QLabel(self.Settings_Frame)
        self.year_label.setGeometry(QtCore.QRect(690, 60, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.year_label.setFont(font)
        self.year_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.year_label.setObjectName("year_label")

        # am-pm label
        self.am_pm_label = QtWidgets.QLabel(self.Settings_Frame)
        self.am_pm_label.setGeometry(QtCore.QRect(700, 30, 31, 21))
        self.am_pm_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.am_pm_label.setObjectName("am_pm_label")

        # Back button that goes back the homeScreen
        self.back_button = QtWidgets.QPushButton(self.Settings_Frame)
        self.back_button.setGeometry(QtCore.QRect(0, 0, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("")
        self.back_button.setAutoDefault(False)
        self.back_button.setDefault(True)
        self.back_button.setObjectName("back_button")


        self.label = QtWidgets.QLabel(self.Settings_Frame)
        self.label.setGeometry(QtCore.QRect(560, 370, 191, 21))
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 128);")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setObjectName("label")

        # opens a log containing the lighting and temperature changes made
        self.open_log_commandLinkButton = QtWidgets.QCommandLinkButton(self.Settings_Frame)
        self.open_log_commandLinkButton.setGeometry(QtCore.QRect(120, 320, 521, 46))
        self.open_log_commandLinkButton.setAutoFillBackground(False)
        self.open_log_commandLinkButton.setStyleSheet("background-color: rgba(255, 255, 255, 124);")
        self.open_log_commandLinkButton.setDefault(True)
        self.open_log_commandLinkButton.setObjectName("open_log_commandLinkButton")

        # The frame that contains everything related to the Wi-fi, Bluetooth
        self.wiBlu_frame = QtWidgets.QFrame(self.Settings_Frame)
        self.wiBlu_frame.setGeometry(QtCore.QRect(240, 150, 251, 110))
        self.wiBlu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.wiBlu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wiBlu_frame.setObjectName("wiBlu_frame")

        self.widget = QtWidgets.QWidget(self.wiBlu_frame)
        self.widget.setGeometry(QtCore.QRect(0, 0, 251, 51))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Wi-fi label
        self.wifi_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.wifi_label.setFont(font)
        self.wifi_label.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.wifi_label)

        # Wi-fi slider that turns the Wi-fi on or off
        self.wifi_slider = QtWidgets.QSlider(self.widget)
        self.wifi_slider.setMaximum(1)
        self.wifi_slider.setPageStep(1)
        self.wifi_slider.setProperty("value", 1)
        self.wifi_slider.setOrientation(QtCore.Qt.Horizontal)
        self.wifi_slider.setObjectName("wifi_slider")
        self.horizontalLayout.addWidget(self.wifi_slider)

        self.layoutWidget = QtWidgets.QWidget(self.wiBlu_frame)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 50, 251, 51))
        self.layoutWidget.setObjectName("layoutWidget")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # Bluetooth label
        self.bluetooth_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.bluetooth_label.setFont(font)
        self.bluetooth_label.setObjectName("bluetooth_label")
        self.horizontalLayout_2.addWidget(self.bluetooth_label)

        # Bluetooth slider that turns the Bluetooth on or off
        self.bluetooth_slider = QtWidgets.QSlider(self.layoutWidget)
        self.bluetooth_slider.setMaximum(1)
        self.bluetooth_slider.setPageStep(1)
        self.bluetooth_slider.setProperty("value", 1)
        self.bluetooth_slider.setOrientation(QtCore.Qt.Horizontal)
        self.bluetooth_slider.setObjectName("bluetooth_slider")
        self.horizontalLayout_2.addWidget(self.bluetooth_slider)

        # Failed attempt to make our application have multiple languages
        '''
        self.language_comboBox = QtWidgets.QComboBox(self.wiBluLan_frame)
        self.language_comboBox.setGeometry(QtCore.QRect(0, 100, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.language_comboBox.setFont(font)
        self.language_comboBox.setObjectName("language_comboBox")
        self.language_comboBox.addItem("")
        self.language_comboBox.addItem("")
        self.language_comboBox.addItem("")
        self.language_comboBox.addItem("")
        self.language_comboBox.addItem("")
        self.language_comboBox.addItem("")
        self.language_comboBox.addItem("")
        self.language_comboBox.addItem("")
        '''
        
        # Lock button that closes the application, ending the program
        self.lock_button = QtWidgets.QPushButton(self.Settings_Frame)
        self.lock_button.setGeometry(QtCore.QRect(150, 0, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lock_button.setFont(font)
        self.lock_button.setObjectName("lock_button")

        self.minutes_label.raise_()
        self.hour_label.raise_()
        self.screen_title_label.raise_()
        self.time_separator_label.raise_()
        self.am_pm_label.raise_()
        self.back_button.raise_()
        self.label.raise_()
        self.open_log_commandLinkButton.raise_()
        self.lock_button.raise_()

        self.retranslateUiSet(Form, setupUiHS)

        # Makes the action of going back to the HomeScreen
        self.back_button.pressed.connect(setupUiHS.show)

        # Makes the action of closing the Settings screen
        self.back_button.pressed.connect(Form.close)

        # Makes the action of closing the application, ending the program
        self.lock_button.pressed.connect(Form.close)

        # Button to open txtfile with log
        self.open_log_commandLinkButton.pressed.connect(lambda: self.open_file())

        QtCore.QMetaObject.connectSlotsByName(Form)

    # Here we make the change from QtDesigner to Python. Also needed for all the text
    # info in the Ambient screen to be displayed correctly 
    def retranslateUiSet(self, Form, setupUiHS):

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Settings"))
        self.screen_title_label.setText(_translate("Form", "Settings"))
        self.time_separator_label.setText(_translate("Form", ":"))
        self.am_pm_label.setText(_translate("Form", datetime.now().strftime("%p")))
        self.month_label.setText(_translate("Form", datetime.now().strftime("%B")))
        self.day_label.setText(_translate("Form", datetime.now().strftime("%d")))
        self.date_separator_label.setText(_translate("Form", ","))
        self.year_label.setText(_translate("Form", datetime.now().strftime("%Y")))
        self.label.setText(_translate("Form", "AutoHome Application(1.0.0)"))
        self.open_log_commandLinkButton.setText(_translate("Form", "Open Home Activity Log"))
        self.wifi_label.setText(_translate("Form", "📶 Wi-Fi          "))
        self.bluetooth_label.setText(_translate("Form", " ᛒ   Bluetooth  "))
        self.back_button.setText(_translate("Form", "↵"))
        self.lock_button.setText(_translate("Form", "🔒"))
        
        # From the language failed attempt
        '''
        self.language_comboBox.setItemText(0, _translate("Form", "English"))
        self.language_comboBox.setItemText(1, _translate("Form", "Spanish"))
        self.language_comboBox.setItemText(2, _translate("Form", "French"))
        self.language_comboBox.setItemText(3, _translate("Form", "Italian"))
        self.language_comboBox.setItemText(4, _translate("Form", "Portuguese"))
        self.language_comboBox.setItemText(5, _translate("Form", "Mandarin"))
        self.language_comboBox.setItemText(6, _translate("Form", "Korean"))
        self.language_comboBox.setItemText(7, _translate("Form", "Japanese"))
        '''


    # This method updates and sets the AutoHome time and date in any open widget
    def update_time(self):
            
        self.minutes_label.setProperty("intValue", datetime.now().strftime("%M"))
        self.hour_label.setProperty("intValue", datetime.now().strftime("%I"))

        # self.hour_label.setText("Form", datetime.now().strftime("%I"))
        # self.minutes_label.setText("Form", datetime.now().strftime("%M"))
        self.am_pm_label.setText(datetime.now().strftime("%p"))

        self.month_label.setText(datetime.now().strftime("%B"))
        self.day_label.setText(datetime.now().strftime("%d"))
        self.year_label.setText(datetime.now().strftime("%Y"))

    # This method saves the AutoHome generated events to a File as text log
    def Save_Log(self):

        elements = {'Lighting set to': self.lighting_label, 'Temperature set to': self.temperature_label}

        # create list of strings
        list_of_strings = [f'{key} : {elements[key]}' for key in elements]

        f = open('AutoHomeLog.txt', 'a+')

        f.write('AutoHomeLog.txt'+ " ")
        f.write(datetime.now().strftime("%c")+ "\n")
        f.close()

        with open('AutoHomeLog.txt', 'a+') as my_file:
            [my_file.write(f'{st}\n') for st in list_of_strings]
            my_file.write("---------------------------------" + "\n")
            my_file.close()

    # This method updates and sets the AutoHome temperature set in ambient to any open widget    
    def update_temperature(self):
        
        newtemp = self.temperature_slider.value()
        self.temperature_label.setText(str(newtemp))
        
    # This method opens the log file that contains the lighting and temperature changes
    def open_file(self):
        
        import os
        os.system('cmd /c "AutoHomeLog.txt"')

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)

    lockScreen = QtWidgets.QWidget()
    homeScreen = QtWidgets.QMainWindow()
    ambient = QtWidgets.QWidget()
    security = QtWidgets.QWidget()
    settings = QtWidgets.QWidget()

    ui = SmartHouse()
    ui.setupUiLS(lockScreen, homeScreen)
    #ui.retranslateUiLS()
    lockScreen.show()
    ui.setupUiHS(homeScreen, ambient, security, settings)
    ui.retranslateUiHS(homeScreen, ambient, security, settings)
    ui.Save_Log()
    timer = QtCore.QTimer(homeScreen)
    timer.timeout.connect(lambda: ui.retranslateUiHS(homeScreen, ambient, security, settings))
    timer.start(1000)
    #homeScreen.show()
     
    ui.setupUiAm(ambient, homeScreen)
    ui.retranslateUiAm(ambient, homeScreen)

    ui.setupUiSet(settings, homeScreen)
    ui.retranslateUiSet(settings, homeScreen)

    ui.setupUiSec(security, homeScreen)
    ui.retranslateUiSec(security, homeScreen)

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    
