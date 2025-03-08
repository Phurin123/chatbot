import os
from dotenv import load_dotenv
from openai import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate

# โหลดค่า API Key จาก .env
load_dotenv()
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

if not openrouter_api_key:
    raise ValueError("Error: OPENROUTER_API_KEY ไม่ถูกต้อง กรุณาตรวจสอบไฟล์ .env")

def response(user_query):
    # ดึงข้อมูลจากหลายเว็บเพจ
    loader = WebBaseLoader(
        web_paths=(
            "https://en.wikipedia.org/wiki/Health",
            "https://en.wikipedia.org/wiki/Disease",
            "https://en.wikipedia.org/wiki/Medicine",
        ),
    )
    
    try:
        docs = loader.load()
    except Exception as e:
        print(f"⚠️ Warning: ไม่สามารถโหลดข้อมูลจากบางเว็บไซต์ได้: {e}")
        docs = []

    if not docs:
        return "ขออภัย ไม่สามารถโหลดข้อมูลจากเว็บไซต์ได้"

    # ตัดข้อความเป็นส่วนย่อยๆ
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)

    # จำกัดขนาดของ Context (สูงสุด 3000 ตัวอักษร)
    max_context_length = 3000
    formatted_context = "\n\n".join(doc.page_content for doc in splits)[:max_context_length]

    # ใช้ OpenRouter API สำหรับเรียก DeepSeek-R1
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=openrouter_api_key,
    )

    def call_deepseek_r1(query, context):
        try:
            completion = client.chat.completions.create(
                model="deepseek/deepseek-r1:free",
                messages=[
                    {"role": "system", "content": "Use the provided context to answer the query."},
                    {"role": "user", "content": f"Context: {context}\n\nQuery: {query}"},
                ]
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"❌ Error: ไม่สามารถเชื่อมต่อกับ OpenRouter API ได้ ({e})"

    # ส่งไปยัง DeepSeek-R1 ผ่าน OpenRouter
    result = call_deepseek_r1(user_query, formatted_context)

    return result
