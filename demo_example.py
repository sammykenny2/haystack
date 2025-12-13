"""
Haystack 簡單範例 - 基本 Pipeline 使用

這個範例展示如何創建一個簡單的 Haystack Pipeline
"""

from haystack import Document, Pipeline
from haystack.components.builders import PromptBuilder
from haystack.components.retrievers.in_memory import InMemoryBM25Retriever
from haystack.document_stores.in_memory import InMemoryDocumentStore

# 1. 創建文件儲存並添加一些文件
print("步驟 1: 創建文件儲存...")
document_store = InMemoryDocumentStore()
documents = [
    Document(content="巴黎是法國的首都，也是歐洲最美麗的城市之一。"),
    Document(content="東京是日本的首都，以其現代化和傳統文化的融合而聞名。"),
    Document(content="倫敦是英國的首都，擁有豐富的歷史和文化遺產。"),
]
document_store.write_documents(documents)
print(f"已添加 {len(documents)} 個文件\n")

# 2. 創建 Pipeline
print("步驟 2: 創建檢索 Pipeline...")
pipeline = Pipeline()

# 3. 添加組件
retriever = InMemoryBM25Retriever(document_store=document_store)
pipeline.add_component("retriever", retriever)

# 4. 運行 Pipeline
print("步驟 3: 執行查詢...")
question = "法國的首都是哪裡？"
print(f"問題: {question}")

results = pipeline.run({"retriever": {"query": question, "top_k": 2}})

# 5. 顯示結果
print("\n查詢結果:")
for idx, doc in enumerate(results["retriever"]["documents"], 1):
    print(f"{idx}. {doc.content} (分數: {doc.score:.4f})")

print("\n✅ Pipeline 執行成功！")
print("\n" + "=" * 60)
print("這只是一個簡單範例。Haystack 可以做更多事情：")
print("- 連接 LLM（如 OpenAI GPT）進行問答")
print("- 建立 RAG（檢索增強生成）系統")
print("- 使用向量搜索和嵌入模型")
print("- 建立複雜的 AI Agent")
print("\n更多範例請參考: https://github.com/deepset-ai/haystack-cookbook/")
print("=" * 60)
