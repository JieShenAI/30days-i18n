import streamlit as st
from streamlit_chat import message
from streamlit.components.v1 import html

from utils import llm_invoke


def on_input_change():
    user_input = st.session_state.user_input_test
    st.session_state.past.append(user_input)
    content = llm_invoke(user_input)
    st.session_state.generated.append(
        {"type": "normal", "data": content},
    )


def on_btn_click():
    # del st.session_state.past[:]
    st.session_state.past.pop()
    # del st.session_state.generated[:]
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