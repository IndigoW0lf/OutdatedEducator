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
   cd graduation-facts
   ```

3. Install the required dependencies:

   ```bash
   pip install flask flask-cors openai
   ```

### Obtaining the OpenAI API Key

To run this project, you'll need an API key from OpenAI. Follow these steps to obtain the key:

1. **Create an OpenAI Account**: If you don't have an OpenAI account, create one by visiting [OpenAI's signup page](https://platform.openai.com/signup).

2. **Subscribe to a Plan**: Depending on your needs, you may need to subscribe to a paid plan. OpenAI offers different plans, including some free options. Review the pricing details on [OpenAI's pricing page](https://openai.com/pricing).

3. **Access API Key**: Once logged in, navigate to the [API Keys page](https://platform.openai.com/account/api-keys) on your OpenAI Dashboard. From there, you'll find your API key(s). If you don't see any, you may need to create one following OpenAI's provided instructions.

4. **Configure Your Project**: After obtaining your API key, set it as an environment variable in your terminal where the project will run. Depending on your operating system, use the following command:

   For Unix/Linux/macOS:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```

   For Windows:
   ```bash
   set OPENAI_API_KEY=your-api-key-here
   ```

Replace `'your-api-key-here'` with your actual API key.

Please consult OpenAI's [official documentation](https://platform.openai.com/docs/) for further details and any specific requirements or restrictions related to your chosen plan.

**Note**: Be sure to keep your API key private and secure. Do not share it publicly or commit it to a public repository.

### Configuration

You'll need to configure your OpenAI API key. Set up an environment variable named OPENAI_API_KEY with your actual API key value.

For Unix/Linux/macOS:

```bash
export OPENAI_API_KEY='your-api-key-here'
```

For Windows:

```bash
set OPENAI_API_KEY=your-api-key-here
```

## Running the Project

After setting up the environment variable, you can run the Flask application:

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
