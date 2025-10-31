from langchain.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["topic", "style"],
    template="Explain {topic} in a {style} tone using simple examples."
)

prompt = template.format(topic="quantum computing", style="funny")
print(prompt)