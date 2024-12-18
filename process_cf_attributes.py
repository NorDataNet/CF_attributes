import csv
from pathlib import Path

class CF_Attributes:

    def __init__(self):
        script_dir = Path(__file__).parent
        self.file_path = script_dir / 'cf_attributes.csv'
        self._to_dict()
        self._global_attributes()
        self._coordinate_variable_attributes()
        self._data_variable_attributes()
        self._boundary_variable_attributes()
        self._geometry_container_variable_attributes()
        self._quantization_container_variable_attributes()
        self._group_attributes
        self._variable_attributes()

    def _to_dict(self):
        # Dictionary to store the result
        self.all_attributes = {}

        # Read the CSV file and process
        with open(self.file_path, "r") as file:
            reader = csv.DictReader(file, delimiter="|")
            for row in reader:
                # Clean the Attribute column
                attribute = row["Attribute"].strip("**`")
                # Add to dictionary, removing unwanted characters
                self.all_attributes[attribute] = {
                    "Type": row["Type"].strip(),
                    "Use": row["Use"].strip().split(', '),
                    "Description": row["Description"].strip()
                }

    def _coordinate_variable_attributes(self):
        self.coordinate_variable_attributes = {}
        for key, val in self.all_attributes.items():
            if 'C' in self.all_attributes[key]['Use']:
                self.coordinate_variable_attributes[key] = val

    def _data_variable_attributes(self):
        self.data_variable_attributes = {}
        for key, val in self.all_attributes.items():
            if 'D' in self.all_attributes[key]['Use']:
                self.data_variable_attributes[key] = val

    def _global_attributes(self):
        self.global_attributes = {}
        for key, val in self.all_attributes.items():
            if 'G' in self.all_attributes[key]['Use']:
                self.global_attributes[key] = val

    def _group_attributes(self):
        self.group_attributes = {}
        for key, val in self.all_attributes.items():
            if 'Gr' in self.all_attributes[key]['Use']:
                self.group_attributes[key] = val

    def _geometry_container_variable_attributes(self):
        self.geometry_container_variable_attributes = {}
        for key, val in self.all_attributes.items():
            if 'M' in self.all_attributes[key]['Use']:
                self.geometry_container_variable_attributes[key] = val

    def _boundary_variable_attributes(self):
        self.boundary_variable_attributes = {}
        for key, val in self.all_attributes.items():
            if 'BI' in self.all_attributes[key]['Use'] or 'BI' in self.all_attributes[key]['Use']:
                self.boundary_variable_attributes[key] = val

    def _quantization_container_variable_attributes(self):
        self.quantization_container_variable_attributes = {}
        for key, val in self.all_attributes.items():
            if 'Q' in self.all_attributes[key]['Use']:
                self.quantization_container_variable_attributes[key] = val

    def _variable_attributes(self):
        # Combine all variable-related dictionaries
        self.variable_attributes = {}
        variable_dictionaries = [
            self.coordinate_variable_attributes,
            self.data_variable_attributes,
            self.boundary_variable_attributes,
            self.geometry_container_variable_attributes,
            self.quantization_container_variable_attributes
        ]

        for var_dict in variable_dictionaries:
            for key, value in var_dict.items():
                if key not in self.variable_attributes:
                    self.variable_attributes[key] = value

def main():
    # Create an instance of CF_Attributes
    cf_attributes = CF_Attributes()
    # Call the display method
    cf_attributes.display_global_attributes()

if __name__ == "__main__":
    main()
