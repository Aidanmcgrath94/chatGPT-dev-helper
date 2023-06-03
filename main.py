import os
import json
import openai
import logging 

# Open the JSON file and load the data
with open('config.json') as json_file:
    config_data = json.load(json_file)

# Open the JSON file and load the data
with open('sec_config.json') as json_file:
    api_config = json.load(json_file)

openai.api_key = api_config["OPENAI_API_KEY"]
logging.basicConfig(filename=config_data["LOGGING"], level=logging.INFO)

def chunk_code(code, max_tokens):
    lines = code.split(config_data["CHUNK_SEPERATOR"])
    chunks = []
    chunk = ""
    for line in lines:
        # Add the size of the line + 1 for newline
        if len(chunk) + len(line) + 1 > max_tokens:
            chunks.append(chunk)
            chunk = line + '\n'
        else:
            chunk += line + '\n'
    chunks.append(chunk)  # Don't forget the last chunk
    return chunks

def process_text_with_gpt(document_path, pre_prompt, max_tokens):
    with open(document_path, 'r') as file:
        text = file.read()

    full_prompt = pre_prompt + text
    wrap_limit = max_tokens - len(pre_prompt)

    # Split the text into chunks that are less than max_tokens
    chunks = chunk_code(full_prompt, wrap_limit)

    responses = []
    for chunk in chunks:
        response = openai.Completion.create(
            engine=config_data["ENGINE"], 
            prompt=chunk,
            max_tokens=max_tokens
        )
        responses.append(response.choices[0].text.strip())

    # Combine the responses
    combined_responses = ' '.join(responses)
    logging.info(f"Generating response for {document_path}...")
    logging.info(f"Generated response as {combined_responses}")
    
    return combined_responses

def save_result_to_file(output_path, result):
    with open(output_path, 'w') as file:
        file.write(result)

def main():
    document_path = config_data["DOCUMENT_PATH"]
    output_dir = config_data["OUTPUT_DIR"]
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "README.md")
    pre_prompt = config_data["PREPROMPT"]
    max_tokens = int(config_data["MAX_TOKENS"])

    files = []
    for filename in os.listdir(document_path):
        file_path = os.path.join(document_path, filename)
        if os.path.isfile(file_path):
            name_without_extension = os.path.splitext(filename)[0]
            files.append({
                'cleanname': name_without_extension,
                'fullname': document_path+filename,
            })

    for file in files:
        logging.info("Running for " + file['cleanname'])
        result = process_text_with_gpt(file['fullname'], pre_prompt, max_tokens)
        output_file_path = os.path.join(output_dir, f"{file['cleanname']}.md")
        save_result_to_file(output_file_path, result)
        logging.info(f"Result saved to {output_file_path}")

if __name__ == "__main__":
    main()
