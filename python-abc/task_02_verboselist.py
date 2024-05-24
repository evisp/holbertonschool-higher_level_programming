class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        item_count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{item_count}] items.")

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item