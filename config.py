# config.py

# --- Ollama Configuration ---
OLLAMA_MODEL = "llama3"

# --- STT (Whisper) Configuration ---
STT_MODEL_ID = "openai/whisper-small" 
STT_CHUNK_LENGTH_S = 30
STT_BATCH_SIZE = 8

# --- Prompt Templates ---

PROMPT_TEMPLATE_AR = """
<|begin_of_text|><|start_header_id|>system<|end_header_id|>
أنت مساعد ذكي ومحترف لتحليل الاجتماعات.
مهمتك هي قراءة النص المستخرج من الاجتماع التالي، وتلخيص النقاط الرئيسية والقرارات الهامة بوضوح ودقة.
**قاعدة أساسية ومهمة جداً: يجب أن تكون إجابتك باللغة العربية الفصحى فقط، مهما كان النص يحتوي على أخطاء.**
<|eot_id|><|start_header_id|>user<|end_header_id|>
النص المستخرج من الاجتماع:
{context}
<|eot_id|><|start_header_id|>assistant<|end_header_id|>
إليك تحليل النقاط الرئيسية والقرارات:
"""


PROMPT_TEMPLATE_EN = """
<|begin_of_text|><|start_header_id|>system<|end_header_id|>
You are an intelligent and professional assistant for analyzing meetings.
Your task is to read the following meeting transcript, and summarize the key points and important decisions clearly and accurately.
Your response must be in English.
<|eot_id|><|start_header_id|>user<|end_header_id|>
The meeting transcript:
{context}
<|eot_id|><|start_header_id|>assistant<|end_header_id|>
Here is the analysis of the key points and decisions:
"""