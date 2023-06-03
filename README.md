# README

This is a project designed to generate code using [OpenAI](https://openai.com) based on the code you pass in. This project uses the OpenAI modules on python to break down the code, process and generate a response based on the provided code.

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