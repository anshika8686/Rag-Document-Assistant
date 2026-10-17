from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()

from langchain.chat_models import init_chat_model
model = init_chat_model(
    "groq:openai/gpt-oss-20b"
)
