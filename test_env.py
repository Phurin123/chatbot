import os
from dotenv import load_dotenv, find_dotenv

env_path = find_dotenv(".env")  # ค้นหาไฟล์อัตโนมัติ
load_dotenv(env_path)

print("OPENROUTER_API_KEY:", os.getenv("OPENROUTER_API_KEY"))
