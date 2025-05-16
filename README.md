# STT Whisper

A simple Streamlit web application that uses OpenAI's Whisper model to transcribe speech from audio files into text. Upload your `.wav` or `.mp3` audio files and get accurate transcriptions quickly and easily.

## Features

- Upload `.wav` or `.mp3` audio files for transcription
- Playback uploaded audio within the app
- Transcription powered by OpenAI's Whisper "base" model
- View transcription results in a text area
- Download the transcription as a `.txt` file

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd stt-whisper
   ```

2. (Optional but recommended) Create and activate a virtual environment using cmd:
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the Streamlit app with the following command:

```bash
streamlit run app.py
```

This will open a local web interface where you can upload audio files and get transcriptions.

## Supported Audio Formats

- WAV (`.wav`)
- MP3 (`.mp3`)

## How to Use

1. Click on the "Browse files" button to upload an audio file.
2. The app will play the uploaded audio.
3. The transcription process will start automatically.
4. Once complete, the transcription text will be displayed.
5. You can download the transcription as a `.txt` file using the download button.

## Dataset

This app can be used with any audio dataset. Example audio files are included in the `audio_dataset/` directory for testing.

To use or test the application with a larger audio mp3 dataset, please install the dataset from the following link:  
https://commonvoice.mozilla.org/en/datasets

## Outputs

Transcriptions are displayed in the app and can be downloaded as text files.

## Requirements

- Python 3.7+
- Streamlit
- OpenAI Whisper model dependencies (see `requirements.txt`)

## License

This project is licensed under the MIT License.
