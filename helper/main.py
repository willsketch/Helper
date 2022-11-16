import os
import openai
import argparse

class Helper():
    def __init__(self, prompt=''):
        self.prompt = prompt
        self.path = 'helper/examples.txt'
        self.model = 'text-davinci-002'
        self.temperature = 0.5

    def fetch_examples(self):
        with open(self.path) as f:
            data = f.read().splitlines()

        return data

    def make_prompt(self):
        # ex= self.fetch_examples()
        ex_string= '\n'.join(self.fetch_examples()) + '\n' # examples in string format
        query = ex_string + "\n" +"input:" + self.prompt + "\n"
        return query

    def run_engine(self):
        response = openai.Completion.create(
            model = self.model,
            prompt = self.make_prompt(),
            max_tokens = 100,
            temperature= self.temperature,
            stop="\ninput:"
        )
        return response

if __name__ == '__main__':
    openai.api_key = os.getenv("OPENAI_API_KEY")
    parser = argparse.ArgumentParser()
    parser.add_argument('prompt', help='What do ypu need help with', default= '')
    query = parser.parse_args().prompt
    response = Helper(query).run_engine()
    print(response.choices[0].text)
