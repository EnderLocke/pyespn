import re


def camel_to_snake(name):
    """Convert camelCase or PascalCase to snake_case."""
    name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
    return name
