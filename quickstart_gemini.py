"""
Haystack 快速入門 - 使用 Google Gemini

這個範例展示如何使用 Google Gemini API 建立 RAG 系統
"""

from haystack import Pipeline, Document
from haystack.components.generators import GoogleAIGeminiGenerator
from haystack.components.retrievers import InMemoryBM25Retriever
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.components.builders import PromptBuilder
from haystack.utils import Secret

def main():
    """使用 Google Gemini 建立 RAG Pipeline"""
    
    # ====== 步驟 1: 建立文件儲存 ======
    print("📚 步驟 1: 建立文件儲存...")
    document_store = InMemoryDocumentStore()
    document_store.write_documents([
        Document(content="My name is Jean and I live in Paris."),
        Document(content="My name is Mark and I live in Berlin."),
        Document(content="My name is Giorgio and I live in Rome.")
    ])
    print(f"   ✓ 已寫入 {document_store.count_documents()} 個文件\n")

    # ====== 步驟 2: 定義提示模板 ======
    print("💬 步驟 2: 定義提示模板...")
    template = """
    根據以下文件回答問題:
    
    {% for doc in documents %}
    - {{ doc.content }}
    {% endfor %}
    
    問題: {{ question }}
    
    請用繁體中文簡潔回答。
    """
    print("   ✓ 提示模板已建立\n")

    # ====== 步驟 3: 建立組件 ======
    print("🔧 步驟 3: 建立 Pipeline 組件...")
    retriever = InMemoryBM25Retriever(document_store=document_store)
    prompt_builder = PromptBuilder(template=template)
    
    # 使用 Google Gemini
    # 模型選項: "gemini-1.5-flash" (快速便宜) 或 "gemini-1.5-pro" (更強大)
    llm = GoogleAIGeminiGenerator(
        api_key=Secret.from_env_var("GOOGLE_API_KEY"),
        model="gemini-1.5-flash",
        generation_config={
            "temperature": 0.7,
            "top_p": 0.95,
            "max_output_tokens": 1024,
        }
    )
    print("   ✓ 已建立 Retriever")
    print("   ✓ 已建立 PromptBuilder")
    print("   ✓ 已建立 LLM (Google Gemini)\n")

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
    
    results = rag_pipeline.run({
        "retriever": {"query": question},
        "prompt_builder": {"question": question},
    })

    # ====== 步驟 7: 顯示結果 ======
    print("✨ 結果:")
    print(f"   回答: {results['llm']['replies'][0]}\n")
    
    # 顯示完整的 Pipeline 結構
    print("📊 Pipeline 結構:")
    rag_pipeline.show()


if __name__ == "__main__":
    print("=" * 60)
    print("  Haystack RAG Pipeline - Google Gemini 版本")
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
        print("1. 安裝依賴: pip install haystack-ai google-generativeai")
        print("2. 取得 API Key: https://aistudio.google.com/app/apikey")
        print("3. 設定環境變數: $env:GOOGLE_API_KEY='your-key'")
        print("\n💰 費用: Gemini 1.5 Flash 有免費額度!")
