import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv()
key = os.environ.get("API_KEY")
url = os.environ.get("BASE_URL")


def llm_invoke(text):
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        base_url=url,
        api_key=key,  # 在这里填入你的密钥
    )
    return llm.invoke(text).content


if __name__ == "__main__":
    content = llm_invoke("Hello, who are you?")
    print(content)
