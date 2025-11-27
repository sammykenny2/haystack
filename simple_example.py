"""
最簡單的 Haystack 範例 - 不需要 API Key

這個範例展示如何使用本地模型運行 Haystack
"""

from haystack import Pipeline, Document
from haystack.components.retrievers import InMemoryBM25Retriever
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.components.builders import PromptBuilder

def main():
    """使用本地組件建立簡單的檢索系統"""
    
    # 建立文件儲存
    print("建立文件儲存...")
    document_store = InMemoryDocumentStore()
    document_store.write_documents([
        Document(content="Python is a high-level programming language."),
        Document(content="JavaScript is commonly used for web development."),
        Document(content="Java is known for its 'write once, run anywhere' capability."),
        Document(content="C++ is an extension of the C programming language."),
    ])
    
    # 建立檢索器
    print("建立檢索器...")
    retriever = InMemoryBM25Retriever(document_store=document_store)
    
    # 建立提示建構器
    template = """
    根據以下文件回答問題:
    
    {% for doc in documents %}
    - {{ doc.content }}
    {% endfor %}
    
    問題: {{ query }}
    
    請提供相關的文件內容。
    """
    prompt_builder = PromptBuilder(template=template)
    
    # 組裝 Pipeline
    print("組裝 Pipeline...")
    pipeline = Pipeline()
    pipeline.add_component("retriever", retriever)
    pipeline.add_component("prompt_builder", prompt_builder)
    pipeline.connect("retriever.documents", "prompt_builder.documents")
    
    # 執行查詢
    query = "What is Python?"
    print(f"\n查詢: {query}\n")
    
    result = pipeline.run({
        "retriever": {"query": query},
        "prompt_builder": {"query": query}
    })
    
    # 顯示結果
    print("=" * 60)
    print("生成的提示詞:")
    print("=" * 60)
    print(result["prompt_builder"]["prompt"])
    print("=" * 60)
    
    # 顯示找到的文件
    print("\n找到的相關文件:")
    documents = result["retriever"]["documents"]
    for i, doc in enumerate(documents, 1):
        print(f"{i}. {doc.content}")


if __name__ == "__main__":
    print("=" * 60)
    print("  Haystack 簡單範例 (無需 API Key)")
    print("=" * 60)
    print()
    main()
    print("\n執行完成!")
