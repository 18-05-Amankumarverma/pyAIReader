# pyAIReader
This bot helps user to read their pdf data and also they can download audio file of that pdf

# Text to Audio Converter

A Django web application that allows users to upload files, extracts text from them, and converts the extracted text into audio. This project is ideal for anyone looking to convert written content into spoken words.

## Features

- Upload files (supports various formats such as .txt, .pdf, .docx)
- Extract text from uploaded files
- Convert extracted text into audio
- Simple and user-friendly interface

## Technologies Used

- Django
- Python
- Text extraction libraries (e.g., `PyPDF2`, `python-docx`)
- Text-to-speech libraries (e.g., `gTTS` or `pyttsx3`)
- HTML/CSS for frontend

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/text-to-audio-converter.git
   cd text-to-audio-converter


   ```
   ### Create a virtual environment:
   > python -m venv venv
   > source venv/bin/activate  # On Windows use `venv\Scripts\activate`

   ### Run the Django development server:
   > python manage.py runserver
   

### Access the application:

#### Open your web browser and go to http://127.0.0.1:8000/.

### Usage

### Navigate to the homepage.
Upload your file using the provided form.
Click on the "Convert" button.
Wait for the audio file to be generated and download it.
Contributing
Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments
Thanks to the contributors of the libraries used in this project.
Inspired by various open-source projects.

### Contact
For any questions or suggestions, feel free to reach out.

Feel free to modify any sections to better fit your project specifics, such as adjusting the technologies or installation steps. Let me know if you need any more help!



