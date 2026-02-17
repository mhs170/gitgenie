# GitGenie 🧞‍♂️

AI-powered CLI tool that generates commit messages and PR descriptions using local LLMs.

## Features

- 🎯 **Smart Commit Messages** - Analyzes staged changes and generates conventional commit messages
- 📝 **PR Descriptions** - Creates comprehensive PR descriptions from commit history
- 🔄 **Regenerate Option** - Don't like the suggestion? Regenerate with one keystroke
- 🤖 **Local AI** - Uses Ollama for private, offline AI generation
- ⚡ **Streaming Output** - See AI responses generate in real-time

## Demo
```bash
$ git add .
$ gitgenie commit

Generating commit message...
feat(auth): add JWT token validation and refresh mechanism

[c]ommit, [r]egenerate, [q]uit: c
✓ Committed successfully!
```

## Prerequisites

1. **Python 3.9+**
2. **Ollama** - [Install from ollama.com](https://ollama.com)
3. **llama3 model**

### Install Ollama and llama3
```bash
# Install Ollama (macOS)
brew install ollama

# Or download from https://ollama.com

# Start Ollama
ollama serve

# Pull the llama3 model (in a new terminal)
ollama pull llama3
```

## Installation
```bash
# Clone the repository
git clone https://github.com/mhs170/gitgenie.git
cd gitgenie

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the package
pip install -e .
```

## Usage

### Generate Commit Messages
```bash
# Stage your changes
git add .

# Generate a commit message
gitgenie commit

# Options:
# [c] - Commit with the generated message
# [r] - Regenerate a new message
# [q] - Cancel and quit
```

### Generate PR Descriptions
```bash
# Generate PR description (compares against main)
gitgenie pr

# Compare against a different branch
gitgenie pr master
```

## How It Works

1. **Commit Messages**: GitGenie reads your staged git diff, sends it to llama3, and generates a conventional commit message following best practices
2. **PR Descriptions**: GitGenie analyzes your commit history between branches and creates a structured PR description with overview, changes, and testing notes

## Configuration

GitGenie uses Ollama running locally on `localhost:11434`. Make sure Ollama is running before using GitGenie:
```bash
# Check if Ollama is running
ollama list

# Start Ollama if needed
ollama serve
```

## Commit Message Format

GitGenie follows [Conventional Commits](https://www.conventionalcommits.org/):
```
type(scope): description

Examples:
feat(auth): add user login
fix(api): resolve timeout issue
docs(readme): update installation steps
```

## PR Description Format

Generated PR descriptions include:
- **Title**: Brief summary
- **Overview**: What and why
- **Changes**: Bullet-pointed key changes
- **Testing**: How to test the changes

## Troubleshooting

**Error: "Ollama might not be running"**
```bash
# Start Ollama
ollama serve
```

**Error: "Model not found"**
```bash
# Pull the llama3 model
ollama pull llama3
```

**Error: "Not a git repository"**
- Make sure you're inside a git repository
- Run `git init` if needed

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

MIT

## Author

Mohammed Salama - [GitHub](https://github.com/mhs170)
