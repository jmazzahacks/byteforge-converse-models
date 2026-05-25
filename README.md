# byteforge-converse-models

Shared data models for ByteforgeConverse — conversations, messages, turns, and sessions.

This library has no internal dependencies and is consumed by `byteforge-converse-core`, `byteforge-converse-backend`, and `byteforge-converse-api-python`.

## Installation

This is a public repo — no token required.

```bash
pip install git+https://github.com/jmazzahacks/byteforge-converse-models.git
```

### As a dependency in pyproject.toml
```toml
dependencies = [
    "byteforge-converse-models @ git+https://github.com/jmazzahacks/byteforge-converse-models.git",
]
```

### As a dependency in requirements.txt
```
byteforge-converse-models @ git+https://github.com/jmazzahacks/byteforge-converse-models.git
```

## Usage

```python
import byteforge_converse_models

# Add usage examples here
```

## Development

### Setup

```bash
# Create virtual environment
python -m venv .

# Activate virtual environment
source bin/activate  # On Windows: bin\Scripts\activate

# Install dependencies
pip install -r dev-requirements.txt
pip install -e .
```

## License

O'Saasy License — see [LICENSE](LICENSE). Reserves commercial SaaS rights for the copyright holder. See https://osaasy.dev/ for details.

## Author

Jason Byteforge ([@jmazzahacks](https://github.com/jmazzahacks)) — jason@reallybadapps.com
