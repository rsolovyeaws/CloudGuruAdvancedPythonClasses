class CallTracker:
    def __init__(self, func):
        self.func = func
        self.times_called = 0
        self.call_args = []
        
    def track_call(self, *args, **kwargs):
        self.times_called += 1
        self.call_args.append((args, kwargs))
    
    def __call__(self, *args, **kwargs):
        self.track_call(*args, **kwargs)
        return self.func(*args, **kwargs)
    
@CallTracker
def add(a, b):
    return a + b

print(add(1, 2))
print(add(2, b=3))
print(f"Times called: {add.times_called}")
print(f"Called args: {add.call_args}")