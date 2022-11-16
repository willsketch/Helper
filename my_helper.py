import os
import openai
import argparse
from helper.main import Helper

def cli():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    parser = argparse.ArgumentParser()
    parser.add_argument('prompt', help='What do you need help with', default= '')
    query= parser.parse_args().prompt
    response = Helper(query).run_engine()
    print(response.choices[0].text)

if __name__ == '__main__':
    cli()
