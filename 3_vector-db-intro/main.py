import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_pinecone.vectorstores import PineconeVectorStore

def do():
    print("Injesting...")
    loader = TextLoader("./blog-text-1.txt")
    document = loader.load()
    
    print("Splitting...")
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0)
    texts = text_splitter.split_documents(document)
    # print(texts)
    
    embeddings = OllamaEmbeddings(model="llama3")
    
    print("Injesting...")
    PineconeVectorStore.from_documents(texts, embeddings, index_name=os.environ['PINECONE_INDEX_NAME'])
    print("Finish ")


if __name__ == "__main__":
    load_dotenv()
    print("Vector DB Intro !!")
    do()
    

