# QA Email AI

QA Email AI is a virtual assistant designed to automate the process of responding to customer emails for a company. The AI is trained using company-specific data stored on Notion, leveraging its API to retrieve and process information. The more data collaborators provide in the Notion database, the more personalized and accurate the AI responses become.

## Features

- Automatically retrieves customer emails from an inbox.
- Responds to emails based on company data stored in Notion.
- Utilizes AI-powered natural language processing for personalized email responses.
- Exports company knowledge from Notion into a CSV file for enhanced response accuracy.

## Prerequisites

- Python 3.10 or higher
- Notion API Token and Database ID
- An email account with IMAP and SMTP access
- Virtual environment: Poetry

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/dudaborges/qa-email-ai.git
   cd qa-email-ai
   ```

2. Install dependencies:
   ```bash
   poetry install
   ```

3. Set up environment variables:
   Create a `.env` file in the root directory with the following variables:
   ```env
   OPENAI_API_KEY=your_api_key
   EMAIL_USERNAME=your_email@example.com
   EMAIL_PASSWORD=your_email_password
   NOTION_TOKEN=your_notion_api_token
   DATABASE_ID=your_notion_database_id
   ```

4. (Optional) If you're contributing to development, also install dev dependencies:
   ```bash
   poetry install --with dev
   ```

## Usage

1. Start the script to process and respond to emails:
   ```bash
   poetry run python main.py
   ```

2. The script will:
   - Fetch emails from the inbox.
   - Query Notion for relevant company data.
   - Generate a response using AI.
   - Send personalized replies to the customers.

## Dependencies

The project dependencies are managed with Poetry and are listed in the `pyproject.toml` file. Major dependencies include:

- `langchain` and `langchain-openai` for AI integration.
- `faiss-cpu` for similarity searches.
- `notion-client` for interacting with the Notion API.
- `streamlit` for potential UI development.
- `imbox` for email handling.

## Development

The project uses `isort` and `blue` for code formatting. To lint and format the code, run:
```bash
poetry run task lint
```

## Contribution

Feel free to fork the repository and submit pull requests. Ensure all new features are properly documented and tested before submission.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
Created by [Maria Eduarda Borges](mailto:duda.pborges92@gmail.com)
