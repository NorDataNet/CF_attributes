# CF Attributes Processor

This repository contains a Python class `CF_Attributes` for managing Climate and Forecast (CF) convention metadata attributes from a CSV file, serving them in different python dictionaries in specific categories, such as global attributes, variable attributes, and others. It also combines these attributes into a unified dictionary for use if necessary.

## Features

- **File Parsing**: Reads and processes a CSV file containing CF attributes into Python dictionaries.
- **Attribute Categorisation**: Automatically categorises attributes into:
  - global attributes
  - coordinate variable attributes
  - data variable attributes
  - boundary variable attributes
  - geometry container variable attributes
  - quantization container variable attributes
  - all variable attributes
  - group Attributes

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the repository:
   ```bash
   cd <repository-folder>
   ```
3. Ensure Python 3.8 or higher is installed.


## Usage

1. Update the file path to the CSV file containing CF attributes in the `CF_Attributes` class:
   ```python
   self.file_path = '/path/to/cf_attributes.csv'
   ```

2. Initialise the `CF_Attributes` class:
    ```python
    from cf_attributes import CF_Attributes

    cf_attributes = CF_Attributes()
    ```

3. Access specific categories of attributes:
    ```python
    cf_attributes.global_attributes
    cf_attributes.variable_attributes
    cf_attributes.data_variable_attributes
    cf_attributes.boundary_variable_attributes
    cf_attributes.geometry_container_variable_attributes
    cf_attributes.quantization_container_variable_attributes
    cf_attributes.group_attributes
    ```

## CSV File

The CSV file is currently stored in this repository. However, if and when the CF conventions host this as a standalone CSV file, I will write something to use that as the source.

## Keys

Each attribute has the following keys:

- **Attribute**: The name of the attribute
- **Type**: The type of the attribute:
  - `S`: String
  - `N`: Numeric
- **Use**: A comma-separated list indicating where the attribute is used:
  - `G`: Global attributes
  - `C`: Coordinate variables
  - `D`: Data variables
  - `BI`: Boundary variables
  - `M`: Geometry container variables
  - `Q`: Quantization container variables
  - `Gr`: Group attributes
- **Description**: A brief explanation of the attribute.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Push to your branch and create a pull request.

## Acknowledgements

- Climate and Forecast (CF) conventions for providing guidance on metadata standards. https://cfconventions.org/
