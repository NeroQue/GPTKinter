# GPTKinter

A desktop application for chatting with ChatGPT built with Python and CustomTkinter.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Features

- Chat with ChatGPT directly from your desktop
- Modern, dark-themed user interface
- Clear conversation history with one click
- Fast and lightweight

## Prerequisites

- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/NeroQue/GPTKinter.git
   cd GPTKinter
   ```

2. **Install uv** (if you don't have it)
   ```bash
   pip install uv
   ```

3. **Install dependencies**
   ```bash
   uv sync
   ```

4. **Set up your API key**
   
   Create a `.env` file in the project folder and add your OpenAI API key:
   ```
   API_KEY=your-openai-api-key-here
   ```

## Usage

Run the application:
```bash
uv run python main.py
```

1. Type your question in the text box at the bottom
2. Click **Submit** to send your message to ChatGPT
3. The response will appear in the main text area
4. Click **Clear** to start a new conversation

## License

This project is licensed under the MIT License, see the LICENSE file for details.

## Troubleshooting

**Issue: "Please add your OpenAI API key"**
- Make sure you created a `.env` file with your API key

**Issue: Application won't start**
- Check that you ran `uv sync` to install all dependencies
- Verify Python 3.8+ is installed: `python --version`
