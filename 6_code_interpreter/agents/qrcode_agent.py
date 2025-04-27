from dotenv import load_dotenv
from langchain import hub
from langchain_ollama import OllamaLLM
from langchain.agents import create_react_agent, AgentExecutor
from langchain_experimental.tools import PythonREPLTool
from langchain_experimental.agents import create_csv_agent


def get_qrcode_agent_executor() -> AgentExecutor:
    instructions = """You are an agent designed to write and execute python code to answer questions.
    You have access to a python REPL, which you can use to execute python code.
    If you get an error, debug your code and try again.
    Only use output of your code to answer the question.
    You might know the answer without running any code, but you should still run the code to get the answer.
    If it does not seem like you can write the code to answer the question, just return "I don't know" as the answer.    
    """

    base_prompt = hub.pull("langchain-ai/react-agent-template")
    prompt = base_prompt.partial(instructions=instructions)

    tools = [PythonREPLTool()]
    agent = create_react_agent(
        prompt=prompt, llm=OllamaLLM(temperature=0, model="llama3"), tools=tools
    )
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    return agent_executor


def execute_qrcode_agent():
    qrcode_agent_executor = get_qrcode_agent_executor()
    res = qrcode_agent_executor.invoke(
        input={
            "input": "generate and save in current working directoy child directory named 'qrcodes' 4 QR codes that point to www.udemy.com/courses/langchain, you have qrcode package install already"
        }
    )
    print(res)
