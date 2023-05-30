import openai

class ChatGPT():
    def __init__(self, api_key, file_name):
        openai.api_key = api_key
        self.file_name = file_name
    
    def read_file(self):
        with open(self.file_name) as file:
            return file.read()
    
    def write_file(self, data: str):
        with open(self.file_name, 'w') as file:
            file.write(data)
    
    def generate(self, content: str):
        messages = [{'role': 'user', 'content': content}]
        if content[:2] == '--':
            last_message = self.read_file()
            if last_message:
                messages.append({'role': 'assistant', 'content': last_message})
            content = content[2:]
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages,
            temperature=0.5,
            max_tokens=1000
        )
        message = response['choices'][0]['message']['content']
        self.write_file(message)
        return message
