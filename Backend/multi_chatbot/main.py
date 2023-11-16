import sys
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.document_loaders import TextLoader
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import DirectoryLoader
from langchain.prompts import PromptTemplate
from streamlit_chat import message
from langchain.embeddings import HuggingFaceBgeEmbeddings
# from InstructorEmbedding import INSTRUCTOR
from langchain.chains import ConversationalRetrievalChain
from dotenv import load_dotenv
import openai
import os
import streamlit as st
import json
from streamlit_lottie import st_lottie
from streamlit.components.v1 import html
load_dotenv()  # take environment variables from .env (especially openai api key)


api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = api_key
# Create Google Palm LLM model
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5,
                 openai_api_key=api_key)

vectordb_file_path = "faiss_index"
# Dedfining  the embedding model:
# model_name = "BAAI/bge-base-en"
# encode_kwargs = {'normalize_embeddings': True} # set True to compute cosine similarity

# model_norm = HuggingFaceBgeEmbeddings(
#     model_name=model_name,
#     model_kwargs={'device': 'cpu'},
#     encode_kwargs=encode_kwargs
# )

# ## Using the new embedding model:
# embeddings = model_norm

embeddings = OpenAIEmbeddings()

# def create_vector_db():
#         loader = DirectoryLoader('data/', glob="*.pdf", loader_cls=PyPDFLoader)
#         data = loader.load()

#         text_splitter  = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
#         text_chunks = text_splitter.split_documents(data)

#         # Create a FAISS instance for vector database from 'data'
#         vectordb = FAISS.from_documents(documents=text_chunks,
#                                         embedding=embeddings)

#         # Save vector database locally
#         vectordb.save_local(vectordb_file_path)


vectordb = FAISS.load_local(vectordb_file_path, embeddings)
# Create a retriever for querying the vector database
retriever = vectordb.as_retriever(score_threshold=0.7)
prompt_template = """As a Helpful agent specializing in retirement planning, utilize the provided context to generate detailed responses. Give response about the startup ideas based on users past/present Field of work if Provided (the best 5) in Structured format. Strive to maximize the inclusion of text from the "response" section of the source document, minimizing alterations.Structure the response in good manner , like showing the response in points/bullet-points.
CONTEXT: {context}
QUESTION: {question}"""
PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)

memory = ConversationBufferMemory(
    memory_key="chat_history", return_messages=True)


chain = ConversationalRetrievalChain.from_llm(llm=llm,
                                              chain_type="stuff",
                                              retriever=retriever,
                                              # input_key="query",
                                              # return_source_documents=True,
                                              memory=memory,
                                              combine_docs_chain_kwargs={"prompt": PROMPT})

#-------------------------------------------------------------------------------------------------------------------------------------

def load_lottiefile(filepath: str):
    with open(filepath, "r") as file:
        return json.load(file)


st.set_page_config(
    page_title="Chatbot-Advisor",
    page_icon=":books:",
    layout="wide",
    initial_sidebar_state="expanded"

)


#-------------------------------------------------------------------------------------------------------------------------------------


left_column, right_column = st.columns([1,3])
with st.container():
    with left_column:
        lottie = load_lottiefile('../assets/Animation.json')
        st_lottie(lottie, key="hello")


    # Column 2: Display text explaining chatbot with enhanced UI

    with right_column:
        st.markdown(
            """
            <div style="background-color: #d4cbb1; padding: 20px; border-radius: 10px; box-shadow: 5px 5px 15px #888888;margin-top: 50px;">
                <h2 style="color: #3d405b;">Chatbot Overview</h2>
                <p style="color: #3d405b;font-size:1.2rem">
                    This chatbot is designed to assist you with various tasks.
                    Feel free to ask questions or seek help on a wide range of topics.
                    The enhanced UI provides a user-friendly experience for interaction.You can ask anything related to retirement planning , about mental ans social health , Buiness/startup ideas during/after retirement etc
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

#-------------------------------------------------------------------------------------------------------------------------------------


st.title("Retirement Assistant!")
def conversation_chat(query):
    try:
        result = chain(
            {"question": query, "chat_history": st.session_state['history']})
        st.session_state['history'].append((query, result["answer"]))
        return result["answer"]
    except ValueError as ve:
        print("ValueError:", ve)
        print("Input query:", query)
        print("Chat history:", st.session_state['history'])


def initialize_session_state():
    if 'history' not in st.session_state:
        st.session_state['history'] = []
    if 'generated' not in st.session_state:
        st.session_state['generated'] = ["Hello! Ask me anything"]
    if 'past' not in st.session_state:
        st.session_state['past'] = ["Hey! 👋"]
    if 'audio_recorder' not in st.session_state:
        st.session_state['audio_recorder'] = {}

def message(content, is_user=False, key=None, avatar_style=None):
    background_color = "#aed6f1" if is_user else "#d4cbb1"
    st.markdown(
        f'<div style="display: flex; margin-bottom: 10px;">'
        f'<div style="width: 50px; height: 50px; border-radius: 25px; background-color: lightblue; display: flex; align-items: center; justify-content: center; margin-right: 10px;">'
        f'{ "👤" if is_user else "🤖"}</div>'
        f'<div style="flex: 1; padding: 10px; border-radius: 10px; background-color: {background_color}; color: black;">'
        f'{content}'
        f'</div></div>',
        unsafe_allow_html=True
    )
def display_chat_history():
    reply_container = st.container()
    container = st.container()
    with container:
        with st.form(key='my_form', clear_on_submit=True):

            sample_questions = [
                "What are the best startup/business ideas after the retirement",
                "What are steps to be taken for Retirement Planning",
                "Plot the stock price for Microsoft.",
                "What all things I can do during me retirement"
            ]

            selected_question = st.selectbox(":blue[Select a sample question:]", sample_questions)

            user_input = st.text_input(
                ":blue[Question:]", placeholder="Ask any thing about Your retirement", key='input')
            submit_button = st.form_submit_button(label='Send')
        if submit_button:
            input_text = user_input if user_input else selected_question
            output = conversation_chat(input_text)
            st.session_state['past'].append(input_text)
            st.session_state['generated'].append(output)
    if st.session_state['generated']:
        with reply_container:
            for i in range(len(st.session_state['generated'])):
                message(st.session_state["past"][i], is_user=True, key=str(
                    i) + '_user')
                message(st.session_state["generated"]
                        [i], key=str(i))


# Initialize session state
initialize_session_state()
# Display chat history
display_chat_history()

#-------------------------------------------------------------------------------------------------------------------------------------


footer = """
<style>
    .footer {
        width: 100%;
        background-color: #f4f4f4;
        padding: 10px;
        text-align: center;
        color: black;
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
    }
</style>
<div class="footer">
    <p>© 2023 Stock-Bot. All rights reserved.</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)

#-------------------------------------------------------------------------------------------------------------------------------------


custom_css = """

    .section-header {
        color: #d4cbb1;
        font-size: 18px;
        
        margin-bottom: 10px;
    }

    .bullet-point {
        color: #3d405b;
        margin-left: 15px;
    }
"""

# Apply the custom CSS
st.markdown(f'<style>{custom_css}</style>', unsafe_allow_html=True)

# Sidebar content
st.sidebar.header("Chatbot Information")
st.sidebar.markdown(
    """
    Welcome to the Retirement Assistant Chatbot! 🌟

    This chatbot is here to support you with various tasks related to retirement, including:
    """
)

# Dynamic sections
sections = {
    "Health and Wellness": [
        "Offer advice on maintaining physical health through exercise.",
        "Provide information on mental health resources for retirees."
    ],
    "Hobbies and Leisure": [
        "Recommend leisure activities and hobbies for a fulfilling retirement."
    ],
    "Travel and Exploration": [
        "Share travel tips for retirees looking to explore new places."
    ]
}

# Display dynamic sections
for section, content_list in sections.items():
    st.sidebar.markdown(f'<div class="custom-sidebar">', unsafe_allow_html=True)
    st.sidebar.markdown(f'<div class="section-header">{section}</div>', unsafe_allow_html=True)
    for content in content_list:
        st.sidebar.markdown(f'<div class="bullet-point">{content}</div>', unsafe_allow_html=True)
    st.sidebar.markdown('</div>', unsafe_allow_html=True)



st.subheader(":mailbox: Get In Touch With Me!")


contact_form = """
<form action="https://formsubmit.co/meetvasa09@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your Feedback!"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style1.css")