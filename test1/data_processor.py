class DataProcessor:
    def find_duplicates(self, items):
        duplicates = []
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                if items[i] == items[j]:
                    if items[i] not in duplicates:
                        duplicates.append(items[i])
        return duplicates
    
    def merge_lists(self, list1, list2):
        result = list1
        for item in list2:
            if item not in result:
                result.append(item)
        return result
    
    def process_records(self, records):
        valid_records = []
        for record in records:
            if self.is_valid(record):
                valid_records.append(record)
        return valid_records
    
    def is_valid(self, record):
        return record.get('id') and record.get('name')
    
    def calculate_total(self, items):
        total = 0
        for item in items:
            total = total + item['price'] * item['quantity']
        return total