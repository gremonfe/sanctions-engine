# Sanctions Validator App

The Sanctions Validator App is a Python application that validates entries in an Excel file against various sanction lists. It helps users identify potential matches between the entries in the Excel file and the sanctioned entities listed in different XML files.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Project Overview](#project-overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites
Before running the Sanctions Validator, ensure that you have the following prerequisites installed:

- Python (version 3.6 or above)
- pip (Python package installer)
## Project Overview

The Sanctions Validator App is designed to streamline the process of validating entries in an Excel file against multiple sanction lists. It fetches the latest XML files containing the sanction data, reads the Excel file, and performs the validation to identify potential matches.

## Features

- Fetches XML files containing sanction lists from multiple sources
- Reads entries from an Excel file for validation
- Matches the entries against the sanction lists
- Provides feedback on potential matches
- User-friendly graphical user interface (GUI)

## Getting Started

To get started with the Sanctions Validator App, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/sanctions-validator-app.git`
2. Navigate to the project directory: `cd sanctions-validator-app`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Configure the config.json file by providing the URLs of the sanctions lists in XML format that you want to use for validation. Open the config.json file in a text editor and replace the sample URLs with the actual URLs. The file should be in the following format:
```json
{
  "Source1": "https://example.com/sanctions_list1.xml",
  "Source2": "https://example.com/sanctions_list2.xml",
  ...
}
```
Add as many sources and URLs as needed, ensuring that each URL points to a valid XML file.
5. Save the `config.json` file.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the project directory:
```shell
cd sanctions-validator
```
3. Launch the application: `python sanctions_validator.py`
4. The application will display a GUI window.
5. Click the "Browse" button to select an Excel file for validation.
6. Click the "Validate" button to start the validation process.
7. Click the "Validate" button to perform the validation.The application will compare the names in the Excel file with the entries in the configured sanctions lists. Any matches found will be displayed in the log area.
8. Review the log area to see the validation results.
9. Repeat the process for different Excel files or make changes to the configuration as needed.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

Feel free to modify this README.md file as needed, adding sections specific to your project or providing additional information relevant to your users.
