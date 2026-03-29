import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Search Chatbot", page_icon="🔎", layout="wide")

## Initialize tools
@st.cache_resource
def get_search_tools():
    """Initialize search tools"""
    search = DuckDuckGoSearchRun()
    wiki = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=500)
    arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=500)
    return search, wiki, arxiv_wrapper

search_tool, wiki_tool, arxiv_tool = get_search_tools()

def search_web(query):
    """Search the web"""
    try:
        result = search_tool.run(query)
        return f"🌐 Web Search Results:\n{result}"
    except Exception as e:
        return f"Web search failed: {str(e)}"

def search_wikipedia(query):
    """Search Wikipedia"""
    try:
        result = wiki_tool.run(query)
        return f"📚 Wikipedia:\n{result}"
    except Exception as e:
        return f"Wikipedia search failed: {str(e)}"

def search_arxiv(query):
    """Search Arxiv"""
    try:
        from langchain_community.tools import ArxivQueryRun
        arxiv_search = ArxivQueryRun(api_wrapper=arxiv_tool)
        result = arxiv_search.run(query)
        return f"🎓 Arxiv Papers:\n{result}"
    except Exception as e:
        return f"Arxiv search failed: {str(e)}"

def get_answer(question, search_results, model, api_key):
    """Get AI answer based on search results"""
    llm = ChatGroq(groq_api_key=api_key, model_name=model, temperature=0.7)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AI assistant. Answer the question based on the search results provided. Be concise and accurate."),
        ("human", "Question: {question}\n\nSearch Results:\n{results}\n\nProvide a clear, comprehensive answer:")
    ])
    
    chain = prompt | llm
    response = chain.invoke({"question": question, "results": search_results})
    return response.content


st.title("🔎 LangChain - Chat with Search")
st.markdown("""
Ask me anything! I can search the web, Wikipedia, and academic papers to answer your questions.
""")

## Sidebar
st.sidebar.title("⚙️ Settings")
api_key = st.sidebar.text_input("Enter your Groq API Key:", type="password", help="Get your free API key from https://console.groq.com")

st.sidebar.subheader("Model Selection")
model_choice = st.sidebar.selectbox(
    "Choose Model",
    ["llama-3.1-8b-instant", "llama-3.3-70b-versatile", "mixtral-8x7b-32768", "gemma2-9b-it"],
    index=0,
    help="llama-3.1-8b-instant is fastest and most reliable"
)

st.sidebar.subheader("Search Tools")
use_web = st.sidebar.checkbox("🌐 Enable Web Search", value=True)
use_wiki = st.sidebar.checkbox("📚 Enable Wikipedia", value=True)
use_arxiv = st.sidebar.checkbox("🎓 Enable Arxiv", value=False, help="May have rate limits")

st.sidebar.markdown("---")
st.sidebar.markdown("### 📖 How to use:")
st.sidebar.markdown("1. Enter your Groq API key")
st.sidebar.markdown("2. Select search tools")
st.sidebar.markdown("3. Ask any question!")

## Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm a search assistant. Ask me anything and I'll search the web to find answers for you! 🔍"}
    ]

## Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

## Chat input
if prompt := st.chat_input("Ask me anything..."):
    # Check API key
    if not api_key:
        st.error("⚠️ Please enter your Groq API key in the sidebar!")
        st.stop()
    
    # Check if at least one tool is enabled
    if not (use_web or use_wiki or use_arxiv):
        st.error("⚠️ Please enable at least one search tool in the sidebar!")
        st.stop()
    
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("🔍 Searching..."):
            search_results = []
            
            # Search web
            if use_web:
                with st.status("🌐 Searching the web...", expanded=True):
                    web_result = search_web(prompt)
                    search_results.append(web_result)
                    st.markdown(web_result)
            
            # Search Wikipedia
            if use_wiki:
                with st.status("📚 Searching Wikipedia...", expanded=True):
                    wiki_result = search_wikipedia(prompt)
                    search_results.append(wiki_result)
                    st.markdown(wiki_result)
            
            # Search Arxiv
            if use_arxiv:
                with st.status("🎓 Searching Arxiv...", expanded=True):
                    try:
                        arxiv_result = search_arxiv(prompt)
                        search_results.append(arxiv_result)
                        st.markdown(arxiv_result)
                    except Exception as e:
                        if "429" in str(e):
                            st.warning("⚠️ Arxiv rate limit reached. Skipping...")
                        else:
                            st.warning(f"⚠️ Arxiv search failed: {str(e)}")
            
            # Combine results
            combined_results = "\n\n".join(search_results)
            
            # Get AI answer
            with st.spinner("🤖 Generating answer..."):
                try:
                    answer = get_answer(prompt, combined_results, model_choice, api_key)
                    st.markdown("---")
                    st.markdown("### 💡 AI Answer:")
                    st.markdown(answer)
                    
                    # Save to history
                    st.session_state.messages.append({
                        "role": "assistant", 
                        "content": f"{combined_results}\n\n---\n\n### 💡 AI Answer:\n{answer}"
                    })
                    
                except Exception as e:
                    error_msg = f"⚠️ Error generating answer: {str(e)}"
                    st.error(error_msg)
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})

## Footer
st.sidebar.markdown("---")
st.sidebar.markdown("Made with ❤️ using LangChain & Groq")