class non_standard_entries(Exception):
    def __init__(self):
        self.message = "NON-STANDARD ENTRIES"


class OperationsModel:
    def __init__(self, items: list):
        try:
            entries = []
            for i in range(1, len(items)):
                entries.append(items[i])

            self.operation = int(items[0])
            self.entries = entries
            if self.operation == 1 and len(entries) == 2:
                return
            if self.operation == 2 and len(entries) == 2:
                return
            if self.operation == 3 and len(entries) == 3:
                return
            raise non_standard_entries()
        except non_standard_entries as e:
            print(f"ERROR: {e.message}")

    def print(self):
        print(f"operação: {self.operation}")
        print(f"entradas: {self.entries}")

