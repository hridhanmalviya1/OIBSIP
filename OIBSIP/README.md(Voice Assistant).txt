# Voice Assistant in Python

## 📌 Project Overview

This project is a simple voice assistant developed using Python. It listens to the user's voice commands, recognizes speech, and responds through spoken output.

## 🎯 Objectives

* Capture voice input through a microphone.
* Convert speech into text using speech recognition.
* Respond to basic voice commands.
* Generate spoken responses using text-to-speech.

## 🛠️ Technologies Used

* **Python** – Core programming language
* **SpeechRecognition** – Speech-to-text conversion
* **PyAudio** – Microphone input
* **pyttsx3** – Text-to-speech output
* **Google Speech Recognition** – Online speech recognition service used by the project

## ⚙️ Features

* Voice input through a microphone
* Speech recognition
* Spoken responses
* Greeting response for “hello”
* Exit response for “goodbye”

## 📂 Project Structure

```text
Voice-Assistant/
├── voice_assistant.py
├── README.md
└── requirements.txt
```

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Voice-Assistant
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Install Dependencies

Make sure Python is installed, then run:

```bash
python -m pip install SpeechRecognition pyttsx3 pyaudio
```

### 3. Run the Project

```bash
python voice_assistant.py
```

If the `python` command does not work on Windows, try:

```bash
py voice_assistant.py
```

## 🗣️ Example Usage

* **User:** Hello

* **Assistant:** Hello! How can I assist you?

* **User:** Goodbye

* **Assistant:** Goodbye!

*Responses depend on the commands implemented in the Python code.*

## 📚 Learning Outcomes

* Understanding Python libraries for speech recognition
* Working with microphone input
* Implementing text-to-speech functionality
* Handling basic voice commands
* Learning the fundamentals of voice-based human-computer interaction

## 🔮 Future Improvements

* Add more voice commands
* Integrate a weather or web-search feature
* Add a date and time announcement
* Improve error handling for unclear speech
* Integrate an AI model for more flexible conversations

## 👨‍💻 Author

**Hridhan Malviya**

## 📝 Note

This project was developed as an internship task to practice Python programming and basic voice-assistant development.
