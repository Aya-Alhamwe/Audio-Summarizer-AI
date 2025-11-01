from langchain.chat_models import ChatOllama 
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import config  
# --- Initialize the language model ---
def initialize_llm():
    print("Initializing LLM (Ollama/Llama 3 Local)...")
    try:
        llm = ChatOllama(model=config.OLLAMA_MODEL, temperature=0.1)
        print("Ollama LLM initialized successfully.")
        return llm
    except Exception as e:
        print(f"Error initializing Ollama: {e}")
        return None

llm_instance = initialize_llm()

# --- Initialize LLM Chains ---
llm_chain_ar = None
llm_chain_en = None

if llm_instance:
    try:
        # Create Arabic chain
        prompt_template_ar = PromptTemplate(
            input_variables=["context"],
            template=config.PROMPT_TEMPLATE_AR
        )
        llm_chain_ar = LLMChain(llm=llm_instance, prompt=prompt_template_ar)
        print("Arabic LLM chain created.")

        # Create English chain
        prompt_template_en = PromptTemplate(
            input_variables=["context"],
            template=config.PROMPT_TEMPLATE_EN
        )
        llm_chain_en = LLMChain(llm=llm_instance, prompt=prompt_template_en)
        print("English LLM chain created.")
        
    except Exception as e:
        print(f"Error creating LLM chains: {e}")


def analyze_text(context: str, language: str) -> str:
    """
    Receives text and language, selects the appropriate LLM chain.
    """
    print(f"Analyzing text with detected language: {language}")
    
    try:
        if language == "ar" and llm_chain_ar:
            print("Using Arabic LLM chain...")
            result = llm_chain_ar.run(context)
        
        elif llm_chain_en:
            print("Using English LLM chain...")
            result = llm_chain_en.run(context)
        else:
            return "Error: LLM chains are not initialized."

        print("Analysis complete.")
        return result
        
    except Exception as e:
        return f"Error during LLM analysis: {e}"
