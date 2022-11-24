import openai
import pkg_resources

class Helper():
    """
    This class creates a prompt and queries the openai api
    """
    def __init__(self, prompt=''):
        self.prompt = prompt
        self.path = 'examples.txt'
        self.model = 'text-davinci-002'
        self.temperature = 0.5

    def fetch_examples(self)-> list:
        """
        fetch examples to be used in designing the api
        returns the examples as a list of the examples
        """
        with pkg_resources.resource_stream(__name__, self.path) as stream:
            data = stream.read().decode("utf-8").splitlines()

        return data

    def make_prompt(self) -> str:
        """
        this function designs the prompt: it concatenates your prompt to the examples
        returns a string
        """
        ex_string= '\n'.join(self.fetch_examples()) + '\n' # examples in string format
        query = ex_string + "\n" +"input:" + self.prompt + "\n"
        return query

    def run_engine(self):
        """
        this function runs the openai api and returns the openai response
        """
        response = openai.Completion.create(
            model = self.model,
            prompt = self.make_prompt(),
            max_tokens = 100,
            temperature= self.temperature,
            stop="\ninput:"
        )
        return response
