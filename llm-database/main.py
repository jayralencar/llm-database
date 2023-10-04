import openai
from argparse import ArgumentParser
from tools.QueryStudents import QueryStudents
from tools.QueryCronograma import QueryCronograma

class LLMDatase():
    def __init__(self, **args) -> None:
        self.args = args
        openai.api_key = args["openai_key"]
        self.database_path = args["database_path"]
        self.functions = [QueryStudents.openai_schema,QueryCronograma.openai_schema]
    
    def call_model(self, messages):
        response = openai.ChatCompletion.create(
            model=self.args["model"],
            messages= messages,
            temperature=0,
            functions=self.functions,
        )
        return response

    def run(self, user_question):
        instruction = """You are an agent that has access to a database and can perform queries before answering the user's question.

You have access to a SQLite database. You can use the SQLite language to query the database. Use pattern matching to find the answer to the user's question."""

        messages = [
            {"role":"system","content":instruction},
            {"role":"user","content":user_question}
        ]

        while True:
            response = self.call_model(messages)
            finish_reason = response["choices"][0]["finish_reason"]
            if finish_reason == "function_call":
                ai_message = dict(response["choices"][0]["message"])
                function_name = response["choices"][0]["message"]["function_call"]["name"]

                messages.append(ai_message)
            
                function_call = None
                function_call = eval(function_name).from_response(response)

                if function_call:
                    function_response = function_call(database_path=self.database_path)
                    messages.append({"role":"function","name":function_name,"content":function_response})
                print(messages)
            else:
                return response["choices"][0]["message"]["content"]
                break

                    
if __name__ == "__main__":
    # Create an ArgumentParser object.
    parser = ArgumentParser(description="Executa a extração de alegações considerando o dataset de alegações")
    # Add arguments
    parser.add_argument("--database_path", type=str, default="example.db", help="Path to the SQLite database file")
    parser.add_argument("--openai_key", type=str, help="OpenAI API key")
    parser.add_argument("--model", type=str, default="gpt-3.5-turbo", help="Model name")

    args = parser.parse_args()

    c = LLMDatase(**vars(args))
    
    while True:
        user_question = input("User Qustion: ")
        print("AI: ", c.run(user_question))