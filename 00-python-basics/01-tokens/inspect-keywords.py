import keyword
import tokenize
import io

# 1. Dynamically check if a string is a reserved keyword
print(f"Is 'def' a keyword? {keyword.iskeyword('def')}")
print(f"Is 'True' a keyword? {keyword.iskeyword('True')}")
print(f"Is 'true' a keyword? {keyword.iskeyword('true')}") # False - Python is case-sensitive!

# 2. Let's look at how the CPython Tokenizer sees a line of code
code = "if True:\n    pass"

# We feed a byte-stream into the tokenizer (mimicking what CPython does when reading a file)
tokens = tokenize.tokenize(io.BytesIO(code.encode('utf-8')).readline)

for t in tokens:
    if t.type in (tokenize.NAME, tokenize.OP, tokenize.INDENT):
        print(f"Token Type: {tokenize.tok_name[t.type]:<10} | Value: '{t.string}'")
