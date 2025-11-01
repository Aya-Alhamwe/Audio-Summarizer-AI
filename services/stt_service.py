from transformers import pipeline
import config 

# Initialize the STT model once at startup to save time
print("Loading STT (Whisper) model...")
try:
    stt_pipeline = pipeline(
        "automatic-speech-recognition",
        model=config.STT_MODEL_ID,
        chunk_length_s=config.STT_CHUNK_LENGTH_S,
    )
    print("STT model loaded successfully.")
except Exception as e:
    print(f"Error loading STT model: {e}")
    stt_pipeline = None

def transcribe_audio(audio_file_path: str) -> str:
    """
    Receives an audio file path and converts it to text using Whisper.
    """
    if stt_pipeline is None:
        return "Error: Speech-to-Text model is not loaded."
        
    try:
        print(f"Transcribing audio: {audio_file_path}")
        # Analyze the audio file using the model
        result = stt_pipeline(audio_file_path, batch_size=config.STT_BATCH_SIZE)
        
        transcript_text = result["text"]
        print("Transcription complete.")
        return transcript_text
        
    except Exception as e:
        print(f"Error during transcription: {e}")
        return f"Error during transcription: {e}"
