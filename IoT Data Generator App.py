import wx
import pandas as pd
import numpy as np
import random
import json
import os
import matplotlib.pyplot as plt
from faker import Faker
from datetime import datetime,timedelta

class IoTDataGenerator(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(IoTDataGenerator, self).__init__(*args, **kwargs)

        self.fake = Faker()
        self.user_data = pd.DataFrame()
        self.sensor_data = pd.DataFrame()

        self.Centre()
        self.basicGUI()

    def basicGUI(self):
        panel = wx.Panel(self)
        menuBar = wx.MenuBar()

        fileMenu = wx.Menu()
        generateItem = fileMenu.Append(wx.ID_ANY, 'Generate IoT', 'Generate IoT data')
        saveJsonItem = fileMenu.Append(wx.ID_ANY, 'Save JSON', 'Save data as JSON')
        saveCsvItem = fileMenu.Append(wx.ID_ANY, 'Save CSV', 'Save data as CSV')
        exitItem = fileMenu.Append(wx.ID_EXIT, 'Exit', 'Exit program')

        statsMenu = wx.Menu()
        descriptiveItem = statsMenu.Append(wx.ID_ANY, 'Descriptive', 'Show descriptive statistics')
        plotAItem = statsMenu.Append(wx.ID_ANY, 'Plot A', 'Show histogram of outside temperature')
        plotBItem = statsMenu.Append(wx.ID_ANY, 'Plot B', 'Show line graph of outside vs room temperature')
        plotCItem = statsMenu.Append(wx.ID_ANY, 'Plot C', 'Show histogram of ALL temperature and humdity')

        menuBar.Append(fileMenu, 'File')
        menuBar.Append(statsMenu, 'Statistics')
        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.GenerateData, generateItem)
        self.Bind(wx.EVT_MENU, self.SaveJSON, saveJsonItem)
        self.Bind(wx.EVT_MENU, self.SaveCSV, saveCsvItem)
        self.Bind(wx.EVT_MENU, self.Exit, exitItem)
        self.Bind(wx.EVT_MENU, self.DescriptiveStats, descriptiveItem)
        self.Bind(wx.EVT_MENU, self.PlotA, plotAItem)
        self.Bind(wx.EVT_MENU, self.PlotB, plotBItem)
        self.Bind(wx.EVT_MENU, self.PlotC, plotCItem)

    def GenerateData(self, event):
        self.user_data = pd.DataFrame()
        self.sensor_data = pd.DataFrame()
        users = []
        sensors = []

        start_date = datetime(2015, 1, 1)
        end_date = datetime.now()
        delta = timedelta(hours=6)
        timesamples = []

        while start_date <= end_date:
            timesamples.append(start_date)
            start_date += delta

        for i in range(1000):
            user_id = i + 1
            user = {
                'user_id': user_id,
                'firstname': self.fake.first_name(),
                'lastname': self.fake.last_name(),
                'age': random.randint(18, 90),
                'gender': random.choice(['Male', 'Female']),
                'username': self.fake.user_name(),
                'address': self.fake.address().replace('\n', ', '),
                'email': self.fake.email()
            }
            users.append(user)

            for ts in timesamples[:1000]:
                outside_temp = random.uniform(70, 95)
                outside_humidity = random.uniform(50, 95)
                room_temp = outside_temp - random.uniform(0, 10)
                room_humidity = outside_humidity - random.uniform(0, 10)

                sensors.append({
                    'user_id': user_id,
                    'date': ts.date(),
                    'time': ts.time(),
                    'outside_temp': round(outside_temp, 2),
                    'outside_humidity': round(outside_humidity, 2),
                    'room_temp': round(room_temp, 2),
                    'room_humidity': round(room_humidity, 2)
                })

        self.user_data = pd.DataFrame(users)
        self.sensor_data = pd.DataFrame(sensors)
        wx.MessageBox('IoT Data Generated Successfully!', 'Success')

    def SaveJSON(self, event):
        with wx.FileDialog(self, "Save JSON file", wildcard="JSON files (*.json)|*.json", style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            path = fileDialog.GetPath()
            self.sensor_data.to_json(path, orient='records', indent=2)

    def SaveCSV(self, event):
        with wx.FileDialog(self, "Save CSV file", wildcard="CSV files (*.csv)|*.csv", style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            path = fileDialog.GetPath()
            self.sensor_data.to_csv(path, index=False)

    def Exit(self, event):
        self.Close(True)

    def DescriptiveStats(self, event):
        if self.sensor_data.empty:
            wx.MessageBox('No data generated.', 'Error')
            return
        stats = self.sensor_data.describe().to_string()
        wx.MessageBox(stats, 'Descriptive Statistics')

    def PlotA(self, event):
        if self.sensor_data.empty:
            wx.MessageBox('Generate IoT data first.', 'Error')
            return
        plt.figure()
        self.sensor_data['outside_temp'].hist(bins=30)
        plt.title('Histogram of Outside Temperature')
        plt.xlabel('Temperature')
        plt.ylabel('Frequency')
        plt.show()

    def PlotB(self, event):
        if self.sensor_data.empty:
            wx.MessageBox('Generate IoT data first.', 'Error')
            return
        plt.figure()
        sample = self.sensor_data.sample(1000)
        plt.plot(sample['outside_temp'], label='Outside Temp')
        plt.plot(sample['room_temp'], label='Room Temp')
        plt.legend()
        plt.title('Outside vs Room Temperature')
        plt.xlabel('Sample Index')
        plt.ylabel('Temperature')
        plt.show()

    def PlotC(self, event):
        if self.sensor_data.empty:
            wx.MessageBox('Generate IoT data first.', 'Error')
            return
        plt.figure()
        self.sensor_data[['outside_temp', 'room_temp', 'outside_humidity', 'room_humidity']].hist(bins=30, layout=(2, 2))
        plt.tight_layout()
        plt.suptitle('Temperature and Humidity Histograms')
        plt.show()

def main():
    app = wx.App()
    frame = IoTDataGenerator(None, size=(800, 600))
    frame.Show()
    app.MainLoop()

if __name__ == "__main__":
    main()
