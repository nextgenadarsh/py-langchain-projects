from dotenv import load_dotenv
from langchain_experimental.tools import PythonREPLTool
from agents.qrcode_agent import execute_qrcode_agent
from agents.csv_agent import execute_csv_agent
from agents.router_agent import get_router_agent_executor


if __name__ == "__main__":
    load_dotenv()

    # execute_qrcode_agent()

    # execute_csv_agent()

    router_agent_executor = get_router_agent_executor()
    router_agent_executor.invoke({"input": "which season has the most episodes"})
