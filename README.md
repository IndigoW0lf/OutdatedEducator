# OutdatedEducator
This project allows users to retrieve outdated facts and concepts based on a specific country and year. It leverages OpenAI's GPT model to generate the responses, providing a unique and engaging experience for users.

## Features

- Interactive Web Interface: Users can select a country and year to get relevant outdated facts.
- Powered by OpenAI: The responses are generated using OpenAI's GPT model, providing intelligent and context-aware answers.
- Cross-Origin Support: Implements CORS to allow cross-origin requests.

## Installation & Setup

### Requirements

- Python 3.x
- Flask
- Flask-CORS
- OpenAI

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/IndigoW0lf/OutdatedEducator.git
   ```

2. Navigate to the project directory:

   ```bash
   cd OutdatedEducator
   ```

3. Install the required dependencies:

   ```bash
   pip install flask flask-cors openai
   ```

### Configuration

To run this project, you'll need to configure your OpenAI API key:

1. **Obtain an API Key**: Follow the instructions in [OpenAI's official documentation](https://platform.openai.com/docs/) to obtain your key.

2. **Set the Environment Variable**: Configure your project by setting up an environment variable named OPENAI_API_KEY with your actual API key value. Depending on your operating system, use the following command:

   For Unix/Linux/macOS:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```

   For Windows:
   ```bash
   set OPENAI_API_KEY=your-api-key-here
   ```

Replace `'your-api-key-here'` with your actual API key.

**Note**: Be sure to keep your API key private and secure. Do not share it publicly or commit it to a public repository.

## Running the Project

<img align="right" alt="Screenshot" src="Screenshot 2023-08-07 at 9.07.29 PM.png" width="520" height="520"/>  

After setting up the environment variable, you can run the Flask application:

```bash
cd backend
```

```bash
python app.py
```

The application will start, and you can access it at http://127.0.0.1:5000/.

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss the proposed change.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

Thanks to OpenAI for providing the AI engine that powers this application.
