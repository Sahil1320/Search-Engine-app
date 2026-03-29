# 🔎 LangChain Search Chatbot - Simple & Working Version

**Now with 100% working search functionality!**

An intelligent chatbot that searches the web, Wikipedia, and academic papers to answer your questions. Built with a simple, reliable architecture.

## ✨ What's New

- ✅ **Completely rewritten** - No more complex agent errors
- ✅ **Direct search integration** - Tools work reliably every time
- ✅ **Visual search progress** - See each search happening in real-time
- ✅ **Better error handling** - Clear feedback if something goes wrong
- ✅ **Faster responses** - Simpler architecture means quicker results

## Features

- 🌐 **Web Search** - Real-time web search via DuckDuckGo
- 📚 **Wikipedia Integration** - Access encyclopedia knowledge
- 🎓 **Academic Papers** - Search Arxiv for research (optional)
- 🤖 **Multiple AI Models** - Choose from Groq's fastest models
- 💬 **Interactive Chat** - Conversational interface with history
- 👀 **Transparent Process** - See each search as it happens

## Quick Start

### 1. Get Your Groq API Key (Free!)
- Visit [https://console.groq.com](https://console.groq.com)
- Sign up and create an API key

### 2. Start the App
```bash
cd "D:\Q&A Chatbot project\Search Engine Tools"
streamlit run app.py
```

### 3. Use the App
1. Enter your Groq API key in the sidebar
2. Select model: **llama-3.1-8b-instant** (recommended)
3. Enable: ✅ Web Search, ✅ Wikipedia
4. Ask any question!

## Example Questions

Try these to see it work:

**General Knowledge:**
- "What is machine learning?"
- "Explain artificial intelligence"
- "Who is Elon Musk?"

**Current Information:**
- "What's the latest in technology?"
- "Recent developments in AI"

**Definitions:**
- "What is Python programming?"
- "Explain blockchain technology"

## How It Works

**Simple 3-Step Process:**

1. **Search** - The app searches your selected sources (Web/Wikipedia/Arxiv)
2. **Display** - You see the raw search results
3. **Synthesize** - AI creates a comprehensive answer from the results

No complex agents, no tool calling errors - just straightforward, working search!

## Configuration

### Sidebar Controls

**API Key**
- Required: Your Groq API key
- Get it free from: https://console.groq.com

**Model Selection**
- `llama-3.1-8b-instant` ⭐ **Recommended** - Fast and reliable
- `llama-3.3-70b-versatile` - Slower but more detailed
- `mixtral-8x7b-32768` - Good for long conversations
- `gemma2-9b-it` - Alternative fast model

**Search Tools**
- 🌐 Web Search - Always recommended
- 📚 Wikipedia - Always recommended
- 🎓 Arxiv - Use only for academic questions (has rate limits)

## Requirements

```
streamlit
langchain
langchain-community
langchain-core
langchain-groq
python-dotenv
duckduckgo-search
ddgs
wikipedia
arxiv
```

## Troubleshooting

### App won't start?
```bash
# Make sure you're in the right directory
cd "D:\Q&A Chatbot project\Search Engine Tools"

# Activate virtual environment
cd ..
.\cleanenv\Scripts\activate
cd "Search Engine Tools"

# Run the app
streamlit run app.py
```

### No search results?
- Check your internet connection
- Make sure at least one search tool is enabled
- Try disabling Arxiv if you see rate limit errors

### API key not working?
- Copy the entire key without spaces
- Make sure it's active in Groq console
- Try generating a new key

## What's Different from Before?

**Old Version:**
- ❌ Used complex LangChain agents
- ❌ Tool calling often failed
- ❌ Unclear error messages
- ❌ Difficult to debug

**New Version:**
- ✅ Direct search calls - always work
- ✅ Simple, predictable flow
- ✅ Clear visual feedback
- ✅ Easy to understand and modify

## Technical Details

**Architecture:**
1. User asks a question
2. App directly calls search APIs (DuckDuckGo, Wikipedia, Arxiv)
3. Results are displayed immediately
4. AI model synthesizes an answer from all results

**No agents, no tool calling, no complexity - just reliable search!**

## Project Structure

```
Search Engine Tools/
├── app.py              # Main app (completely rewritten)
├── README.md           # This file
├── requirements.txt   # Dependencies

```

## Support

For issues or questions:
1. Check the QUICKSTART.md file
2. Verify your API key is correct
3. Make sure all dependencies are installed

## License

MIT License - Feel free to modify and use!

---

**Now actually working! 🎉 Ask any question and see it search in real-time!**

