# 🚀 Haystack 運行指南

這份指南將幫助你快速上手 Haystack 專案。

## 📋 前置需求

- Python 3.9 或更高版本
- pip 套件管理器

## 🔧 安裝步驟

### 1. 安裝 Haystack

```powershell
# 基本安裝
pip install haystack-ai

# 或從本專案安裝 (開發版本)
pip install -e .
```

### 2. 安裝額外依賴 (根據需求)

```powershell
# 如果要使用 Hugging Face 模型
pip install transformers[torch,sentencepiece]

# 如果要使用 Sentence Transformers
pip install sentence-transformers

# 如果要使用文件轉換功能
pip install pypdf python-docx python-pptx

# 如果要使用評估功能
pip install pandas
```

## ⚡ 快速開始

### 方案 1: 運行簡單範例 (無需 API Key)

這個範例只使用本地組件,不需要任何外部 API:

```powershell
python simple_example.py
```

**功能說明:**
- 在記憶體中建立文件儲存
- 使用 BM25 演算法進行檢索
- 展示如何建立和運行 Pipeline

### 方案 2: 運行完整 RAG 範例 (需要 OpenAI API Key)

```powershell
# 設定 OpenAI API Key
$env:OPENAI_API_KEY = "your-api-key-here"

# 運行範例
python quickstart_example.py
```

**功能說明:**
- 完整的 RAG (檢索增強生成) 系統
- 使用 OpenAI GPT 模型生成答案
- 展示端到端的工作流程

### 方案 3: 使用預定義模板

```python
from haystack import Pipeline, PredefinedPipeline

# 使用 RAG 模板快速建立 Pipeline
pipeline = Pipeline.from_template(PredefinedPipeline.RAG)

# 運行
result = pipeline.run({
    "text_embedder": {"text": "What is AI?"}
})
```

## 📚 範例程式碼說明

### 基本 Pipeline 結構

```python
from haystack import Pipeline, Document
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.components.retrievers import InMemoryBM25Retriever

# 1. 建立文件儲存
document_store = InMemoryDocumentStore()
document_store.write_documents([
    Document(content="Your content here")
])

# 2. 建立組件
retriever = InMemoryBM25Retriever(document_store=document_store)

# 3. 建立 Pipeline
pipeline = Pipeline()
pipeline.add_component("retriever", retriever)

# 4. 運行
result = pipeline.run({"retriever": {"query": "your query"}})
```

### 典型 RAG Pipeline

```python
from haystack import Pipeline, Document
from haystack.components.generators.chat import OpenAIChatGenerator
from haystack.components.retrievers import InMemoryBM25Retriever
from haystack.components.builders import ChatPromptBuilder
from haystack.document_stores.in_memory import InMemoryDocumentStore

# 組件
document_store = InMemoryDocumentStore()
retriever = InMemoryBM25Retriever(document_store=document_store)
prompt_builder = ChatPromptBuilder(template=template)
llm = OpenAIChatGenerator(model="gpt-4o-mini")

# Pipeline
pipeline = Pipeline()
pipeline.add_component("retriever", retriever)
pipeline.add_component("prompt_builder", prompt_builder)
pipeline.add_component("llm", llm)

# 連接
pipeline.connect("retriever", "prompt_builder.documents")
pipeline.connect("prompt_builder", "llm")

# 運行
result = pipeline.run({
    "retriever": {"query": question},
    "prompt_builder": {"question": question}
})
```

## 🔍 可用的 LLM 供應商

### OpenAI
```python
from haystack.components.generators.chat import OpenAIChatGenerator
llm = OpenAIChatGenerator(model="gpt-4o-mini")
```

### Hugging Face
```python
from haystack.components.generators import HuggingFaceLocalGenerator
llm = HuggingFaceLocalGenerator(model="google/flan-t5-base")
```

### Anthropic Claude
```python
# 需要安裝整合套件
from haystack_integrations.components.generators.anthropic import AnthropicChatGenerator
llm = AnthropicChatGenerator(model="claude-3-sonnet-20240229")
```

### Cohere
```python
from haystack.components.generators import CohereGenerator
llm = CohereGenerator(model="command")
```

## 🧪 運行測試

```powershell
# 安裝測試依賴
pip install -e ".[test]"

# 運行單元測試
pytest test/ -m "not integration"

# 運行整合測試
pytest test/ -m "integration"

# 運行所有測試
pytest test/
```

## 📖 更多資源

- **官方文件**: https://docs.haystack.deepset.ai
- **快速入門指南**: https://haystack.deepset.ai/overview/quick-start
- **教學範例**: https://haystack.deepset.ai/tutorials
- **Cookbook**: https://github.com/deepset-ai/haystack-cookbook/
- **API 參考**: https://docs.haystack.deepset.ai/reference

## 💡 常見問題

### Q: 我沒有 OpenAI API Key,可以使用嗎?
A: 可以!你可以使用:
- Hugging Face 的免費本地模型
- 其他開源 LLM (如 Ollama)
- 只使用檢索功能,不使用生成功能

### Q: 如何使用自己的資料?
A: 將你的資料轉換為 `Document` 物件:
```python
from haystack import Document

documents = [
    Document(content="Your text content"),
    Document(content="More content", meta={"source": "file.pdf"})
]
document_store.write_documents(documents)
```

### Q: 如何處理 PDF 文件?
A: 使用文件轉換器:
```python
from haystack.components.converters import PyPDFToDocument

converter = PyPDFToDocument()
documents = converter.run(sources=["path/to/file.pdf"])
```

### Q: 支援中文嗎?
A: 支援!Haystack 支援多語言,包括中文。選擇支援中文的模型即可。

## 🎯 下一步

1. ✅ 運行 `simple_example.py` 瞭解基本概念
2. ✅ 嘗試 `quickstart_example.py` 體驗完整 RAG
3. ✅ 查看官方 Cookbook 學習更多範例
4. ✅ 根據你的需求自訂 Pipeline
5. ✅ 探索不同的組件和整合

## 🤝 需要幫助?

- GitHub Issues: https://github.com/deepset-ai/haystack/issues
- Discord 社群: https://discord.com/invite/VBpFzsgRVF
- Stack Overflow: 標籤 `haystack`

---

**祝你使用 Haystack 順利! 🚀**
