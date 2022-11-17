import openai
import pkg_resources

class Helper():
    def __init__(self, prompt=''):
        self.prompt = prompt
        self.path = 'examples.txt'
        self.model = 'text-davinci-002'
        self.temperature = 0.5

    def fetch_examples(self):
        stream = pkg_resources.resource_stream(__name__, self.path)
        data = stream.read().decode("utf-8").splitlines()

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
