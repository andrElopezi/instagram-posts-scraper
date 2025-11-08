thonimport json

class Exporter:
    def __init__(self, data):
        self.data = data

    def export_to_json(self, output_file):
        with open(output_file, 'w') as f:
            json.dump(self.data, f, indent=4)