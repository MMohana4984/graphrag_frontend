import os
import subprocess
import sys
import warnings
import yaml

def run_command(command, error_message):
    try:
        # Suppress warnings explicitly using the PYTHONWARNINGS environment variable
        env = os.environ.copy()
        env['PYTHONWARNINGS'] = 'ignore'
        result = subprocess.run(command, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=env)
        print(result.stdout)
        if result.stderr:
            print(f"Warning: {result.stderr}")
    except subprocess.CalledProcessError as e:
        print(f"{error_message}")
        print(f"Command '{e.cmd}' returned non-zero exit status {e.returncode}.")
        print(e.output)
        print(e.stderr)
        exit(1)

def update_env_file(api_key):
    env_file = '.env'
    with open(env_file, 'w') as file:
        file.write(f'GRAPHRAG_API_KEY={api_key}\n')
    print(f"Updated {env_file} with the provided API key.")

def update_settings_yaml():
    settings_file = 'settings.yaml'
    
    with open(settings_file, 'r') as file:
        settings = yaml.safe_load(file)
    
    if 'llm' in settings and 'model' in settings['llm']:
        settings['llm']['model'] = 'gpt-4o'
    
    with open(settings_file, 'w') as file:
        yaml.safe_dump(settings, file, default_flow_style=False)
    
    print(f"Updated model in {settings_file} to gpt-4o.")

def main():
    # Set PYTHONIOENCODING to utf-8
    os.environ['PYTHONIOENCODING'] = 'utf-8'

    # Preprocessing documents into text files
    print("Running preprocessing.py")
    run_command('py preprocessing.py', "Error during preprocessing")

    # Initialize the GraphRAG index if not already initialized
    if not os.path.exists('settings.yaml'):
        print("Initializing the GraphRAG index")
        run_command('py -m graphrag.index --init --root .', "Error initializing GraphRAG index")
    else:
        print("GraphRAG index already initialized")

    # Prompt user for OpenAI API key
    api_key = input("Please enter your OpenAI API key: ")

    # Update the .env file with the OpenAI API key
    update_env_file(api_key)

    # Set the OpenAI API key environment variable
    os.environ['GRAPHRAG_API_KEY'] = api_key

    # Verify that the input directory contains text files
    if not any(fname.endswith('.txt') for fname in os.listdir('input')):
        print("No text files found in input directory")
        exit(1)
    else:
        print("Text files found in input directory")

    # Update the settings.yaml file to use gpt-4o model
    update_settings_yaml()

    # Run the GraphRAG index with the provided API key
    print("Running the GraphRAG index")
    run_command('py -m graphrag.index --root .', "Error running GraphRAG index")


    # Start the Streamlit app
    print("Starting the Streamlit app")
    run_command('streamlit run app.py', "Error starting Streamlit app")

if __name__ == "__main__":
    main()
