"""
展示我们通过文本分类与实体识别构建的知识图谱

展示文本分类，展示实体抽取，展示知识图谱的一个demo
"""

import streamlit as st
from streamlit_chat import message
from streamlit.components.v1 import html
# from st_pages import add_page_title, get_nav_from_toml

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


ner_user_input = """
你是专门进行实体抽取的专家。请从text中抽取出符合schema定义的实体，不存在的实体类型返回空列表。请按照JSON字符串的格式回答。
    schema: ["主要任务","功能定位","基本遵循","重要项目"]
    text: 积极创建国家级全民健身模范城区，加大体育场馆公益开放力度，启动“智慧共享公共运动场”工程，引入新型体医融合中心
"""

ner_IE = """
实体抽取的结果如下:
```json
{
    "主要任务": [
        "积极创建国家级全民健身模范城区，加大体育场馆公益开放力度，启动“智慧共享公共运动场”工程，引入新型体医融合中心"
    ],
    "功能定位": [],
    "基本遵循": [],
    "重要项目": [
        "“智慧共享公共运动场”工程"
    ]
}
```
"""

cls_user_prompt = """
请将text中的文本分类到domain和summary列出的类别中，若给出类别都不是返回空列表。
    schema: ["主要任务","功能定位","基本遵循","重要项目"]
    text: 积极创建国家级全民健身模范城区，加大体育场馆公益开放力度，启动“智慧共享公共运动场”工程，引入新型体医融合中心
    domain: ['乡村振兴', '生态文明', '社会', '区域协调', '产业', '开放', '城乡规划', '基础设施', '创新', '安全']
    summary: ['成就总结', '机遇挑战', '任务规划']
"""

cls_IE = """
```json
{
    domain: [],
    summary: ["任务规划"]
}
```
"""

st.session_state.setdefault(
    "past",
    [cls_user_prompt, ner_user_input],
)
st.session_state.setdefault(
    "generated",
    [
        {"type": "normal", "data": f"{cls_IE}"},
        {"type": "normal", "data": f"{ner_IE}"},
    ],
)

st.title("知识图谱构建")

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

    # st.button("Clear message", on_click=on_btn_click)

# with st.container():
#     st.text_input("User Input:", on_change=on_input_change, key="user_input_test")

st.markdown(
    """
    通过下述cypher语句，在neo4j中查询上述信息抽取构建的知识图谱:
    ```cypher
    尚待更新
    ```
    """
)


# st.help(get_nav_from_toml)
# st.help(add_page_title)
