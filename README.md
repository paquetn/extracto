# extracto
File and folder structure extractor, outputs a json file.

## Installation

To clone the repository, run the following command:
```sh
git clone https://github.com/paquetn/extracto
```

To install the tool, run the following command in the root directory of the project:
```sh
pip install -e .
```


## Running the Tool

### Windows
1. Open Command Prompt:
   - Press `Win + R`, type `cmd`, and press `Enter`.

2. Run the tool:
   ```sh
   extracto
   ```

3. Alternatively, specify a different folder and output file:
   ```sh
   extracto path\to\folder path\to\output.json
   ```

### macOS/Linux
1. Open Terminal:
   - On macOS: Press `Cmd + Space`, type `Terminal`, and press `Enter`.
   - On Linux: Press `Ctrl + Alt + T` or open Terminal from Applications.

2. Run the tool:
   ```sh
   extracto
   ```

3. Alternatively, specify a different folder and output file:
   ```sh
   extracto /path/to/folder /path/to/output.json
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