from langchain_core.prompts import ChatPromptTemplate
from const import DATASET_SUMMARY_PROMPT_TEMPLATE

async def dataset_summary_async(llm, sample_dataset_str: str, rows: int, cols: int, schema: str) -> str:
    """Asynchronous function to generate dataset summary"""
    prompt_template = ChatPromptTemplate.from_template(DATASET_SUMMARY_PROMPT_TEMPLATE)
    prompt = prompt_template.format(sample_dataset=sample_dataset_str, rows=rows, cols=cols, schema=schema)
    return await llm.apredict(prompt)

def dataset_summary(llm, sample_dataset_str: str, rows: int, cols: int, schema: str) -> str:
    """Asynchronous function to generate dataset summary"""
    prompt_template = ChatPromptTemplate.from_template(DATASET_SUMMARY_PROMPT_TEMPLATE)
    prompt = prompt_template.format(sample_dataset=sample_dataset_str, rows=rows, cols=cols, schema=schema)
    return llm.predict(prompt)