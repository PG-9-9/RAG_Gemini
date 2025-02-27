# 📌 RAG Chatbot with Gemini Pro & ChromaDB

This is a **Retrieval-Augmented Generation (RAG) chatbot** that integrates:
- **Google Gemini Pro** for text generation
- **ChromaDB** for document retrieval
- **LangChain** for AI-driven pipeline management
- **Streamlit** for the user interface

The chatbot **retrieves relevant information** from a PDF and generates **context-aware responses**.

---

## 📂 Project Structure
```
📁 project-directory/
│-- 📜 app.py                # Main Streamlit application
│-- 📜 requirements.txt       # Required dependencies
│-- 📜 .env                   # API keys (ignored in Git)
│-- 📜 my_paper.pdf           # Sample document for retrieval
│-- 📂 data/                  # Store additional PDF files (if needed)
```

---

## 🚀 Features
✅ **Retrieval-Augmented Generation (RAG):** Retrieves relevant document sections before answering.  
✅ **Google Gemini Pro API:** Generates accurate and contextual responses.  
✅ **ChromaDB for Vector Search:** Efficiently retrieves semantically similar text chunks.  
✅ **Streamlit UI:** Provides a simple and interactive chatbot interface.  
✅ **Scalable Document Search:** Can process large PDFs and find answers in seconds.  

---

## 🛠 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo/rag-chatbot-gemini.git
cd rag-chatbot-gemini
```

### 2️⃣ Install Dependencies
Ensure you have **Python 3.8+** installed. Then, install the required dependencies:
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up API Keys
- Create a `.env` file in the project root and add your **Google Gemini API key**:
```bash
GOOGLE_API_KEY="your-gemini-api-key"
```
- Ensure `.env` is **ignored in `.gitignore`** to prevent exposing sensitive information.

### 4️⃣ Run the Application
```bash
streamlit run app.py
```
This will launch the chatbot UI in your **default web browser**.

---

## 📜 How It Works

### 🔹 Step 1: Load the PDF
- Uses **`PyPDFLoader`** to extract text from `my_paper.pdf`.

### 🔹 Step 2: Text Chunking & Vectorization
- Splits text into **1000-character chunks** using `RecursiveCharacterTextSplitter`.
- Converts chunks into **vector embeddings** using **GoogleGenerativeAIEmbeddings**.
- Stores vectors in **ChromaDB** for retrieval.

### 🔹 Step 3: Query Processing
- User **enters a question** in the Streamlit chat input.
- The **retriever fetches** relevant document chunks.
- The retrieved context is **fed into the LLM**.

### 🔹 Step 4: Response Generation
- **Gemini Pro** generates a response using both **retrieved context** and the **user’s query**.
- The final **answer is displayed** in the Streamlit chat UI.

---

## 🖥️ Usage Example

1️⃣ Upload a PDF (or use `my_paper.pdf`).  
2️⃣ Ask a question in the **chatbox**.  
3️⃣ The AI **retrieves relevant text** and generates a **concise response**.

Example:
```
🔹 User: "What are CNNs used for?"
🔹 AI: "CNNs are deep learning models used for image recognition, medical imaging, and self-driving cars."
```

---

## ⚡ Key Technologies Used

| Component | Technology |
|-----------|------------|
| **UI Framework** | Streamlit |
| **LLM** | Google Gemini Pro (via LangChain) |
| **Vector Database** | ChromaDB |
| **Document Processing** | PyPDFLoader |
| **Prompt Engineering** | LangChain's `ChatPromptTemplate` |

---

## 🛠 Troubleshooting

🔹 **Error: Missing API Key**  
   - Ensure `.env` contains `GOOGLE_API_KEY`  
   - Restart the app after setting the key.  

🔹 **PDF Not Processing?**  
   - Check if `my_paper.pdf` exists in the root folder.  
   - Try another PDF file.  

🔹 **Slow Response Times?**  
   - Reduce `k=10` to `k=5` in the retriever for faster search.  

---

## 🔮 Future Enhancements

🚀 **Multi-document search:** Allow searching across multiple PDFs.  
🚀 **Memory Integration:** Store past conversations for follow-ups.  
🚀 **Better UI:** Add file upload & chatbot avatars.  

---

## 📜 License

This project is **MIT Licensed**. Feel free to use, modify, and contribute!

---

## 🙌 Contributing

Pull requests are welcome! Open an issue for **feature requests or bug reports**.
