from pynput.mouse import Button, Controller
import sqlite3
from datetime import datetime
import time

class Activity:
    def __init__(self):
        self.timeOnScreen = 0
        self.storedDate = datetime.strftime(datetime.now().date(),"%m/%d/%Y")
        database.addEntry(self.storedDate,self.timeOnScreen)
    
    def tracker(self):
        while True:
            self.currentDate = datetime.strftime(datetime.now().date(),"%m/%d/%Y")
            if self.storedDate != self.currentDate:
               database.addEntry(self.storedDate,self.timeOnScreen)
               self.storedDate = self.currentDate
               self.timeOnScreen = 0
            self.position = mouse.position
            time.sleep(30)
            if self.position != mouse.position:
                self.timeOnScreen += 30
            else:
                pass

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('Tracker.db')
        self.cursor = self.conn.cursor()

    def createTable(self):
        self.cursor.execute("""CREATE TABLE TRACKER
                 (START TEXT,
                 ELAPSED INT);""")
        self.conn.commit()
        

    def addEntry(self,start,time):
        self.cursor.execute("""INSERT INTO TRACKER
                (START, ELAPSED)
                VALUES(?,?);""",(start,time))
        self.conn.commit()
                 
mouse = Controller()
database = Database()
database.createTable()
session = Activity()
session.tracker()
