import ollama
from rich import print
from rich.progress import track
from rich.console import Console
from rich.logging import RichHandler
import logging
import os

# 设置Ollama服务器地址环境变量
# 可以通过环境变量传入或直接在此设置
os.environ["OLLAMA_HOST"] = "127.0.0.1:11434"

# 初始化Rich控制台和日志系统
console = Console()
logging.basicConfig(
    level="NOTSET",  # 设置日志级别为最低，记录所有日志
    format="%(message)s",  # 日志格式
    datefmt="[%X]",  # 时间格式
    handlers=[RichHandler(console=console)]  # 使用Rich处理日志输出
)
log = logging.getLogger("rich")

def complete_output():
    """
    完整输出模式 - 一次性获取完整响应
    """
    console.print("[bold yellow]完整输出模式启动...[/bold yellow]")

    # 构造对话消息
    messages = [
        {
            "role": "system",
            "content": "你是一个python开发专家,针对问题直接返回代码,如果办不到直接回复暂时无法解决"
        },
        {
            "role": "user",
            "content": "请使用pygame编写一个弹球游戏"
        }
    ]

    # 发送请求并获取完整响应
    try:
        response = ollama.chat(
            model="deepseek-r1:1.5b",
            messages=messages,
            stream=False  # 关闭流式输出
        )

        # 输出完整响应
        console.print("\n[bold green]完整响应:[/bold green]")
        console.print(response['message']['content'])

    except Exception as e:
        log.error(f"请求失败: {str(e)}")

def stream_output():
    """
    流式输出模式 - 实时显示响应内容
    """
    console.print("[bold yellow]流式输出模式启动...[/bold yellow]")

    # 构造对话消息
    messages = [
        {
            "role": "system",
            "content": "你是一个python开发专家,针对问题直接返回代码,如果办不到直接回复暂时无法解决"
        },
        {
            "role": "user",
            "content": "请使用pygame编写一个弹球游戏"
        }
    ]

    console.print("生成中...")
    console.print("AI响应:\n")

    try:
        # 发送流式请求
        stream = ollama.chat(
            model="deepseek-r1:1.5b",
            messages=messages,
            stream=True  # 启用流式输出
        )

        # 实时输出响应内容
        for chunk in stream:
            print(chunk['message']['content'], end="", flush=True)

        console.print("\n[bold green]生成完成[/bold green]")

    except Exception as e:
        log.error(f"请求失败: {str(e)}")

if __name__ == '__main__':
    # 用户可以选择输出模式
    console.print("请选择输出模式:")
    console.print("1. 完整输出模式")
    console.print("2. 流式输出模式")

    choice = input("请输入选择(1/2): ")

    if choice == "1":
        complete_output()
    elif choice == "2":
        stream_output()
    else:
        console.print("[bold red]无效选择![/bold red]")
