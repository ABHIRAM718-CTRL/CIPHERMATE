# CIPHERMATE

CIPHERMATE is a small utility project that mixes cryptography tools with GitHub automation features.

It includes:
- Python-based cipher tools for encoding and encryption
- JavaScript/Node.js support for GitHub repo operations using the GitHub API
- Secure token handling and automatic refresh logic for GitHub authentication

## What it does

### Cryptography Module
- `CIPHERCODE.py` contains encoding and encryption tools
- Supports Morse code conversion for letters, numbers, and spaces
- Uses AES encryption with the `cryptography` library
- Generates secure random keys using `os.urandom(16)`

### GitHub Integration Module
- Intended to support `create_repo.js` for repository creation and management
- Uses the GitHub REST API client (`@octokit/rest`)
- Works with Replit-style connector authentication and OAuth token handling
- Refreshes tokens automatically and recreates GitHub clients for each operation

## Why it exists

The project separates concerns cleanly:
- Python handles cryptography
- JavaScript handles GitHub automation
- Each module can be tested and maintained independently

Security goals:
- fresh GitHub clients per operation
- secure random key generation
- token expiration checks before use

## Requirements

### Python
- Python 3.11 or later
- `cryptography` library

Install Python dependencies with:

```bash
pip install cryptography
```

### Node.js (optional)
If you add GitHub automation files such as `create_repo.js`:
- `@octokit/rest`
- Replit connector support for OAuth tokens

## How to use

### Python cryptography
Run `CIPHERCODE.py` from the project root. It is the main script for encoding and AES encryption utilities.

### GitHub automation
If you use the GitHub module, make sure your environment and Replit connector tokens are set up before running the JavaScript script.

## Files

- `CIPHERCODE.py` — Python cryptography and encoding utilities
- `pyproject.toml` — Python package metadata and dependencies
- `replit.md` — project overview and architecture notes

## Notes

This project is designed to work in a Replit-like environment, especially for the GitHub authentication side.

For the best security, keep your GitHub tokens and any secret keys out of source control.
