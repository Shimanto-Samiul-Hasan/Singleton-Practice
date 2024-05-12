# Singleton Practice

This repository contains an example implementation of the Singleton pattern in Python for practicing purposes.

## Logger Class

The `Logger` class is designed to encapsulate logging functionality in Python.

### Overview

This class implements the Singleton pattern, ensuring that only one instance of the logger is created throughout the runtime of the program. It provides methods to log messages at different severity levels: INFO, WARNING, ERROR, FATAL, and DEBUG.

### Attributes

- `_instance`: A class attribute that holds the singleton instance of the logger.

### Methods

#### `__new__()`
- Overrides the `__new__()` method to implement the Singleton pattern.
- Creates a new instance of the class if `_instance` is `None`.
- Configures the logger with a file handler for logging to `log.txt`.

#### `log(level, message)`
- Logs messages at different levels based on the specified `level` parameter.
- Parameters:
  - `level` (str): The severity level of the message (INFO, WARNING, ERROR, FATAL, DEBUG).
  - `message` (str): The message to be logged.

### Usage

In the main block of your Python script, create an instance of the `Logger` class and use the `log()` method to log messages at different severity levels.

Example:
```python
if __name__ == '__main__':
    logger = Logger()
    logger.log('INFO', 'This is an info message')
    logger.log('WARNING', 'This is a warning message')
    logger.log('ERROR', 'This is an error message')
    logger.log('FATAL', 'This is a fatal message')
```

### Dependencies

- `logging`: The built-in logging module in Python.
