# README

This project is focused on creating automated READMEs for various projects. By using OpenAI and their GPT-3 API, the task of writing out a detailed README can be automated. This project uses two config files, config.json and sec_config.json, that are used to set various parameters that allow the user to customize their outputs. The project utilizes logging which is through config.json and stored at the parameter "LOGGING". Users must have an OpenAI API key is used in order to access OpenAI services.

The core functionality of the code is to process the text entered by the user. This takes in the docs stored at config.json "DOCUMENT_PATH" and is processed to fit the max token limit through the Chunk_code function which takes the text and breaks it into chunks. After, the process_text_with_GPT function is used to generate responses to the chunks passed in. Responses gathered are then joined together to form one entire response. Finally, to wrap up the code, the save_result_to_file function takes the output and stores it at the directory found at config.json "OUTPUT_DIR".

In order for the code to successfully run, users must install the correct libraries and ensure their config files are set correctly. Dependencies include os json openai,and logging. §§ COM
script that generates subchapter text in markdown format

## Requirements
- Python 3.6 or above 
- OpenAI API key
- JSON file with configuration

## Setup

1. Clone/download the project from Github
2. Also download the configuration `config.json` and `api_config.json` 
3. Get an OpenAI API key and save it in `api_config.json`
4. Install the required packages using the provided `requirements.txt`

## Usage 

1. Edit the configuration JSON for defining the parameters
2. Run `main.py` to execute the project
3. The generated responses from OpenAI will be saved in the `OUTPUT_DIR` defined in `config.json`

## Configuration

- `CHUNK_SEPERATOR`: Character used in the code to split different parts of the code
- `DOCUMENT_PATH`: Path of the main file containing the code
- `LOGGING`: Logging output file
- `MAX_TOKENS`: Maximum number of characters allowed per text submission to OpenAI
- `OUTPUT_DIR`: Output directory for generated responses. Directory is created if not found
- `PREPROMPT`: Text to be passed before the code string to OpenAI
- `ENGINE`: Name of the OpenAI engine being used 