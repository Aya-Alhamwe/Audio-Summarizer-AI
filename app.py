import gradio as gr
from services.stt_service import transcribe_audio
from services.llm_service import analyze_text # Our modified analysis function
import time
import re  
print("Starting Gradio App...")

def contains_arabic(text):
    """
    Checks if the text contains any Arabic character.
    """
    # Search for any character in the Arabic Unicode range
    return bool(re.search("[\u0600-\u06FF]", str(text)))

def process_meeting_audio(audio_file_path):
    """
    Main function that executes all processing steps.
    """
    if not audio_file_path:
        return "Error: No audio file uploaded."
        
    # --- Step 1: Convert audio to text (Whisper) ---
    print(f"Processing audio file: {audio_file_path}")
    start_time = time.time()
    transcript = transcribe_audio(audio_file_path)
    stt_time = time.time() - start_time
    print(f"STT finished in {stt_time:.2f} seconds.")

    if "Error during transcription" in transcript:
        return transcript

    # --- Step 1.5: Detect text language ---
    if contains_arabic(transcript):
        detected_lang = "ar"
        print("Detected language: Arabic (based on characters)")
    else:
        detected_lang = "en"
        print("Detected language: English (default)")

    # --- Step 2: Summarize/analyze text (Llama 3) ---
    start_time = time.time()
    analysis = analyze_text(transcript, detected_lang) 
    llm_time = time.time() - start_time
    print(f"LLM analysis finished in {llm_time:.2f} seconds.")

    if "Error:" in analysis: 
        return analysis 

    # --- Compile and return final result ---
    final_output = f"""
    ---
    ## 🎙️ Audio Transcription (Raw Text):
    ---
    {transcript}
    
    ---
    ## 🧠 AI Analysis & Key Points:
    ---
    {analysis}
    """
    
    return final_output

# --- Gradio interface setup ---
audio_input = gr.Audio(sources="upload", type="filepath", label="ارفع ملف الاجتماع الصوتي (MP3, WAV)")
output_text = gr.Markdown(label="نتيجة التحليل")

iface = gr.Interface(
    fn=process_meeting_audio, 
    inputs=audio_input,       
    outputs=output_text,      
    title="🤖 مساعد الاجتماعات الذكي (AI Meeting Companion)",
    
 
    description="""
    <div style='text-align: center; font-size: 20px;'><strong>Aya Alhamwi</strong></div>
    <br>
    ارفع ملفاً صوتياً (عربي أو إنجليزي) وسيتم تلخيصه باللغة المناسبة.
    """
)

# --- Launch the app ---
if __name__ == "__main__":
    print("Launching Gradio interface...")
    # يمكنك استخدام 7860 إذا قمت بحل مشكلة البورت العالق
    iface.launch(server_name="0.0.0.0", server_port=7861)