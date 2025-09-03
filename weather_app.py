import tkinter as tk
from tkinter import ttk, messagebox
import requests
from datetime import datetime
import ttkbootstrap as tb  

API_KEY = "YOUR_API_KEY"  # replace with your OpenWeather API key


# ---------------- Emoji Mapper ----------------
def get_weather_emoji(desc):
    desc = desc.lower()
    if "clear" in desc: return "☀️"
    if "cloud" in desc: return "☁️"
    if "rain" in desc: return "🌧️"
    if "snow" in desc: return "❄️"
    if "thunder" in desc: return "⛈️"
    return "🌍"


# ---------------- Fetch Weather ----------------
def get_weather():
    city = city_var.get().strip()
    if not city:
        messagebox.showwarning("⚠️", "Please enter a city name")
        return

    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        data = requests.get(url).json()

        if data.get("cod") != 200:
            messagebox.showerror("Error", "City not found!")
            return

        city_name = f"{data['name']}, {data['sys']['country']}"
        temp = data["main"]["temp"]
        feels = data["main"]["feels_like"]
        condition = data["weather"][0]["description"].title()
        emoji = get_weather_emoji(condition)

        city_label.config(text=f"📍 {city_name}")
        temp_label.config(text=f"🌡️ {temp:.1f}°C")
        feels_label.config(text=f"🤔 Feels Like {feels:.1f}°C")
        cond_label.config(text=f"{emoji} {condition}")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------- UI ----------------
root = tk.Tk()
root.title("🌤️ Weather App")
root.geometry("400x350")
root.configure(bg="#87CEEB")  # Sky Blue background

# --- Header Bar ---
header = tk.Frame(root, bg="#FFD43B", height=50)
header.pack(fill="x")
title = tk.Label(header, text="Weather App", bg="#FFD43B", fg="black",
                 font=("Arial", 16, "bold"))
title.pack(pady=10)

# --- Search Frame ---
search_frame = tk.Frame(root, bg="#87CEEB")
search_frame.pack(pady=10)

city_var = tk.StringVar()
city_entry = tk.Entry(search_frame, textvariable=city_var,
                      font=("Arial", 12), width=20)
city_entry.grid(row=0, column=0, padx=5)

btn = tk.Button(search_frame, text="Get Weather",
                bg="#FFD43B", fg="black", font=("Arial", 10, "bold"),
                command=get_weather)
btn.grid(row=0, column=1, padx=5)

# --- Card (white box) ---
card = tk.Frame(root, bg="#FFF8DC", bd=2, relief="ridge")
card.pack(pady=20, padx=20, fill="both")

city_label = tk.Label(card, text="📍 City, Country",
                      bg="#FFF8DC", fg="black", font=("Arial", 12, "bold"))
city_label.pack(pady=5)

temp_label = tk.Label(card, text="🌡️ --°C",
                      bg="#FFF8DC", fg="black", font=("Arial", 14))
temp_label.pack(pady=5)

feels_label = tk.Label(card, text="🤔 Feels Like --°C",
                       bg="#FFF8DC", fg="black", font=("Arial", 12))
feels_label.pack(pady=5)

cond_label = tk.Label(card, text="☀️ Condition",
                      bg="#FFF8DC", fg="black", font=("Arial", 12))
cond_label.pack(pady=5)

root.mainloop()

