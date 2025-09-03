import tkinter as tk
from tkinter import messagebox
import requests
import time

# --- Function to Get Weather ---
def getWeather(event=None):
    city = textField.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    api_key = "OPENWEATHER_API_KEY"
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(api)
        json_data = response.json()

        if json_data.get("cod") != 200:
            label1.config(text="❌ City not found!", fg="red")
            label2.config(text="")
            return

        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 273.15)
        min_temp = int(json_data['main']['temp_min'] - 273.15)
        max_temp = int(json_data['main']['temp_max'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        sunrise = time.strftime('%I:%M:%S %p', time.gmtime(json_data['sys']['sunrise'] + json_data['timezone']))
        sunset = time.strftime('%I:%M:%S %p', time.gmtime(json_data['sys']['sunset'] + json_data['timezone']))

        final_info = f"{condition}\n{temp}°C"
        final_data = (
            f"\nMin Temp: {min_temp}°C"
            f"\nMax Temp: {max_temp}°C"
            f"\nPressure: {pressure} hPa"
            f"\nHumidity: {humidity}%"
            f"\nWind Speed: {wind} m/s"
            f"\nSunrise: {sunrise}"
            f"\nSunset: {sunset}"
        )

        label1.config(text=final_info, fg="#222")
        label2.config(text=final_data, fg="#444")

    except Exception as e:
        label1.config(text="⚠️ Error fetching data", fg="red")
        label2.config(text=str(e))


# --- UI Setup ---
canvas = tk.Tk()
canvas.geometry("600x550")
canvas.title("🌤️ Weather App")
canvas.config(bg="#e0f7fa")

# --- Fonts ---
font_title = ("Poppins", 35, "bold")
font_info = ("Poppins", 15, "bold")

# --- Entry Field ---
textField = tk.Entry(canvas, justify='center', width=20, font=font_title, bg="white", fg="black")
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', getWeather)

# --- Get Weather Button ---
btn = tk.Button(canvas, text="Get Weather", command=getWeather, font=font_info, bg="#4dd0e1", fg="white", relief='flat', padx=10, pady=5)
btn.pack(pady=10)

# --- Labels for Output ---
label1 = tk.Label(canvas, font=font_title, bg="#e0f7fa")
label1.pack()

label2 = tk.Label(canvas, font=font_info, justify="left", bg="#e0f7fa")
label2.pack()

canvas.mainloop()

