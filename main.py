# from src.manual_markdown import DeMarkdownStep  # adjust filename
# from src.datacontract import NoSettings

# def main():
#     step = DeMarkdownStep(set())

#     result = step.run(None)

#     print(f"Found {len(result)} markdown files")
#     for doc in result:
#         print(doc)

# if __name__ == "__main__":
#     main()

    


from rag_md_engine.datacontract import MarkdownDataContract
from rag_md_engine.step_executor import BaseStepExecutor

from rag_md_engine.manual_markdown import DeMarkdownStep
 
hilfe_documents: list[MarkdownDataContract]
with BaseStepExecutor() as exe:
    hilfe_documents, _ = exe(DeMarkdownStep, set(), None)[0]#

    print("document__", hilfe_documents)
