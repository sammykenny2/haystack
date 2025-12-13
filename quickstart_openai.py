# SPDX-FileCopyrightText: 2022-present deepset GmbH <info@deepset.ai>
#
# SPDX-License-Identifier: Apache-2.0

"""
Haystack 快速入門範例 - 建立一個簡單的 RAG 應用程式

這個範例展示如何使用 Haystack 建立一個基本的檢索增強生成 (RAG) 系統
"""

from haystack import Document, Pipeline
from haystack.components.builders import ChatPromptBuilder
from haystack.components.generators.chat import OpenAIChatGenerator
from haystack.components.retrievers import InMemoryBM25Retriever
from haystack.dataclasses import ChatMessage
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.utils import Secret


def main():
    """主程式:建立並運行 RAG Pipeline"""

    # ====== 步驟 1: 建立文件儲存並寫入資料 ======
    print("📚 步驟 1: 建立文件儲存...")
    document_store = InMemoryDocumentStore()
    document_store.write_documents(
        [
            Document(content="My name is Jean and I live in Paris."),
            Document(content="My name is Mark and I live in Berlin."),
            Document(content="My name is Giorgio and I live in Rome."),
        ]
    )
    print(f"   ✓ 已寫入 {document_store.count_documents()} 個文件\n")

    # ====== 步驟 2: 定義提示模板 ======
    print("💬 步驟 2: 定義提示模板...")
    prompt_template = [
        ChatMessage.from_system(
            """
            Given these documents, answer the question.
            Documents:
            {% for doc in documents %}
                {{ doc.content }}
            {% endfor %}
            Question:
            """
        ),
        ChatMessage.from_user("{{question}}"),
        ChatMessage.from_system("Answer:"),
    ]
    print("   ✓ 提示模板已建立\n")

    # ====== 步驟 3: 建立組件 ======
    print("🔧 步驟 3: 建立 Pipeline 組件...")
    retriever = InMemoryBM25Retriever(document_store=document_store)
    prompt_builder = ChatPromptBuilder(template=prompt_template, required_variables=["documents", "question"])

    # 注意:需要設定 OPENAI_API_KEY 環境變數
    # 可以改用其他生成器,例如 Hugging Face 模型
    llm = OpenAIChatGenerator(api_key=Secret.from_env_var("OPENAI_API_KEY"), model="gpt-4o-mini")
    print("   ✓ 已建立 Retriever")
    print("   ✓ 已建立 PromptBuilder")
    print("   ✓ 已建立 LLM (OpenAI)\n")

    # ====== 步驟 4: 組裝 Pipeline ======
    print("🔗 步驟 4: 組裝 Pipeline...")
    rag_pipeline = Pipeline()
    rag_pipeline.add_component("retriever", retriever)
    rag_pipeline.add_component("prompt_builder", prompt_builder)
    rag_pipeline.add_component("llm", llm)
    print("   ✓ 已添加所有組件\n")

    # ====== 步驟 5: 連接組件 ======
    print("🔌 步驟 5: 連接組件...")
    rag_pipeline.connect("retriever", "prompt_builder.documents")
    rag_pipeline.connect("prompt_builder", "llm")
    print("   ✓ 組件連接完成\n")

    # ====== 步驟 6: 運行 Pipeline ======
    print("🚀 步驟 6: 運行 Pipeline...")
    question = "Who lives in Paris?"
    print(f"   問題: {question}\n")

    results = rag_pipeline.run({"retriever": {"query": question}, "prompt_builder": {"question": question}})

    # ====== 步驟 7: 顯示結果 ======
    print("✨ 結果:")
    print(f"   回答: {results['llm']['replies'][0].content}\n")

    # 顯示完整的 Pipeline 結構
    print("📊 Pipeline 結構:")
    rag_pipeline.show()


if __name__ == "__main__":
    print("=" * 60)
    print("  Haystack RAG Pipeline 快速入門範例")
    print("=" * 60)
    print()

    try:
        main()
        print("\n" + "=" * 60)
        print("  ✓ 執行成功!")
        print("=" * 60)
    except Exception as e:
        print(f"\n❌ 錯誤: {e}")
        print("\n提示:")
        print("1. 確保已安裝 haystack-ai: pip install haystack-ai")
        print("2. 設定 OpenAI API Key: $env:OPENAI_API_KEY='your-key'")
        print("3. 或修改程式碼使用其他 LLM 供應商")
