from typing import Final

# The VM doesn't care, but Pylance/Pyright will throw a static error if you reassign this
MAX_CONNECTIONS: Final = 100 

# CPython executes this at runtime without crashing, but your IDE will flag it as an error
MAX_CONNECTIONS = 200