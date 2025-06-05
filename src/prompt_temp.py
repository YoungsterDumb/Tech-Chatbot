from langchain_core.prompts import PromptTemplate


PROMPT_TEMPLATE = """
Bạn là trợ lý AI công nghệ hữu dụng, dùng những thông tin đã được cung cấp để trả lời câu hỏi của người dùng
Nếu thông tin không có, hãy nói bạn chưa có thông tin đầy đủ để trả lời.


Đoạn trích tài liệu (Context):
{context}

Câu hỏi của người dùng: 
{question}

Trả lời trực tiếp, không lòng vòng, trả lời đúng ngôn ngữ và nội dung của câu hỏi 
"""

def set_prompt_template(prompt_template):
    prompt = PromptTemplate(
        template = prompt_template,
        input_variables = ["context", "question"]
    )
    
    return prompt

prompt = set_prompt_template(PROMPT_TEMPLATE)
    