import tkinter as tk
import requests
import time

def getWeather(canvas):
    city = textField.get()
    API_key = "49220c923e0faf9700102428a6405cd3"  # you should add your own api key
    api = fr"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    temp_min = int(json_data['main']['temp_min'] - 273.15)
    temp_max = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind_speed = json_data['wind']['speed']
    sunrise = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 19800))  # the difference is your time zone difference in seconds
    sunset = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunset'] - 19800))  # the difference is your time zone difference in seconds

    final_info = condition + "\n" + str(temp)+"°C"
    final_data = "\n"+"Max Temp: "+str(temp_max)+"\n"+"Min Temp: "+str(temp_min)+"\n"+"Pressure: "+str(pressure)+"\n"+"Humidity: "+str(humidity)+"\n"+"Wind Speed: "+str(wind_speed)+"\n"+"Sunrise: "+sunrise+"\n"+"Sunset: "+sunset
    label1.config(text=final_info)
    label2.config(text=final_data)

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(canvas, justify='center', font=t)
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t)
label1.pack()

label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()
