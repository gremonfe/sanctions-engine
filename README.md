# Sanctions Validator App

The Sanctions Validator App is a Python application that validates entries in an Excel file against various sanction lists. It helps users identify potential matches between the entries in the Excel file and the sanctioned entities listed in different XML files.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The Sanctions Validator App is designed to streamline the process of validating entries in an Excel file against multiple sanction lists, including the United Nations (UN) consolidated list. It fetches the latest XML files containing the sanction data, reads the Excel file, and performs the validation to identify potential matches.

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

## Usage

1. Launch the application: `python sanctions_validator_app.py`
2. Select the Excel file containing the entries to be validated.
3. Click the "Validate" button to perform the validation.
4. View the results, which will indicate potential matches between the entries and the sanction lists.

## Contributing

Contributions to the Sanctions Validator App are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request. For major changes, it is recommended to discuss them first by opening an issue to ensure they align with the project's goals.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

Feel free to modify this README.md file as needed, adding sections specific to your project or providing additional information relevant to your users.
