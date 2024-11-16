# JARVIS - Personal Voice Assistant 🚀

Welcome to **JARVIS**, your personal voice assistant powered by Python! JARVIS can handle a variety of tasks, from fetching the latest news to managing your emails, all through voice commands. Whether you need a quick fact from Wikipedia, a good laugh, or a simple system command, JARVIS is here to assist you.

---

## 🌟 Features
### Here's what JARVIS can do:
- 🕰️ **Time & Date**: Announces the current time and date.
- 🌐 **Wikipedia Search**: Provides brief summaries from Wikipedia.
- ✉️ **Email Sending**: Send emails using just your voice.
- 🔍 **Web Searches**: 
  - Open websites in Google Chrome.
  - Search on YouTube and Google.
- 📊 **System Monitoring**:
  - Reports CPU usage and battery level.
- 😂 **Jokes**: Tells random jokes to lighten your day.
- 📸 **Screenshots**: Captures and saves screenshots instantly.
- 📝 **Note Taking**: Takes notes and reads them back to you.
- 🧠 **Memory Function**: Remembers and recalls information for you.
- 📰 **News Updates**: Fetches the latest entertainment news headlines.
- 📍 **Location Search**: Opens Google Maps for specific locations.
- 🧮 **WolframAlpha Queries**: Answers factual and computational questions.
- 🖥️ **System Controls**:
  - Shutdown, restart, or log out commands.
  - Temporarily pauses listening for commands.

---

## 🛠️ Technologies Used
- **Python Libraries**:
  - `pyttsx3` - Text-to-speech conversion
  - `datetime` - Date and time handling
  - `speech_recognition` - Speech-to-text conversion
  - `wikipedia` - Wikipedia API
  - `smtplib` - Sending emails
  - `webbrowser` - Opening web pages
  - `psutil` - System and battery details
  - `pyjokes` - Fetching jokes
  - `os` - System operations
  - `pyautogui` - Taking screenshots
  - `json` - JSON handling
  - `requests` - HTTP requests
  - `wolframalpha` - WolframAlpha API for computational queries

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/JARVIS-Voice-Assistant.git
cd JARVIS-Voice-Assistant
```

### 2. Install the Required Packages
Ensure you have Python 3.x installed. Then, run:
```bash
pip install pyttsx3 SpeechRecognition wikipedia smtplib psutil pyjokes pyautogui requests wolframalpha
```

### 3. Configure Email (Optional)
To use the email feature, update the `send_email` function with your credentials:
```python
server.login('your-email@gmail.com', 'your-password')
```

### 4. Run JARVIS
```bash
python jarvis.py
```

---

## 🎤 How to Use
Simply speak commands like:
- **"What's the time?"**
- **"Tell me a joke"**
- **"Search Wikipedia for Python programming"**
- **"Send an email"**
- **"Take a screenshot"**

### Example Voice Commands:
| Command                  | Action                                       |
|--------------------------|----------------------------------------------|
| "What's the time?"      | Announces the current time                   |
| "Search Wikipedia for..."| Provides a summary from Wikipedia            |
| "Tell me a joke"        | Tells a random joke                          |
| "Send email"            | Prompts for email content and recipient      |
| "Shutdown"              | Shuts down your computer                     |

---

## 🙋‍♂️ Contributing
Contributions are welcome! If you have ideas or improvements, feel free to fork the repository and submit a pull request.

---

### ⭐ If you found this project helpful, please give it a star on [GitHub](https://github.com/your-username/JARVIS-Voice-Assistant)! ⭐

--- 

Thank you for checking out **JARVIS**. Let’s make your digital life easier, one command at a time! 🚀💡
