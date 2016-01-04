import datetime
from Tkinter import *
import tkMessageBox
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

root = Tk()
textBox = Entry(root, width=40)
textBox.pack()

time_re = re.compile("(59:00|2[0-5]:[0-5][0-9]|[0-5][0-9]:[0-5][0-9])")

class YT_Playlist_Calculator:

    count = 0
    total = datetime.timedelta()
    loadMores = 0

    def __init__(self):
        button = Button(root, text='Calculate Total Runtime', width=40, command = self.ytCalc).pack()
        root.title("Youtube Playlsit Calculator")

    def bigPlaylistCheck(self, text):
        isLoadMore = False
        text = open("source.txt", "r")
        for line in text:
            if "Load more" in line:
                self.loadMores += 1
                isLoadMore = True
        return isLoadMore

    def addTime(self, time):
        (h, m, s) = time.split(':')
        s = datetime.timedelta(hours = int(h), minutes = int(m), seconds = int(s))
        self.total += s
        self.count += 1
        print s

    def ytCalc(self):
        url = textBox.get()
        driver = webdriver.Firefox()
        driver.get(url)
        offSet = 313
        oldLoadMores = 0

        elem = driver.find_element_by_xpath("//*")
        source_code = elem.get_attribute("outerHTML")
        text_file = open("source.txt", "w")
        text_file.write(source_code.encode('utf8'))
        text_file = open("source.txt", "r")

        while self.bigPlaylistCheck(text_file):
            if (self.loadMores > oldLoadMores):
                oldLoadMores = self.loadMores
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #Scroll to bottom of the page
                loadMoreXpath = "(//button[@type='button'])[]" #Xpath to 'Load more' button
                loadMoreXpath = loadMoreXpath[:27] + str(offSet) + loadMoreXpath[27:]
                loadMoreButton = WebDriverWait(driver, 50).until(lambda driver: driver.find_element_by_xpath(loadMoreXpath))
                import time
                time.sleep(2)
                loadMoreButton.click()
                time.sleep(2)
                offSet += 300
                elem = driver.find_element_by_xpath("//*")
                source_code = elem.get_attribute("outerHTML")
                text_file = open("source.txt", "w")
                text_file.write(source_code.encode('utf8'))
                text_file = open("source.txt", "r")
            else:
                break


        for line in text_file:
            if ("hour,") in line:
                possibleTime = line.split("minutes")[-1].split()[0]
                if len(possibleTime) > 5:
                    time = str(0) + possibleTime[2] + possibleTime[3] + possibleTime[4] + possibleTime[5] + possibleTime[6] + possibleTime[7] + possibleTime[8]
                    if time_re.match(str(time)):
                        self.addTime(time)

            elif ("hours,") in line:
                possibleTime = line.split("minutes")[-1].split()[0]
                if len(possibleTime) > 5:
                    time = str(0) + possibleTime[2] + possibleTime[3] + possibleTime[4] + possibleTime[5] + possibleTime[6] + possibleTime[7] + possibleTime[8]
                    if time_re.match(str(time)):
                        self.addTime(time)

            elif "hours" in line:
                possibleTime = line.split("hours")[-1].split()[0]
                if len(possibleTime) > 5:
                    time = possibleTime[2] + possibleTime[3] + possibleTime[4] + possibleTime[5] + possibleTime[6] + possibleTime[7] + possibleTime[8] + possibleTime[9]
                    if time_re.match(str(time)):
                        self.addTime(time)


            elif ("minutes" and "seconds") in line:
                possibleTime = line.split("seconds")[-1].split()[0]
                if len(possibleTime) > 5:
                    time = str(0) + str(0) + ':' + str(0) + possibleTime[2] + possibleTime[3] + possibleTime[4] + possibleTime[5]
                    if time_re.match(str(time)):
                        self.addTime(time)

            elif "second" in line:
                possibleTime = line.split("second")[-1].split()[0]
                if len(possibleTime) > 5:
                    time = str(0) + str(0) + ':' + str(0) + possibleTime[2] + possibleTime[3] + possibleTime[4] + possibleTime[5]
                    if time_re.match(str(time)):
                        self.addTime(time)

            elif ("minutes" or "minute") in line:
                possibleTime = line.split("minutes")[-1].split()[0]
                if len(possibleTime) > 5:
                    time = str(0) + str(0) + ':' + possibleTime[2] + possibleTime[3] + possibleTime[4] + possibleTime[5] + possibleTime[6]
                    time2 = str(0) + str(0) + ':' + str(0) + possibleTime[2] + possibleTime[3] + possibleTime[4] + possibleTime[5]
                    if time_re.match(str(time)):
                        self.addTime(time)
                    elif time_re.match(str(time2)):
                        self.addTime(time2)

            # TODO: Cases were video is over an hour (hour + minute/minutes/second/seconds/nothing, hours + second/seconds/minutes/minute/nothing)!

        text_file.close()

        tkMessageBox.showinfo("Total","Total Playlist Time = " + str(self.total) + " Videos in playlist = " + str(self.count))
        self.count = 0
        self.total = datetime.timedelta();

program = YT_Playlist_Calculator()
root.mainloop()
