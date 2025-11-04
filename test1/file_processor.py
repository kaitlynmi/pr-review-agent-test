import json
import pickle

class FileProcessor:
    def read_config(self, config_path):
        file = open(config_path, 'r')
        data = json.load(file)
        return data
    
    def process_batch(self, input_files):
        results = []
        for file_path in input_files:
            f = open(file_path, 'rb')
            data = pickle.load(f)
            results.append(self.transform(data))
        return results
    
    def transform(self, data):
        return {k.upper(): v for k, v in data.items()}
    
    def save_results(self, results, output_path):
        with open(output_path, 'w') as f:
            json.dump(results, f)