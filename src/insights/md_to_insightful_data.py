import os
import yaml
import time
from urllib.parse import urlparse, quote
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

def load_config():
    with open('config/config.yaml', 'r') as file:
        return yaml.safe_load(file)

config = load_config()

llm = ChatGroq(
    temperature=0, 
    groq_api_key=config['insights']['groq_api_key'], 
    model_name=config['insights']['model_name']
)

def prompt_splitter(prompt):
    if len(prompt) > 20000:
        split_prompt = []
        while True:
            if len(prompt) == 0:
                break
            split_prompt.append(prompt[0:20000])
            prompt = prompt[20000:]

        return split_prompt

    return [prompt]

def get_llm_insights(markdown_content):
    while True:
        try:
            text = ''
            prompts = prompt_splitter(markdown_content)
            if prompts is None:
                return ''
            for prompt in prompts:
                system = "Please conduct a thorough analysis of the provided content. Ensure that all relevant information is formatted clearly and concisely, and remove any irrelevant details."
                human = "Content to analyze:\n{markdown_content}."
                prompt_chat = ChatPromptTemplate.from_messages([("system", system), ("human", human)])
                
                chain = prompt_chat | llm
                response = chain.invoke({'markdown_content': prompt}).content
                
                find_all_subs = [i for i in range(len(response)) if response.startswith('```', i)]
                if len(find_all_subs) == 2:
                    response = response[find_all_subs[0] + 3: find_all_subs[1] - 3]
                text += response + "\n"
                print('\tDone')
            break
        except:
            print('wait for 60 sec')
            time.sleep(60)

    return text

def safe_write(data, path):
    """Safely writes data to a file."""
    try:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(data)
    except Exception as e:
        print(f"An error occurred when writing to {path}: {e}")

def generate_filename(url):
    """Generates a filename from a URL by using its path and query."""
    base_name = url.replace("/", "_").replace("=", "_").replace("&", "_")
    safe_name = quote(base_name, safe="")
    return f"{safe_name}.md"

def scrape_site(base_url, fol_name):
    files_in_fol = os.listdir(fol_name)

    new_fol_data = []
    if os.path.exists(fol_name + "//new"):
        new_fol_data = os.listdir(fol_name + "//new")

    cnt = 1
    for x in files_in_fol:
        if x.split('.')[-1] == 'md':
            cnt += 1

    i = len(new_fol_data)
    for x in files_in_fol:
        if x.split('.')[-1] == 'md':
            if x not in new_fol_data:
                markdown = open(fol_name + '\\' + x, "r", encoding="utf-8").read()

                page_title = markdown.split('\n')[0]
                current_url = (markdown.split('## PageLink: ')[-1]).split('\n')[0]

                i += 1
                print(i, '/', cnt)
                print(x)
                print(page_title)
                print(current_url)

                insights = get_llm_insights(markdown)

                page_title = markdown.split('\n')[0]
                current_url = (markdown.split('## PageLink: ')[-1]).split('\n')[0]

                os.system(f'mkdir "{fol_name}\\new"')

                markdown = f"# {page_title}\n## PageLink: {current_url}\n## PageData:\n{insights.replace('```','')}"
                if markdown:
                    filename = generate_filename(current_url)
                    fol_name1 = fol_name + '\\new'
                    file_path = os.path.join(fol_name1, filename)
                    safe_write(markdown, file_path)
                print('----------------------------------------------------\n')
