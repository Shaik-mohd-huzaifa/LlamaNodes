from ..Services.LLM_Service import LLM
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from ..Services.Lambda_Service import call_lambda


def llm_configuration_and_execution(message, parameters, user_input):
    max_tokens = parameters.get("max_tokens")
    temperature = parameters.get("temperature")
    model = parameters.get("model")

    llm_instance = LLM(model=model, max_token=max_tokens, temperature=temperature)
    llm = llm_instance.get_llm()

    template = """
    System: {system_prompt}
    User Query: {user_prompt}
    """

    prompt = ChatPromptTemplate.from_template(template=template)

    output_parser = StrOutputParser()

    # Execute the chain
    chain = prompt | llm | output_parser
    return chain.invoke({"system_prompt": user_input, "user_prompt": user_input})


def flow_execution(nodes, input_data):
    # Initialize dynamic_input as a dictionary with `input_data` values
    dynamic_input = dict(input_data)
    final_output = ""

    for node in nodes:
        if node["node_type"] == "LLM":
            input_variable = node.get("input_variable")
            output_variable = node.get("output_variable")

            # Fetch the input for this node's LLM execution
            node_input = dynamic_input.get(input_variable)
            if node_input is None:
                continue  # Skip if the expected input variable is missing

            output = llm_configuration_and_execution(
                node["messages"], node["parameters"], node_input
            )

            # Store the output back in `dynamic_input`
            dynamic_input[output_variable] = output
            final_output = output

    # Return the final state of dynamic_input
    return final_output
