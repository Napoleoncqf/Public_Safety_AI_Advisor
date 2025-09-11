import fitz  # 导入PyMuPDF
import ollama
import os

# --- 1. 定义PDF读取函数 ---
def read_pdf_text(file_path):
    """读取PDF文件的全部文本内容"""
    try:
        with fitz.open(file_path) as doc:
            text = ""
            for page in doc:
                text += page.get_text()
            return text
    except Exception as e:
        return f"读取PDF文件时出错: {e}"

# --- 2. 主执行逻辑 ---
def main():
    print("--- “资产一号”点火程序启动 ---")

    # 指定PDF文件路径 (确保它和脚本在同一个文件夹)
    pdf_path = "test.pdf"

    # 检查文件是否存在
    if not os.path.exists(pdf_path):
        print(f"错误：未找到测试文件 '{pdf_path}'。请确保文件已创建并放置在正确位置。")
        return

    # --- 步骤A: 读取PDF内容 ---
    print(f"正在读取文件: {pdf_path}...")
    document_text = read_pdf_text(pdf_path)
    print("PDF内容读取成功！")
    print("---------------------------------")
    print(f"提取到的原文: {document_text.strip()}")
    print("---------------------------------")

    # --- 步骤B: 与Ollama模型交互 ---
    # !!! 注意: 请将 'qwen2:7b' 替换成你实际下载并运行的模型名称 !!!
    # 你可以在终端输入 `ollama list` 来查看你拥有的模型
    model_name = 'qwen2:2b' 
    print(f"正在调用模型: {model_name}...")

    try:
        # 构造提问的prompt
        prompt = f"根据以下内容回答问题：'{document_text.strip()}'。请问，应急管理的最终目标是什么？"

        response = ollama.chat(
            model=model_name,
            messages=[
                {'role': 'user', 'content': prompt},
            ]
        )
        
        print("模型响应成功！")
        print("---------------------------------")
        print(f"模型的回答: {response['message']['content']}")
        print("---------------------------------")
        print("--- 点火成功！系统已打通！ ---")

    except Exception as e:
        print(f"调用Ollama模型时出错: {e}")
        print("--- 点火失败，请检查Ollama服务是否已在后台运行。---")


# --- 运行主函数 ---
if __name__ == "__main__":
    main()