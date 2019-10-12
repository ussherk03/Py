
## Create a class that behaves like an iterator and an iterable. ##
class Domain:

    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return  current

nums = Domain(1, 10)

print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
## Create an iterator of a list. ##