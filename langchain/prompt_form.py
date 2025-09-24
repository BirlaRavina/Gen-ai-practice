from langchain.prompts import PromptTemplate

prompt1 = PromptTemplate(
    input_variables=['country'],
    template= 'give me the information about {county}'
)

prompt_format = prompt1.format(county = 'India')
print(prompt_format)

prompt2 = PromptTemplate.from_template('give me the information of the {state}')
print(prompt2.format(state = 'Madhya Pradesh'))