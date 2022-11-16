## Helper
This is a simple  cli tool to help you with your linux  and git commands  
(__still in progress ...__)
## About Helper
Helper was built with openai api using the model 'davinci'
prompt is designed with examples (to be found in examples.txt) of git commands and more will be added.
As for the command line , argparse was used

## Usage
To use Helper , you will need openai api key. Follow these steps to generate the api key or visit this [article](https://elephas.app/blog/how-to-create-openai-api-keys-cl5c4f21d281431po7k8fgyol0) for more details.
 * step1: signup [here](https://beta.openai.com/signup) and create an openai account
 * step2: go to openai api key page [link](https://beta.openai.com/account/api-keys)
 * step3 : click "Create new secret key"

Now that you have your api key, run the following command in your terminal
```
export OPENAI_API_KEY="your_OPENAI_API_KEY"
```
You're ready to use helper in your terminal. Here is an example of how helper can be used.

``` 
helper "Linux command for  ip address"
```
the output to the command above is :
``` 
output:ip addr
```

