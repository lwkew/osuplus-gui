import settings
import random
import sys
import requests
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from app_modules import *

from data import recommendinfo, userinfo



class MainWindow(QMainWindow, userinfo, recommendinfo, QLabel):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        UIFunctions.removeTitleBar(True)
        self.setWindowTitle('osu!plus')
        UIFunctions.labelTitle(self, 'osu!plus')
        UIFunctions.labelDescription(self, 'beatmap recommendation system')
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "osu!plus", "btn_home", "url(:/16x16/icons/16x16/cil-home.png)", True)
        UIFunctions.addNewMenu(self, "mod selection", "btn_widgets", "url(:/16x16/icons/16x16/cil-equalizer.png)", True)
        UIFunctions.selectStandardMenu(self, "btn_home")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        #DEFINING THE WIDTH OF THE COLUMNS IN THE TABLE
        self.ui.Recent_Maps.setColumnWidth(0,460)
        self.ui.Recent_Maps.setColumnWidth(1,70)
        self.ui.Recent_Maps.setColumnWidth(2,70)
        self.ui.Recent_Maps.setColumnWidth(3,70)
        self.ui.Recent_Maps.setColumnWidth(4,70)
        self.ui.Recent_Maps.setColumnWidth(5,70)
        



        def loadmaps():
            
            row = 0
            songs= userinfo.GetRecentScore()
            self.ui.Recent_Maps.setRowCount(len(songs))

            for song in songs:
                #LOOPING THROUGH THE LATEST PLAYS AND INPUTTING THE COUNTS OF THE 300, 100, 50 AND MISS COUNTS INTO THE REQUIRED TABLES
                self.ui.Recent_Maps.setItem(row, 1, QtWidgets.QTableWidgetItem(song['count300']))
                self.ui.Recent_Maps.setItem(row, 2, QtWidgets.QTableWidgetItem(song['count100']))
                self.ui.Recent_Maps.setItem(row, 3, QtWidgets.QTableWidgetItem(song['count50']))
                self.ui.Recent_Maps.setItem(row, 4, QtWidgets.QTableWidgetItem(song['countmiss']))
                
                row = row+1
            
            title= userinfo.GetRecentTitle()
            row = 0
            for test in title:
                #LOOPING THROUGH THE TITLES AND PLACING THEM IN THE FIRST COLUMN OF THE TABLE
                self.ui.Recent_Maps.setItem(row, 0, QtWidgets.QTableWidgetItem(test))
                row = row+1
            
            songs2 = userinfo.GetRecentAccuracy()
            row = 0
            for song1 in songs2:
                #LOOPING THROUGH THE ACCURACY CALCULATIONS AND ADDING THEM INTO THE TABLE
                self.ui.Recent_Maps.setItem(row, 5, QtWidgets.QTableWidgetItem(str(song1)+'%'))
                row = row+1
                
        
        
        def returnuser():
            #TAKING THE USERNAME READING FROM THE TEXT BOX
            self._username = self.ui.username.text()
        
        self.ui.username.setPlaceholderText("ENTER USERNAME")#PLACEHOLDER TEXT
        self.ui.username.editingFinished.connect(returnuser)#EDITING FINISHED TAKES THE INPUT AFTER THE TEXT BOX IS CLICKED OFF OF

        def recommendMaps():
            number = 0
            recommend_songs=[]
            
            m=recommendinfo()
            m.CalculateMapStars()
            
            checkbox()
            m.mod_change()

            recommend_songs = m.FindMap()
            sorted_list = m.sorter()
            random_number = random.randint(0,len(sorted_list)-1)

            #PLACING THE RECOMMENDATION DATA ON THE SCREEN
            self.ui.title_5.setText(str(recommend_songs[random_number]['title']))#RECOMMENDATION TITLE
            self.ui.title_6.setText(str(round(float(recommend_songs[random_number]['difficultyrating']),2))+'*')#RECOMMENDATION STAR RATING
         
            #CREATING THE INTERACTIVE MAP LINK
            string1 = ('osu://s/'+ str(recommend_songs[random_number]['beatmapset_id']))#RECOMMENDATION MAP LINK
            linkTemplate = '<a href={0}>{1}</a>'
            self.ui.title_7.setOpenExternalLinks(True)#MAKING THE LINK CLICKABLE
            self.ui.title_7.setText(linkTemplate.format(string1, 'map link'))#ADDING TO THE SCREEN

            self.ui.stackedWidget.setCurrentIndex(3)#MOVING SCREEN INDEX TO 3
            
        def checkbox():
            #CHECKING THE CHECK BOX FOR THE MOD CHOICE
            if self.ui.HardRock.isChecked() == True:
                settings.ModChoice = 1
                print('mod choice: Hard Rock')
            elif self.ui.Hidden.isChecked() == True:
                settings.ModChoice = 2
                print('mod choice: Hidden')
            elif self.ui.DoubleTime.isChecked() == True:  
                settings.ModChoice = 3
                print('mod choice: Double Time')
            elif self.ui.Flashlight.isChecked() == True:
                settings.ModChoice = 4
                print('mod choice: Flashlight')
        
        
        #COMMANDS TO HAVE A FUNCTION RUN AFTER A BUTTON PRESS
        self.ui.btn_submit.clicked.connect(recommendMaps)
        self.ui.btn_go.clicked.connect(lambda:scores_click())
        self.ui.btn_go.clicked.connect(loadmaps)

        #DEBUGGING TABLE
        app.setStyleSheet('QWidget { background-image: url(bg.png); } QHeaderView::section { background-color: rgba(0,0,0,0); } QTableWidget QTableCornerButton::section {background-color: rgba(0,0,0,0); }')
       
        
        def scores_click():
            #API REQUEST BASED ON THE USERNAME INPUT FROM THE CODE
            settings.request1 = requests.get(f'https://osu.ppy.sh/api/get_user_recent?k=09fe03d3b80c29a27e0b75b07e0c483c54657817&limit=20&u={str(self._username)}')
            self.ui.stackedWidget.setCurrentIndex(1)#OPENING SCREEN AT INDEX 1, THE LATEST SCORES SCREEN


       
        def moveWindow(event):
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        UIFunctions.uiDefinitions(self)
        self.show()

    def Button(self):
        btnWidget = self.sender()

        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_home")
            UIFunctions.labelPage(self, "Home")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        if btnWidget.objectName() == "btn_new_user":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_new_user")
            UIFunctions.labelPage(self, "New User")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        if btnWidget.objectName() == "btn_widgets":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_widgets)
            UIFunctions.resetStyle(self, "btn_widgets")
            UIFunctions.labelPage(self, "Custom Widgets")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        if btnWidget.objectName() == "btn_go":
           btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet())) 

    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')

    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))

    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())
