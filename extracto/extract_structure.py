import os
import json
import argparse


def load_config(config_path: str) -> dict:
    """
    Loads the configuration from a JSON file.
    Args:
        config_path (str): Path to the JSON config file.
    Returns:
        dict: Configuration dictionary.
    """
    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Config file '{config_path}' not found.")
        exit(1)
    except json.JSONDecodeError:
        print(f"Error: Config file '{config_path}' is not a valid JSON.")
        exit(1)


def extract_folder_structure(folder_path: str, excluded_folders: list) -> dict:
    """
    Extracts the folder structure from the selected folder onward and filters out specified folders.
    Args:
        folder_path (str): The path to the folder whose structure is to be extracted.
        excluded_folders (list): List of folder names to exclude from the structure.
    Returns:
        dict: The folder structure as a dictionary.
    """
    folder_structure = {}
    for root, dirs, files in os.walk(folder_path):
        # Remove excluded folders from the traversal
        dirs[:] = [d for d in dirs if d not in excluded_folders]
        # Build the nested folder structure
        relative_path = os.path.relpath(root, folder_path)
        current_folder = folder_structure
        if relative_path != ".":
            for part in relative_path.split(os.sep):
                current_folder = current_folder.setdefault(part, {})
        for file in files:
            current_folder[file] = None
    return folder_structure


def save_structure_to_json(folder_structure: dict, output_path: str):
    """
    Saves the folder structure to a JSON file.
    Args:
        folder_structure (dict): The folder structure to be saved.
        output_path (str): The path to the output JSON file.
    """
    try:
        with open(output_path, "w") as f:
            json.dump(folder_structure, f, indent=4)
    except PermissionError:
        print(f"Permission denied: Unable to write to {output_path}.")
        exit(1)
    except Exception as e:
        print(f"An unexpected error occurred while saving the file: {e}")
        exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Extracts the structure of a folder and saves it to a JSON file, excluding specified folders."
    )
    parser.add_argument(
        "folder_path",
        type=str,
        nargs="?",
        default=os.getcwd(),
        help="The path to the folder whose structure is to be extracted (default: current working directory).",
    )
    parser.add_argument(
        "output_path",
        type=str,
        nargs="?",
        default=os.path.join(os.getcwd(), "output.json"),
        help="The path to the output JSON file (default: output.json in the current working directory).",
    )
    parser.add_argument(
        "--config",
        type=str,
        default=os.path.join(os.path.dirname(__file__), "config.json"),
        help="Path to the JSON configuration file (default: config.json in the script directory).",
    )
    args = parser.parse_args()

    # Load excluded folders from config
    config = load_config(args.config)
    excluded_folders = config.get("excluded_folders", [])

    print(f"Extracting folder structure from: {args.folder_path}")
    print(f"Excluding folders: {', '.join(excluded_folders)}")
    folder_structure = extract_folder_structure(args.folder_path, excluded_folders)
    print(f"Saving folder structure to: {args.output_path}")
    save_structure_to_json(folder_structure, args.output_path)


if __name__ == "__main__":
    main()
