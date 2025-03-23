from langchain_core.prompts import PromptTemplate

# Template
template = PromptTemplate(
    template="""
    Summarize the research paper titled "{paper}".  

    **Explanation Style:** {style}  
    (If "Technical," use domain-specific terminology and focus on methodologies and findings.  
    If "Non-Technical," explain in simple terms, avoiding jargon.  
    If "Beginner-friendly," provide a mix of both technical and simple explanations.)  

    **Summary Length:** {length}  
    (The response should be concise, well-structured, and informative.)  

    **Output Format:**  
    - **Title:** {paper}  
    - **Summary:** (Generated based on the requested explanation style and length.)  
    - **Key Points:** (Bullet points summarizing the core findings of the paper.)  

    Now, generate the summary.
    """,
    input_variables=["paper", "style", "length"],
    validate_template=True,
)

template.save("template.json")
