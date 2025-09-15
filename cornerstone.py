# cornerstone.py
# 作战目标：完成LangChain任务一和任务二

import os
from langchain_community.chat_models import ChatOllama
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# --------------------------------------------------------------------------
# 任务一：用ChatOllama类成功调用本地qwen:7b模型
# 执行标准：在22:00前，看到模型成功返回信息。
# --------------------------------------------------------------------------
def mission_one_llm_connection_test():
    """
    测试与本地Ollama模型的连接并获取响应。
    """
    print("--- [任务一] 正在启动：测试与Ollama的连接... ---")
    try:
        # 初始化模型，使用你已确认可用的模型名称
        llm = ChatOllama(model="qwen:7b") 

        # 发起一次简单的调用
        print("向模型发送调用请求...")
        response = llm.invoke("你好，请确认你已准备就绪。")
        
        print("模型响应成功！")
        print("---------------------------------")
        print(f"模型返回: {response.content}")
        print("---------------------------------")
        print("--- [任务一] 执行成功！---\n")
        return True
    except Exception as e:
        print(f"--- [任务一] 执行失败！错误: {e} ---")
        print("--- 请检查Ollama服务是否已在后台运行，以及模型名称是否正确。---\n")
        return False

# --------------------------------------------------------------------------
# 任务二：用PyPDFLoader和TextSplitter成功加载并分割test.pdf
# 执行标准：在23:30前，在终端看到被分割的文本块列表。
# --------------------------------------------------------------------------
def mission_two_document_processing():
    """
    加载并分割指定的PDF文档。
    """
    print("--- [任务二] 正在启动：文档处理... ---")
    
    # 确保你的test.pdf文件与此脚本位于同一目录下
    pdf_path = "test.pdf"
    if not os.path.exists(pdf_path):
        print(f"--- [任务二] 执行失败！错误: 未找到文件 '{pdf_path}' ---")
        return None

    try:
        # 1. 加载文档
        print(f"正在加载文档: {pdf_path}...")
        loader = PyPDFLoader(pdf_path)
        docs = loader.load()
        print("文档加载成功。")

        # 2. 分割文档
        print("正在进行文本分割...")
        # chunk_size: 每个块的最大字符数。
        # chunk_overlap: 相邻块之间重叠的字符数，以保证语义连续性。
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        splits = text_splitter.split_documents(docs)
        
        print(f"文本分割成功！文档被分割成了 {len(splits)} 块。")
        print("--- [任务二] 执行成功！---\n")
        return splits
    except Exception as e:
        print(f"--- [任务二] 执行失败！错误: {e} ---")
        return None

# --------------------------------------------------------------------------
# 主执行程序
# --------------------------------------------------------------------------
if __name__ == "__main__":
    print("====== 代号‘基石’行动 开始 ======")
    
    # 执行任务一
    mission_one_successful = mission_one_llm_connection_test()
    
    # 只有在任务一成功后才继续执行任务二
    if mission_one_successful:
        # 执行任务二
        document_splits = mission_two_document_processing()
        
        if document_splits:
            print("====== 最终产出：分割后的文本块列表 ======")
            # 打印每一块的内容以供查验
            for i, doc_split in enumerate(document_splits):
                print(f"--- [文本块 {i+1}] ---")
                print(doc_split.page_content)
                print("-" * 20)
    
    print("====== 代号‘基石’行动 结束 ======")