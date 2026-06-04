# YouTube RAG Chatbot

This project is a simple Retrieval-Augmented Generation (RAG) based Chatbot for YouTube videos, built using Langchain. It allows you to ask questions about the content of a YouTube video, and it retrieves the relevant information from the video's transcript to provide an answer.

## 🚀 Features

- **YouTube Transcript Extraction**: Automatically fetches transcripts from YouTube videos using `youtube-transcript-api`.
- **RAG Architecture**: Uses Langchain to chunk the transcript, embed the text, and retrieve relevant context based on user queries.
- **Vector Store**: Utilizes FAISS (`faiss-cpu`) for efficient similarity search.
- **LLM Integration**: Uses OpenAI models via `langchain-openai` for generating natural language answers.
- **Embeddings**: Uses `sentence-transformers` for generating embeddings.

## 🛠️ Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.8 or higher.
- An OpenAI API Key (for the LLM).

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd Youtube_Chatbot
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   Create a `.env` file in the root directory and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## 💻 Usage

The main implementation and interactive demonstration are provided in the Jupyter Notebook `rag-using-langchain.ipynb`.

1. Launch Jupyter Notebook or Jupyter Lab:
   ```bash
   jupyter notebook
   ```
2. Open `rag-using-langchain.ipynb`.
3. Follow the steps in the notebook to extract a transcript, build the vector store, and start chatting with the YouTube video content!

## 🐛 Note on FAISS

If you encounter an error related to `vector_store.get_by_ids()` when running older versions of the notebook, you can run the provided `fix_faiss_error.py` script. This script automatically updates the notebook to use the correct `vector_store.docstore.search()` method instead, as FAISS does not support `get_by_ids` directly.

```bash
python fix_faiss_error.py
```

## 📚 Libraries Used

- [Langchain](https://github.com/langchain-ai/langchain)
- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api)
- [FAISS](https://github.com/facebookresearch/faiss)
- [OpenAI](https://platform.openai.com/docs/)
- [Sentence Transformers](https://www.sbert.net/)
