## Text Summarizer Application

### Overview

The Text Summarizer application is a Python program built using the Tkinter library. It allows users to input text either through manual entry or by uploading a text file. The application then utilizes the PaLM API for text summarization, providing the user with a summarized version of the input text.

### Features

1. **File Upload:**
   - Users can upload a text file through a user-friendly file dialog.

2. **Text Input:**
   - Users can manually input text through a dedicated Text widget.

3. **Text Summarization:**
   - The application utilizes the PaLM API to generate summaries of the input text.
   - Users can customize the summary length (short or long) and tone (casual or formal).

4. **Download Summary:**
   - Users can download the generated summary as a text file.

5. **Text-to-Speech:**
   - The application includes a feature to convert the generated summary into speech using the text-to-speech engine.

6. **Refresh:**
   - Users can clear both the 'Input Text' and 'Summary' Text widgets with the Refresh button.

### Usage

1. **File Upload:**
   - Click the "Browse" button to upload a text file.

2. **Manual Input:**
   - Enter text directly into the "Input Text" Text widget.

3. **Text Summarization:**
   - Customize the summary length and tone using the options provided.
   - Click the "Summarize Text" button to generate a summary.

4. **Download Summary:**
   - Click the "Download Summary" button to save the generated summary as a text file.

5. **Text-to-Speech:**
   - Click the "Speak Text" button to listen to the generated summary.

6. **Refresh:**
   - Click the "Refresh" button to clear both input and summary fields.

### Dependencies

- Python 3.x
- Tkinter
- PaLM API (replace 'your_api_key' with a valid API key)

### Error Handling

- If an error occurs during text summarization (e.g., due to internet issues), an error message will be displayed to the user.

### Notes

- Ensure a valid PaLM API key is provided in the `API_KEY` variable.

### Building the Executable

1. Install the required dependencies.
2. Use a tool like PyInstaller or cx_Freeze to convert the script to an executable file.

**Disclaimer:** This application requires a working internet connection for PaLM API usage. Handle API keys securely, and replace 'your_api_key' with a valid key.

Feel free to customize the application further based on your needs.
