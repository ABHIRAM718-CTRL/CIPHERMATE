# Overview

This is a cryptography and automation utility project that combines multiple encoding/encryption capabilities with GitHub repository management functionality. The system includes cipher tools (AES encryption, Morse code conversion) implemented in Python, and GitHub API integration using JavaScript/Node.js for automated repository operations.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Core Components

### Cryptography Module (Python)
- **CIPHERCODE.py**: Implements multiple encoding and encryption algorithms
- **Morse Code Dictionary**: Complete mapping for alphabetic, numeric, and space characters
- **AES Encryption**: Uses the `cryptography` library with AES algorithm in ECB mode
- **Key Generation**: Utilizes `os.urandom(16)` for secure 16-byte key generation

### GitHub Integration Module (JavaScript)
- **create_repo.js**: Handles GitHub repository creation and management
- **Authentication**: Uses Replit's connector system for GitHub OAuth token management
- **Token Refresh**: Implements automatic token expiration checking and renewal
- **API Client**: Leverages the Octokit REST API client for GitHub operations

## Authentication Architecture

### Replit Connector Integration
- **Token Management**: Integrates with Replit's connector system for secure GitHub authentication
- **Environment Variables**: Uses `REPL_IDENTITY` and `WEB_REPL_RENEWAL` for different deployment contexts
- **Dynamic Token Refresh**: Automatically handles token expiration and renewal
- **Security Pattern**: Never caches GitHub clients to ensure fresh tokens on each operation

## Design Patterns

### Security-First Approach
- **Fresh Client Generation**: GitHub clients are recreated for each operation to prevent stale token usage
- **Secure Key Generation**: Uses cryptographically secure random number generation
- **Token Validation**: Includes expiration checking before token usage

### Modular Design
- **Separation of Concerns**: Cryptography functions isolated from GitHub operations
- **Language Specialization**: Python for cryptographic operations, JavaScript for API integrations
- **Reusable Components**: Modular functions that can be independently tested and maintained

# External Dependencies

## JavaScript/Node.js Dependencies
- **@octokit/rest**: GitHub REST API client library for repository operations
- **Replit Connectors API**: Authentication service for managing GitHub OAuth tokens

## Python Dependencies
- **cryptography**: Industry-standard cryptographic library for AES encryption operations
- **os**: Built-in Python module for secure random number generation
- **base64**: Standard library for encoding operations
- **time**: Standard library for timing operations

## Platform Dependencies
- **Replit Environment**: Relies on Replit's connector system and environment variables
- **GitHub API**: Integrates with GitHub's REST API for repository management
- **OAuth Integration**: Uses GitHub's OAuth system through Replit's connector infrastructure