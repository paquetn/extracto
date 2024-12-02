
# Folder Structure Extractor

## Running the Tool

### Windows
1. Open Command Prompt:
   - Press `Win + R`, type `cmd`, and press `Enter`.

2. Navigate to the folder containing the tool:
   ```bash
   cd path\to\executable
   ```

   Example:
   ```bash
   cd C:\Users\YourName\Desktop
   ```

3. Run the executable:
   ```bash
   extract_structure.exe
   ```

4. Alternatively, run the executable directly by specifying its full path:
   ```bash
   C:\Users\YourName\Desktop\extract_structure.exe
   ```

### macOS/Linux
1. Open Terminal:
   - On macOS: Press `Cmd + Space`, type `Terminal`, and press `Enter`.
   - On Linux: Press `Ctrl + Alt + T` or open Terminal from Applications.

2. Navigate to the folder containing the tool:
   ```bash
   cd /path/to/executable
   ```

   Example:
   ```bash
   cd ~/Desktop
   ```

3. Make the file executable (if necessary):
   ```bash
   chmod +x extract_structure
   ```

4. Run the executable:
   ```bash
   ./extract_structure
   ```

5. Alternatively, run it directly using its full path:
   ```bash
   /Users/YourName/Desktop/extract_structure
   ```

---

## Additional Notes
- If you specify a directory using the `path` argument, the tool will analyze that directory.
- Use the `-o` or `--output` option to save the folder structure as a JSON file.
- Example command:
  ```bash
  ./extract_structure /path/to/project -o output.json
  ```

Feel free to distribute this tool across multiple systems for quick folder analysis!
