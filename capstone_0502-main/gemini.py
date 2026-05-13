import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
# .env에 키가 잘 들어있는지 확인하거나 직접 넣어줘
genai.configure(api_key=os.getenv('AIzaSyCxtCbh-71oRvwl7OuWZmmB8HENbW7U3Zo'))

print("--- 사용 가능한 모델 목록 ---")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
except Exception as e:
    print(f"에러 발생: {e}")
