"""
上传文件与GPT进行交流
"""

import streamlit as st
from streamlit_chat import message
from streamlit.components.v1 import html
# from st_pages import add_page_title, get_nav_from_toml

from utils import llm_invoke

st.title("st.file_uploader")
st.subheader("Input File")
uploaded_file = st.file_uploader("Choose a file")


if uploaded_file is not None:
    file_content = uploaded_file.read().decode("utf-8")  # 读取为字节并解码为字符串
    # st.subheader("File Content")
    # st.text(file_content)  # 显示文件内容
else:
    st.info("☝️ Upload a file")
    file_content = ""


def on_input_change():
    user_input = st.session_state.user_input_test
    st.session_state.past.append(user_input)
    prompt = f"""
    请你基于下述文本回答用户的问题：
    text: {{{{{file_content}}}}}
    user_input: {{{{{user_input}}}}}
    """
    content = llm_invoke(prompt)
    st.session_state.generated.append(
        {"type": "normal", "data": content},
    )


def on_btn_click():
    # del st.session_state.past[:]
    # del st.session_state.generated[:]
    if len(st.session_state.past) > 0:
        st.session_state.past.pop()
        st.session_state.generated.pop()


st.session_state.setdefault(
    "past",
    [],
)
st.session_state.setdefault(
    "generated",
    [],
)

st.title("Chat placeholder")

chat_placeholder = st.empty()

with chat_placeholder.container():
    for i in range(len(st.session_state["generated"])):
        message(st.session_state["past"][i], is_user=True, key=f"{i}_user")
        message(
            st.session_state["generated"][i]["data"],
            key=f"{i}",
            allow_html=True,
            is_table=(
                True if st.session_state["generated"][i]["type"] == "table" else False
            ),
        )

    st.button("Clear message", on_click=on_btn_click)

with st.container():
    st.text_input("User Input:", on_change=on_input_change, key="user_input_test")

# streamlit run llm_chat.py
# 开始写 ChatGPT的对话代码

# st.help(get_nav_from_toml)
# st.help(add_page_title)
