import os
import google.generativeai as palm
import pyttsx3
import tkinter as tk
from tkinter import filedialog

API_KEY = 'your_api_key'

palm.configure(api_key=API_KEY)

# Global variables
text = ''
summary = ''


def get_input():
    text = text_box.get("1.0", tk.END)  # Get the input from the Text widget
    print("User Input:", text)  # Print the input to the console
    text_box.delete("1.0", tk.END)  # Delete any existing text in the Text widget
    text_box.insert(tk.END, text)  # Insert the contents of the file into the Text widget


def clear_text():
    text_box.delete("1.0", tk.END)  # Clear the 'Input Text' Text widget
    summary_box.delete("1.0", tk.END)  # Clear the 'Summary' Text widget


# Function to handle file upload
def upload_file():
    global text  # Declare "text" as a global variable so it can be accessed outside of this function
    file_path = filedialog.askopenfilename(initialdir=os.getcwd(),  # Open a file dialog box to select a file to upload
                                           title="Select file",
                                           filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    with open(file_path, 'r', encoding='utf-8') as file:  # Open the selected file in read mode
        text = file.read()  # Read the contents of the file and store them in the "text" variable
        # Do something with the text, such as passing it to a summarization function
        # or displaying it in a Text widget
        print(text)  # Print the contents of the file to the console
        # Insert the text into the Text widget
        text_box.delete("1.0", tk.END)  # Delete any existing text in the Text widget
        text_box.insert(tk.END, text)  # Insert the contents of the file into the Text widget


# Function to download summary to .txt file
def download_summary():
    if summary:  # Check if a summary has been generated
        file_path = filedialog.asksaveasfilename(initialdir=os.getcwd(),  # Open a file dialog box to select where to save the summary file
                                                 title="Save file",
                                                 filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        with open(file_path, 'w', encoding='utf-8') as file:  # Open the file in write mode
            file.write(summary)  # Write the summary to the file
    else:
        tk.messagebox.showerror("Error", "No summary has been generated")


# Function to summarize text
def summarize_text():
    global summary

    try:
        # Determine the desired summary length and tone
        if summary_length_var.get() == '50':
            # Generate a summary using PaLM API
            completion = palm.generate_text(
                model='models/text-bison-001',
                prompt=f"Please with an appropriate heading, summarize the following text into 50 words:\n{text}",
                temperature=0.8,
            )
        elif summary_length_var.get() == '50':
            completion = palm.generate_text(
                model='models/text-bison-001',
                prompt=f"Please with an appropriate heading, summarize the following text into 50 words:\n{text}",
                temperature=0.8,
            )
        elif summary_length_var.get() == '100':
            completion = palm.generate_text(
                model='models/text-bison-001',
                prompt=f"Please with an appropriate heading, summarize the following text into 100 words:\n{text}",
                temperature=0.8,
            )
        elif summary_length_var.get() == '100':
            completion = palm.generate_text(
                model='models/text-bison-001',
                prompt=f"Please with an appropriate heading, summarize the following text into 100 words:\n{text}",
                temperature=0.8,
            )

        # Extract the generated summary from the PaLM API response
        summary = completion.result

        # Display the generated summary in the 'Summary' Text widget
        summary_box.delete("1.0", tk.END)
        summary_box.insert(tk.END, summary)

        # Print the generated summary to the console
        print(summary)

    except Exception as e:
        # Handle the exception and show an error message to the user
        error_message = f"An error occurred: {str(e)}"
        tk.messagebox.showerror("Error", error_message)


# Create a text-to-speech engine
engine = pyttsx3.init()


# Function to speak the text entered in the Text widget
def speak_text():
    # Get the summary from the 'Summary' Text widget
    speech = summary_box.get("1.0", tk.END)
    # Speak the text using the text-to-speech engine
    engine.say(speech)

    # Set the speaking rate to 120
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 120)

    # Get details of the current voice and set it to a female voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    # Run the text-to-speech engine to speak the text
    engine.runAndWait()


root = tk.Tk()
root.title("Text Summarizer")

# Set the window size to 1200x800
root.geometry("1920x1080")

# Set background color to dark gray
root.configure(bg="#333333")

# Create header label with white text on dark gray background
header = tk.Label(root, text="Text Summarizer", pady=30, font=("Arial", 36, "bold"), bg="#333333", fg="white")
header.pack()

# Create frame for file upload
file_upload_frame = tk.Frame(root, pady=10, bg="#333333")
file_upload_frame.pack()

# Create label for file upload button with white text on dark gray background
file_upload_label = tk.Label(file_upload_frame, text="Upload text file", font=("Arial", 14), bg="#333333", fg="white")
file_upload_label.pack(side=tk.LEFT)

# Create file upload button with gray background
file_upload_button = tk.Button(file_upload_frame, text="Browse", font=("Arial", 14), relief=tk.GROOVE, bd=2, bg="#999", command=upload_file)
file_upload_button.pack(side=tk.LEFT, padx=(20, 0))

# Create a button to clear both the 'Input Text' and 'Summary' Text widgets
refresh_button = tk.Button(file_upload_frame, text="Refresh", font=("Arial", 14), relief=tk.GROOVE, bd=2, bg="#87CEEB", command=clear_text)
refresh_button.pack(side=tk.LEFT, padx=(20, 0))

# Create frame for summarization options
options_frame = tk.Frame(root, pady=10, bg="#333333")
options_frame.pack()

# Create summary length selection with white text on dark gray background
summary_length_label = tk.Label(options_frame, text="Select summary length:", font=("Arial", 14), bg="#333333", fg="white")
summary_length_label.pack(side=tk.LEFT)

summary_length_var = tk.StringVar(value=50)

summary_length_50_rb = tk.Radiobutton(options_frame, text="Short (30-100 words)", variable=summary_length_var, value="50", font=("Arial", 14), bg="#333333", fg="white", selectcolor="black")
summary_length_100_rb = tk.Radiobutton(options_frame, text="Long (100-200 words)", variable=summary_length_var, value="100", font=("Arial", 14), bg="#333333", fg="white", selectcolor="black")

summary_length_50_rb.pack(side=tk.LEFT, padx=(20, 0))
summary_length_100_rb.pack(side=tk.LEFT)


# Create text box widget to display text result with white text on dark gray background
text_box_label = tk.Label(root, text="Input Text", font=("Arial", 18, "bold"), bg="#333333", fg="white")
text_box_label.pack(pady=(10, 10))

text_box = tk.Text(root, height=15, width=80, font=("Arial", 14), bg="#222", fg="white")
text_box.pack()

summary_box_label = tk.Label(root, text="Summary", font=("Arial", 18, "bold"), bg="#333333", fg="white")
summary_box_label.pack(pady=(10, 10))

summary_box = tk.Text(root, height=10, width=100, font=("Arial", 14), bg="#222", fg="white")
summary_box.pack()

# Create button for text summarization
summarize_button = tk.Button(root, text="Summarize Text", font=("Arial", 18), relief=tk.GROOVE, bd=2, bg="#999", command=summarize_text)
summarize_button.pack(side=tk.LEFT, pady=15, padx=(570, 0))

summary_download_button = tk.Button(root, text="Download Summary", font=("Arial", 18), relief=tk.GROOVE, bd=2, bg="#999", command=download_summary)
summary_download_button.pack(side=tk.LEFT, pady=15, padx=(100, 100))

# Create a button to speak the text entered in the Text widget
speak_button = tk.Button(root, text="Speak Text", font=("Arial", 18), relief=tk.GROOVE, bd=2, bg="#999", command=speak_text)
speak_button.pack(side=tk.LEFT, pady=15, padx=(0, 0))

root.mainloop()

