--🖥️ Desktop Reminder App

A simple Python GUI application that allows users to set reminders for tasks or events. When the set time is reached, the app shows a pop-up notification with a sound alert.

---

## Features

- ⏰ Set custom reminders for any task or event
- 🕒 Enter time in 12-hour format (HH:MM) with AM/PM dropdown
- 🔊 Sound notification when reminder triggers
- 💬 Pop-up message to display the task
- 🚀 Runs in the background using threading

---

## Technologies Used

- **Python 3**
- **Tkinter** – for building the GUI
- **Threading** – for background reminder checking
- **Datetime** – for time comparison
- **Playsound** – to play notification sound

---

## How to Run

1. **Install Python 3** (if not already installed)

2. **Install the required library**

```bash
pip install playsound
```

3. **Run the script**

```bash
python reminder_app.py
```

---

## Reminder Format

- Enter **hour** and **minute** separately
- Select **AM** or **PM** from dropdown
- Type your reminder message
- Click **"Set Reminder"**

At the chosen time, a sound plays and a pop-up displays your message.

---

## 📁 Files

- `reminder_app.py` – Main application file
- `notification.mp3` – (Optional) Sound file used for alert
- `README.md` – Project documentation

---

## 📃 License

This project is open source and free to use under the [MIT License](LICENSE).

---

## 👩‍💻 Author

**Kashish Arora**  
MCA Student | Data Enthusiast | Python Developer
