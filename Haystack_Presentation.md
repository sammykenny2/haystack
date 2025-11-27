---
marp: true
theme: default
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
---

<!-- _class: lead -->

# 🌾 Haystack

## 端到端 LLM 應用框架

*建立強大的 AI 應用程式*

deepset.ai 開源專案

---

# 📋 目錄

1. 專案概述
2. 核心功能
3. 架構設計
4. 組件系統
5. Pipeline 編排
6. 實戰範例
7. 快速開始
8. 技術棧與生態

---

<!-- _class: lead -->

# 1️⃣ 專案概述

---

# 什麼是 Haystack？

**Haystack** 是一個端到端的 LLM 框架，讓你能夠建立：

- 🤖 **檢索增強生成 (RAG)** 應用
- 💬 **問答系統**
- 🔍 **語義搜索引擎**
- 📚 **文件處理管道**
- 🧠 **智能決策系統**

**開源授權**: Apache 2.0
**語言**: Python 3.9+
**GitHub**: deepset-ai/haystack

---

# 為什麼選擇 Haystack？

| 特性 | 說明 |
|------|------|
| 🔧 **技術無關** | 支援 OpenAI、Hugging Face、Cohere 等多種供應商 |
| 🎯 **明確透明** | 清晰的組件溝通機制 |
| 🔄 **靈活可擴展** | 輕鬆建立自訂組件 |
| 📦 **完整工具鏈** | 從資料處理到模型推理一應俱全 |
| 🚀 **生產就緒** | 內建測試、評估、監控機制 |

---

<!-- _class: lead -->

# 2️⃣ 核心功能

---

# 主要應用場景

### 🔍 檢索增強生成 (RAG)
結合向量資料庫與 LLM，提供精準的上下文答案

### 💬 問答系統
在大量文件中快速找到精確答案

### 🌐 語義搜索
根據意義而非關鍵字檢索文件

### 🔗 複雜決策系統
處理多步驟推理和複雜查詢

---

# 支援的功能模組

```
📁 核心功能
├── 🔄 文件轉換 (PDF, DOCX, HTML, Excel...)
├── ✂️  文本處理 (分割、清理、分類)
├── 🎯 向量嵌入 (多種嵌入模型)
├── 💾 文件儲存 (向量資料庫整合)
├── 🔍 檢索系統 (BM25, Dense, Hybrid)
├── 🤖 LLM 整合 (OpenAI, HF, Cohere...)
├── 📊 評估工具 (準確度、相關性評估)
└── 🔎 追蹤監控 (OpenTelemetry, DDTrace)
```

---

<!-- _class: lead -->

# 3️⃣ 架構設計

---

# 核心架構模式

## Pipeline + Component

```
┌─────────────────────────────────────┐
│         Pipeline (編排引擎)          │
├─────────────────────────────────────┤
│  ┌──────────┐    ┌──────────┐      │
│  │Component │───▶│Component │      │
│  │   A      │    │   B      │      │
│  └──────────┘    └──────────┘      │
│       │               │             │
│       ▼               ▼             │
│  ┌──────────┐    ┌──────────┐      │
│  │Component │───▶│Component │      │
│  │   C      │    │   D      │      │
│  └──────────┘    └──────────┘      │
└─────────────────────────────────────┘
```

**可插拔、可組合、可重用**

---

# Pipeline 工作流程

### 四個關鍵步驟

1. **創建 Pipeline**
   ```python
   pipeline = Pipeline()
   ```

2. **添加組件**
   ```python
   pipeline.add_component("retriever", retriever)
   ```

3. **連接組件**
   ```python
   pipeline.connect("retriever", "generator")
   ```

4. **執行 Pipeline**
   ```python
   result = pipeline.run({"query": "..."})
   ```

---

# 專案結構

```
haystack/
├── core/              # 核心功能
│   ├── pipeline/      # Pipeline 引擎
│   ├── component/     # 組件基礎類別
│   └── serialization/ # 序列化工具
├── components/        # 所有可用組件 (20+ 類別)
├── dataclasses/       # 資料結構
├── document_stores/   # 文件儲存
├── evaluation/        # 評估工具
├── tracing/          # 追蹤監控
└── utils/            # 工具函數
```

---

<!-- _class: lead -->

# 4️⃣ 組件系統

---

# 組件分類總覽

### 20+ 種組件類別

| 類別 | 用途 | 範例 |
|------|------|------|
| **Converters** | 文件轉換 | PDF→Text, DOCX→Text |
| **Embedders** | 向量嵌入 | SentenceTransformers |
| **Retrievers** | 文件檢索 | BM25, Vector Search |
| **Generators** | 文本生成 | OpenAI, Hugging Face |
| **Builders** | 提示建構 | PromptBuilder |
| **Routers** | 條件路由 | 根據條件分支 |

---

# 組件詳細分類 (1/2)

```
components/
├── 🎬 agents/          # AI 代理
├── 🎵 audio/           # 音訊處理 (Whisper 轉錄)
├── 🏗️  builders/        # 提示詞建構器
├── 💾 caching/         # 快取機制
├── 🏷️  classifiers/     # 分類器 (語言、文件類型)
├── 🔗 connectors/      # 外部服務連接器
├── 📄 converters/      # 文件轉換器
├── 🎯 embedders/       # 嵌入模型
├── 📊 evaluators/      # 評估工具
└── 🔍 extractors/      # 內容提取器
```

---

# 組件詳細分類 (2/2)

```
components/ (續)
├── 🌐 fetchers/        # 內容抓取器
├── 🤖 generators/      # LLM 生成器
├── 🔀 joiners/         # 結果合併器
├── ✂️  preprocessors/   # 預處理器
├── 📈 rankers/         # 排序器
├── 📖 readers/         # 閱讀理解模型
├── 🔎 retrievers/      # 檢索器
├── 🚦 routers/         # 路由器
├── 🎲 samplers/        # 採樣器
└── ✍️  writers/         # 文件寫入器
```

---

# 組件範例：Converters

### 支援多種文件格式

```python
# PDF 轉換
from haystack.components.converters import PyPDFToDocument
pdf_converter = PyPDFToDocument()

# Word 文件轉換
from haystack.components.converters import DocxToDocument
docx_converter = DocxToDocument()

# HTML 轉換
from haystack.components.converters import HTMLToDocument
html_converter = HTMLToDocument()

# Excel 轉換
from haystack.components.converters import XLSXToDocument
xlsx_converter = XLSXToDocument()
```

---

# 組件範例：Embedders

### 多種嵌入模型選擇

```python
# Sentence Transformers
from haystack.components.embedders import SentenceTransformersTextEmbedder
embedder = SentenceTransformersTextEmbedder(
    model="sentence-transformers/all-MiniLM-L6-v2"
)

# OpenAI Embeddings
from haystack.components.embedders import OpenAITextEmbedder
embedder = OpenAITextEmbedder(model="text-embedding-3-small")

# Hugging Face
from haystack.components.embedders import HuggingFaceTextEmbedder
embedder = HuggingFaceTextEmbedder()
```

---

# 組件範例：Generators

### 支援多種 LLM 供應商

```python
# OpenAI
from haystack.components.generators.chat import OpenAIChatGenerator
llm = OpenAIChatGenerator(model="gpt-4o-mini")

# Hugging Face (本地)
from haystack.components.generators import HuggingFaceLocalGenerator
llm = HuggingFaceLocalGenerator(model="google/flan-t5-base")

# Cohere
from haystack.components.generators import CohereGenerator
llm = CohereGenerator(model="command")

# Anthropic (整合套件)
from haystack_integrations.components.generators.anthropic import AnthropicChatGenerator
llm = AnthropicChatGenerator(model="claude-3-sonnet")
```

---

<!-- _class: lead -->

# 5️⃣ Pipeline 編排

---

# Pipeline 類型

### 1. 同步 Pipeline
```python
from haystack import Pipeline
pipeline = Pipeline()
result = pipeline.run(data)
```

### 2. 非同步 Pipeline
```python
from haystack import AsyncPipeline
pipeline = AsyncPipeline()
result = await pipeline.run_async(data)
```

### 3. 預定義模板
```python
from haystack import Pipeline, PredefinedPipeline
pipeline = Pipeline.from_template(PredefinedPipeline.RAG)
```

---

# Pipeline 連接機制

### 明確的輸入輸出連接

```python
# 基本連接
pipeline.connect("component1", "component2")

# 指定輸出/輸入
pipeline.connect("embedder.embedding", "retriever.query_embedding")

# 多輸出連接
pipeline.connect("router.approved", "generator")
pipeline.connect("router.rejected", "fallback_handler")
```

**特點**: 類型安全、自動驗證、清晰可見

---

# Pipeline 視覺化

### 內建視覺化工具

```python
# 在終端顯示
pipeline.show()

# 生成圖形
pipeline.draw("pipeline.png")
```

**輸出範例**:
```
retriever -> prompt_builder.documents
prompt_builder -> llm.messages
```

可以清楚看到資料流向！

---

# SuperComponent

### 將 Pipeline 封裝為組件

```python
from haystack import SuperComponent, super_component

@super_component
class MyCustomPipeline(SuperComponent):
    def __init__(self):
        self.pipeline = Pipeline()
        # ... 建構內部 pipeline
    
# 使用
custom_component = MyCustomPipeline()
outer_pipeline.add_component("custom", custom_component)
```

**用途**: 建立可重用的複雜組件

---

<!-- _class: lead -->

# 6️⃣ 實戰範例

---

# 範例 1: 簡單檢索系統

```python
from haystack import Pipeline, Document
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.components.retrievers import InMemoryBM25Retriever

# 建立文件儲存
document_store = InMemoryDocumentStore()
document_store.write_documents([
    Document(content="Python is a programming language."),
    Document(content="Java is used for enterprise apps."),
])

# 建立 Pipeline
pipeline = Pipeline()
retriever = InMemoryBM25Retriever(document_store=document_store)
pipeline.add_component("retriever", retriever)

# 執行查詢
result = pipeline.run({"retriever": {"query": "What is Python?"}})
print(result["retriever"]["documents"])
```

---

# 範例 2: RAG Pipeline

```python
from haystack import Pipeline, Document
from haystack.components.builders import ChatPromptBuilder
from haystack.components.generators.chat import OpenAIChatGenerator
from haystack.components.retrievers import InMemoryBM25Retriever
from haystack.document_stores.in_memory import InMemoryDocumentStore

# 準備組件
document_store = InMemoryDocumentStore()
retriever = InMemoryBM25Retriever(document_store=document_store)
prompt_builder = ChatPromptBuilder(template=template)
llm = OpenAIChatGenerator(model="gpt-4o-mini")

# 組裝 Pipeline
pipeline = Pipeline()
pipeline.add_component("retriever", retriever)
pipeline.add_component("prompt_builder", prompt_builder)
pipeline.add_component("llm", llm)
```

---

# 範例 2: RAG Pipeline (續)

```python
# 連接組件
pipeline.connect("retriever", "prompt_builder.documents")
pipeline.connect("prompt_builder", "llm")

# 執行查詢
question = "What is machine learning?"
result = pipeline.run({
    "retriever": {"query": question},
    "prompt_builder": {"question": question}
})

# 獲取答案
answer = result["llm"]["replies"][0].content
print(answer)
```

**完整的 RAG 系統，不到 20 行程式碼！**

---

# 範例 3: 文件處理 Pipeline

```python
from haystack import Pipeline
from haystack.components.converters import PyPDFToDocument
from haystack.components.preprocessors import DocumentCleaner, DocumentSplitter
from haystack.components.writers import DocumentWriter

# 建立組件
converter = PyPDFToDocument()
cleaner = DocumentCleaner()
splitter = DocumentSplitter(split_by="sentence", split_length=5)
writer = DocumentWriter(document_store=document_store)

# 組裝 Pipeline
pipeline = Pipeline()
pipeline.add_component("converter", converter)
pipeline.add_component("cleaner", cleaner)
pipeline.add_component("splitter", splitter)
pipeline.add_component("writer", writer)
```

---

# 範例 3: 文件處理 Pipeline (續)

```python
# 連接組件
pipeline.connect("converter", "cleaner")
pipeline.connect("cleaner", "splitter")
pipeline.connect("splitter", "writer")

# 執行處理
pipeline.run({
    "converter": {"sources": ["document.pdf"]}
})
```

**自動化文件處理流程**:
PDF → 清理 → 分割 → 儲存

---

# 範例 4: 條件路由 Pipeline

```python
from haystack import Pipeline
from haystack.components.routers import ConditionalRouter

# 建立路由器
routes = [
    {"condition": "{{query|length > 50}}", "output": "long_handler"},
    {"condition": "{{query|length <= 50}}", "output": "short_handler"}
]
router = ConditionalRouter(routes=routes)

# 建立 Pipeline
pipeline = Pipeline()
pipeline.add_component("router", router)
pipeline.add_component("long_handler", long_query_processor)
pipeline.add_component("short_handler", short_query_processor)

pipeline.connect("router.long_handler", "long_handler")
pipeline.connect("router.short_handler", "short_handler")
```

---

<!-- _class: lead -->

# 7️⃣ 快速開始

---

# 安裝

### 基本安裝

```bash
pip install haystack-ai
```

### 從原始碼安裝

```bash
git clone https://github.com/deepset-ai/haystack.git
cd haystack
pip install -e .
```

### 安裝額外依賴

```bash
# Transformers 支援
pip install transformers[torch,sentencepiece]

# Sentence Transformers
pip install sentence-transformers

# 文件轉換
pip install pypdf python-docx python-pptx
```

---

# 第一個應用程式 (1/2)

```python
from haystack import Pipeline, Document
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.components.retrievers import InMemoryBM25Retriever
from haystack.components.builders import ChatPromptBuilder
from haystack.components.generators.chat import OpenAIChatGenerator
from haystack.dataclasses import ChatMessage

# 1. 建立文件儲存並添加資料
document_store = InMemoryDocumentStore()
document_store.write_documents([
    Document(content="My name is Jean and I live in Paris."),
    Document(content="My name is Mark and I live in Berlin."),
    Document(content="My name is Giorgio and I live in Rome.")
])
```

---

# 第一個應用程式 (2/2)

```python
# 2. 建立組件
retriever = InMemoryBM25Retriever(document_store=document_store)
prompt_builder = ChatPromptBuilder(template=prompt_template)
llm = OpenAIChatGenerator(model="gpt-4o-mini")

# 3. 組裝 Pipeline
pipeline = Pipeline()
pipeline.add_component("retriever", retriever)
pipeline.add_component("prompt_builder", prompt_builder)
pipeline.add_component("llm", llm)
pipeline.connect("retriever", "prompt_builder.documents")
pipeline.connect("prompt_builder", "llm")

# 4. 執行
result = pipeline.run({
    "retriever": {"query": "Who lives in Paris?"},
    "prompt_builder": {"question": "Who lives in Paris?"}
})
```

---

# 環境變數設定

### OpenAI API Key

```powershell
# Windows PowerShell
$env:OPENAI_API_KEY = "your-api-key-here"

# Linux/Mac
export OPENAI_API_KEY="your-api-key-here"
```

### Python 中使用

```python
from haystack.utils import Secret

# 從環境變數讀取
api_key = Secret.from_env_var("OPENAI_API_KEY")

# 直接傳入
llm = OpenAIChatGenerator(api_key=api_key)
```

---

<!-- _class: lead -->

# 8️⃣ 技術棧與生態

---

# 核心技術棧

| 技術 | 用途 |
|------|------|
| **Python 3.9+** | 主要程式語言 |
| **Pydantic** | 資料驗證 |
| **NetworkX** | 圖形處理 (Pipeline DAG) |
| **Jinja2** | 模板引擎 |
| **OpenTelemetry** | 分散式追蹤 |
| **Tenacity** | 重試機制 |
| **NumPy** | 數值計算 |

---

# 支援的向量資料庫

### 官方整合

- ✅ **In-Memory** (內建)
- ✅ **Elasticsearch**
- ✅ **Weaviate**
- ✅ **Pinecone**
- ✅ **Qdrant**
- ✅ **Milvus**
- ✅ **Chroma**
- ✅ **OpenSearch**
- ✅ **PostgreSQL (pgvector)**

更多整合請見: [haystack-core-integrations](https://github.com/deepset-ai/haystack-core-integrations)

---

# LLM 供應商支援

### 主流供應商全支援

| 供應商 | 模型範例 |
|--------|----------|
| **OpenAI** | GPT-4, GPT-3.5, o1 |
| **Anthropic** | Claude 3 系列 |
| **Google** | Gemini, PaLM |
| **Cohere** | Command, Generate |
| **Hugging Face** | 開源模型 |
| **Azure OpenAI** | Azure 託管模型 |
| **AWS Bedrock** | Claude, Llama 等 |
| **Ollama** | 本地部署 |

---

# 開發工具

### 內建工具

```bash
# 格式化程式碼
hatch run fmt

# 檢查程式碼風格
hatch run fmt-check

# 運行測試
hatch run test:unit
hatch run test:integration

# 類型檢查
hatch run test:types

# 程式碼檢查
hatch run test:lint
```

---

# 生態系統

### 相關專案

| 專案 | 用途 |
|------|------|
| **Hayhooks** | REST API 部署工具 |
| **deepset Studio** | 視覺化開發環境 |
| **haystack-cookbook** | 實戰範例集合 |
| **haystack-core-integrations** | 官方整合套件 |
| **Haystack Enterprise** | 企業級支援 |

---

# 測試覆蓋

### 完整的測試套件

```
test/               # 單元測試
├── components/     # 組件測試
├── core/          # 核心功能測試
├── dataclasses/   # 資料類別測試
└── ...

e2e/               # 端到端測試
├── pipelines/     # Pipeline 整合測試
└── samples/       # 範例測試
```

**測試覆蓋率**: 高覆蓋率，確保品質

---

# 文件資源

### 📚 豐富的學習資源

- **官方文件**: https://docs.haystack.deepset.ai
- **快速入門**: https://haystack.deepset.ai/overview/quick-start
- **教學課程**: https://haystack.deepset.ai/tutorials
- **Cookbook**: https://github.com/deepset-ai/haystack-cookbook
- **API 參考**: https://docs.haystack.deepset.ai/reference
- **部落格**: https://haystack.deepset.ai/blog

---

# 社群支援

### 🤝 活躍的開發者社群

- **GitHub**: 8k+ Stars, 1.5k+ Forks
- **Discord**: 活躍的技術討論社群
- **Stack Overflow**: `haystack` 標籤
- **Twitter**: @haystack_ai
- **GitHub Discussions**: 問題討論

**貢獻歡迎**: Issues, PRs, Integrations

---

# 企業級方案

### Haystack Enterprise

- ✅ **專家支援** - deepset 團隊直接支援
- ✅ **企業模板** - 加速開發
- ✅ **部署指南** - 雲端與本地部署
- ✅ **安全強化** - 企業級安全性
- ✅ **SLA 保證** - 服務等級協議

### deepset Studio

- 🎨 視覺化 Pipeline 建構
- 🚀 一鍵部署
- 🧪 整合測試環境

---

<!-- _class: lead -->

# 總結

---

# Haystack 的優勢

### ✨ 為什麼選擇 Haystack？

1. **模組化設計** - 組件自由組合
2. **技術靈活** - 支援多種 LLM 和向量資料庫
3. **生產就緒** - 完整的測試和監控
4. **活躍社群** - 持續更新和支援
5. **開源免費** - Apache 2.0 授權
6. **企業支援** - 提供商業方案

**適合**: RAG、問答、搜索、文件處理等 AI 應用

---

# 適用場景

### 🎯 最適合的使用情境

- ✅ 企業知識庫問答系統
- ✅ 智能客服機器人
- ✅ 文件搜索和摘要
- ✅ 多語言內容處理
- ✅ 複雜的多步驟推理
- ✅ 混合檢索系統
- ✅ 大規模文件處理

---

# 快速回顧

### 核心概念

```
Pipeline = 編排引擎
Component = 可插拔單元
Document Store = 資料儲存
Retriever = 檢索器
Generator = LLM 生成器
```

### 基本流程

```
建立組件 → 添加到 Pipeline → 連接組件 → 執行
```

---

# 下一步行動

### 🚀 開始你的 Haystack 之旅

1. **安裝**: `pip install haystack-ai`
2. **運行範例**: 查看 `simple_example.py`
3. **閱讀文件**: https://docs.haystack.deepset.ai
4. **探索 Cookbook**: 實戰範例
5. **加入社群**: Discord、GitHub
6. **建立專案**: 開始你的第一個 RAG 應用

---

# 實用資源連結

### 📖 重要連結

| 資源 | 網址 |
|------|------|
| GitHub | github.com/deepset-ai/haystack |
| 文件 | docs.haystack.deepset.ai |
| Cookbook | github.com/deepset-ai/haystack-cookbook |
| Discord | discord.gg/VBpFzsgRVF |
| Twitter | twitter.com/haystack_ai |
| 部落格 | haystack.deepset.ai/blog |

---

<!-- _class: lead -->

# 謝謝！

## 🌾 Haystack

**建立你的下一個 AI 應用程式**

---

**Questions?**

📧 聯繫: info@deepset.ai
🐦 Twitter: @haystack_ai
💬 Discord: discord.gg/VBpFzsgRVF

---

*本投影片由 Haystack 社群貢獻者製作*
*使用 Marp 生成*
