# Sign Language Interpreter App

A web application that captures images from the user's webcam, processes them to recognize sign language gestures, and constructs coherent sentences using OpenAI's GPT API.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Acknowledgments](#acknowledgments)

## Introduction

This application aims to bridge the communication gap by translating sign language gestures into written sentences. It captures images continuously from the user's webcam, processes each image to recognize the sign language gesture, maintains context by keeping track of previously recognized words, and uses OpenAI's GPT to construct coherent sentences.

## Features

- **Real-time Image Capture**: Continuously captures images from the user's webcam every second.
- **Sign Language Recognition**: Processes images to recognize sign language gestures (placeholder function provided).
- **Context Maintenance**: Keeps track of previously recognized words to build sentences.
- **GPT Integration**: Utilizes OpenAI's GPT API to generate coherent sentences from recognized words.
- **Web-Based Interface**: Simple front-end built with HTML, CSS, and JavaScript.
- **Flask Back-End**: Handles image processing, sign language recognition, and communication with GPT API.

## Prerequisites

- **Python 3.6** or higher
- **OpenAI API Key**
- **Webcam**: A functional webcam connected to your computer.
- **Internet Connection**

## Installation

### Clone the Repository

\`\`\`bash
git clone https://github.com/yourusername/sign-language-interpreter.git
cd sign-language-interpreter
\`\`\`

### Back-End Setup

1. **Create a Virtual Environment** (optional but recommended):

   \`\`\`bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   \`\`\`

2. **Install Dependencies**:

   \`\`\`bash
   pip install flask flask_cors openai
   # Include other dependencies like mediapipe and tensorflow if used
   \`\`\`

3. **Set Up Environment Variables**:

   - Create a \`.env\` file in the project root directory:

     \`\`\`bash
     touch .env
     \`\`\`

   - Add your OpenAI API key to the \`.env\` file:

     \`\`\`env
     OPENAI_API_KEY=your_openai_api_key_here
     \`\`\`

   - Alternatively, you can set the environment variable directly in your terminal:

     \`\`\`bash
     export OPENAI_API_KEY=your_openai_api_key_here
     \`\`\`

### Front-End Setup

No additional setup is required for the front-end. Ensure that \`index.html\` and \`script.js\` are in the \`front-end\` directory.

## Usage

### Start the Back-End Server

\`\`\`bash
python app.py
\`\`\`

The Flask server will start running on \`http://localhost:5000\`.

### Serve the Front-End

You can serve the front-end files using any static file server. For example:

\`\`\`bash
cd front-end
python -m http.server 8000
\`\`\`

Access the front-end at \`http://localhost:8000\` in your web browser.

### Using the Application

1. Open \`http://localhost:8000\` in a web browser that supports webcam access (e.g., Chrome, Firefox).
2. Allow the website to access your webcam when prompted.
3. The application will start capturing images every second.
4. Perform sign language gestures in front of your webcam.
5. Open the browser console to see the recognized words and the constructed sentence (you can modify \`index.html\` to display this information on the page).

## Project Structure

\`\`\`
sign-language-interpreter/
├── app.py
├── requirements.txt
├── .env
├── README.md
└── front-end/
    ├── index.html
    └── script.js
\`\`\`

- \`app.py\`: Main Flask application file.
- \`requirements.txt\`: Contains all Python dependencies.
- \`.env\`: Environment variables file (contains the OpenAI API key).
- \`README.md\`: Project documentation.
- \`front-end/\`: Directory containing the front-end files.
  - \`index.html\`: HTML file for the front-end interface.
  - \`script.js\`: JavaScript file handling webcam access and communication with the back-end.

## Acknowledgments

- **OpenAI**: For providing the GPT API used to construct sentences.
- **Flask**: For the web framework used in the back-end.
- **MediaPipe** and **TensorFlow**: If you implement sign language recognition using these libraries.
- **MDN Web Docs**: For documentation on web APIs and JavaScript.
- **Community Contributors**: Anyone who contributes to improving this project.
