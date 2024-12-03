# Folder Structure Extractor

File and folder structure extractor, outputs a JSON file.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Tool Without Installation](#running-the-tool-without-installation)
  - [Windows](#windows)
  - [macOS/Linux](#macoslinux)
- [Additional Notes](#additional-notes)

## Prerequisites

- Python 3.6 or higher
- `pip` (Python package installer)
- `pipx` (https://github.com/pypa/pipx)
- Cloning the repository
```sh
git clone https://github.com/paquetn/extracto
```

## Installation

To install the tool, run the following command in the root directory of the project:
```sh
pipx install .
```

## Running the Tool Without Installation

You can run the tool directly without installing it by using `python` or `python3`:

### Windows
1. Open Command Prompt:
   - Press `Win + R`, type `cmd`, and press `Enter`.

2. Navigate to the root directory of the project:
   ```sh
   cd path\to\extracto
   ```

3. Run the tool:
   ```sh
   python -m extracto
   ```

4. Alternatively, specify a different folder and output file:
   ```sh
   python -m extracto path\to\folder path\to\output.json
   ```

### macOS/Linux
1. Open Terminal:
   - On macOS: Press `Cmd + Space`, type `Terminal`, and press `Enter`.
   - On Linux: Press `Ctrl + Alt + T` or open Terminal from Applications.

2. Navigate to the root directory of the project:
   ```sh
   cd /path/to/extracto
   ```

3. Run the tool:
   ```sh
   python -m extracto
   ```

4. Alternatively, specify a different folder and output file:
   ```sh
   python -m extracto /path/to/folder /path/to/output.json
   ```

## Additional Notes
- If you specify a directory using the `folder_path` argument, the tool will analyze that directory.
- Use the `output_path` argument to specify the output JSON file.
- Use the `--config` option to specify a custom configuration file (default: `config.json` in the script directory).

### Example Commands
- Analyze the current directory and save the structure to `output.json`:
  ```sh
  extracto
  ```

- Analyze a specific directory and save the structure to a specified file:
  ```sh
  extracto /path/to/project /path/to/output.json
  ```

- Use a custom configuration file:
  ```sh
  extracto /path/to/project /path/to/output.json --config /path/to/config.json
  ```

Feel free to distribute this tool across multiple systems for quick folder analysis!