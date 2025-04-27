from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain import hub
from langchain_ollama import OllamaLLM, OllamaEmbeddings

from dotenv import load_dotenv


def create_vector_store():
    pdf_path = "./sample_file.pdf"
    loader = PyPDFLoader(file_path=pdf_path)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(
        chunk_size=1000, chunk_overlap=30, separator="\n"
    )
    docs = text_splitter.split_documents(documents=documents)

    embeddings = OllamaEmbeddings(model="llama3")
    vector_store = FAISS.from_documents(documents=docs, embedding=embeddings)
    vector_store.save_local("faiss_index_react")


def chat():
    embeddings = OllamaEmbeddings(model="llama3")
    new_vectorstore = FAISS.load_local(
        "/Users/adarshk/Documents/nextgenadarsh/git/py-langchain-projects/4_vector-store-inmemory/faiss_index_react",
        embeddings,
        allow_dangerous_deserialization=True,
    )

    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
    combine_docs_chain = create_stuff_documents_chain(
        OllamaLLM(model="llama3"), retrieval_qa_chat_prompt
    )
    retrieval_chain = create_retrieval_chain(
        new_vectorstore.as_retriever(), combine_docs_chain
    )
    res = retrieval_chain.invoke({"input": "Give me the gist of ReAct in 3 sentense"})
    print(res["answer"])


if __name__ == "__main__":
    load_dotenv()

    print("Welcome !!")
    # create_vector_store()
    chat()
