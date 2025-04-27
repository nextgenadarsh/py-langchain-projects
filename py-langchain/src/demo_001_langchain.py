from typing import Tuple
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
# from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

from dotenv import load_dotenv

from src.agents import linkedin_lookup_agent
from src.parsers.summary_parser import Summary, summary_parser
from src.scrapper.linkedin import scrape_linkedin_profile

print("001 Simple Example of Langchain !!")

def get_user_info(name: str) -> Tuple[Summary, str]:
    # linkedin_data = """
    #     Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a businessman known for his leadership of Tesla, SpaceX, and X (formerly Twitter). Since 2025, he has been a senior advisor to United States president Donald Trump and the de facto head of the Department of Government Efficiency (DOGE). Musk has been the wealthiest person in the world since 2021; as of March 2025, Forbes estimates his net worth to be US$345 billion. He was named Time magazine's Person of the Year in 2021.
    #     Born to a wealthy family in Pretoria, South Africa, Musk emigrated in 1989 to Canada. He graduated from the University of Pennsylvania in the U.S. before moving to California to pursue business ventures. In 1995, Musk co-founded the software company Zip2. Following its sale in 1999, he co-founded X.com, an online payment company that later merged to form PayPal, which was acquired by eBay in 2002. That year, Musk also became a U.S. citizen. 
    # """

    # linkedin_profile_url = linkedin_lookup_agent.lookup(name)
    linkedin_profile_url = "http://linkedin.com/in/nextgenadarsh/"
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url, True)
    
    summary_template = """
        given the information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
        
        \n{format_instructions}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], 
        template=summary_template,
        partial_variables={'format_instructions': summary_parser.get_format_instructions()}
    )
    
    # llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    llm = ChatOllama(temperature=0, model="llama3")
    # llm = ChatOllama(temperature=0, model="mistral")

    # chain = summary_prompt_template | llm | StrOutputParser()
    # chain = LLMChain(llm=llm, prompt= summary_prompt_template)
    chain = summary_prompt_template | llm | summary_parser

    res: Summary = chain.invoke(input={"information": linkedin_data})    
    print("Final Result: ******** ", res)
    return res, linkedin_data.get("photoUrl")

if __name__ == "__main__":
    load_dotenv()

    get_user_info("Adarsh Kumar")
