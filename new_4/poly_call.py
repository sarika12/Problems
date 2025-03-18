class Greeting:
    @staticmethod
    def say_hello():
        return "name"
    @classmethod
    def call_hello(cls):
        return f"class hello{cls.__name__}"

print(Greeting.say_hello())
print(Greeting.call_hello())
