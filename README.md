# logger4dec

[![PyPI version](https://badge.fury.io/py/logger4dec.svg)](https://badge.fury.io/py/logger4dec)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![GitHub](https://img.shields.io/badge/github-ifuckingjoke%2Flogger4dec-blue)](https://github.com/ifuckingjoke/logger4dec)

A lightweight, decorator-based logger for colorful terminal output in Python.

## 📋 Overview

`logger4dec` is a Python logging utility that makes it easy to add logging to your functions using decorators. It provides colorful, readable terminal output with ANSI color codes to help you debug and monitor your applications.

## ✨ Features

- **Decorator-based**: Use the `Logger` class to create decorators with custom colors
- **Colorful output**: Beautiful ANSI color-coded log messages for better readability
- **Lightweight**: Minimal dependencies, fast performance
- **Flexible**: Support for foreground colors, text styles, and background colors
- **Easy to use**: Simple API with keyword-only arguments

## 🚀 Installation

Install from PyPI (recommended):

```bash
pip install logger4dec
```

Or clone and install from source:

```bash
git clone https://github.com/ifuckingjoke/logger4dec.git
cd logger4dec
pip install -e .
```

## 📖 Usage

### Basic Usage

First, create a `Logger` instance and use it to decorate your functions:

```python
from logger4dec import Logger

# Create a logger instance
logger = Logger()

# Use it as a decorator with the log method
@logger.log("Function started")
def my_function(x, y):
    result = x + y
    return result

my_function(5, 3)
# Output: Function started
# Then the function executes normally
```

### With Colors

Customize the output with ANSI color codes. Use `foreground`, `style`, and `background` parameters:

```python
from logger4dec import Logger

# Green text (foreground=32), bold style (style=1)
logger = Logger(foreground=32, style=1)

@logger.log("Processing data...")
def process_data(data):
    return data * 2

process_data([1, 2, 3])
```

### Color Codes Reference

#### Foreground Colors
- `30` - Black
- `31` - Red
- `32` - Green
- `33` - Yellow
- `34` - Blue
- `35` - Magenta
- `36` - Cyan
- `37` - White

#### Text Styles
- `0` - Normal
- `1` - Bold
- `2` - Dim
- `3` - Italic
- `4` - Underline

#### Background Colors
- `40` - Black
- `41` - Red
- `42` - Green
- `43` - Yellow
- `44` - Blue
- `45` - Magenta
- `46` - Cyan
- `47` - White

### Advanced Examples

```python
from logger4dec import Logger

# Red bold text with yellow background
error_logger = Logger(foreground=31, style=1, background=43)

@error_logger.log("ERROR: Something went wrong!")
def critical_operation():
    pass

# Blue underlined text
info_logger = Logger(foreground=34, style=4)

@info_logger.log("INFO: Starting process...")
def start_process():
    pass

critical_operation()
start_process()
```

## 🎨 How It Works

The `Logger` class uses ANSI escape codes to colorize terminal output. The format is:
```
\033[{style};{foreground};{background}m{text}\033[0m
```

Where:
- `\033[` - Escape sequence start
- `{style}` - Text style (bold, dim, italic, etc.)
- `{foreground}` - Text color
- `{background}` - Background color
- `m` - Command terminator
- `{text}` - Your log message
- `\033[0m` - Reset all formatting

## 📝 API Reference

### Logger Class

```python
class Logger:
    def __init__(self, *, foreground=0, style=0, background=0):
        """
        Initialize a Logger instance.
        
        Args:
            foreground (int): ANSI foreground color code (default: 0)
            style (int): ANSI text style code (default: 0)
            background (int): ANSI background color code (default: 0)
        """
    
    def log(self, text: str) -> Callable:
        """
        Create a decorator that logs a message before executing the function.
        
        Args:
            text (str): The message to log
            
        Returns:
            Callable: A decorator that logs the text and executes the function
        """
```

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the GNU General Public License v3.0 - see the LICENSE file for details.

## 🙋 Support

If you have questions or issues, please open an issue on the [GitHub repository](https://github.com/ifuckingjoke/logger4dec/issues).

## 🔗 Links

- [Repository](https://github.com/ifuckingjoke/logger4dec)
- [PyPI Package](https://pypi.org/project/logger4dec/)
- [Issues](https://github.com/ifuckingjoke/logger4dec/issues)
- [Discussions](https://github.com/ifuckingjoke/logger4dec/discussions)

---

<div align="center">
Made with ❤️ by ifuckingjoke
</div>
<div align="center">
ifuckingjoke@proton.me
</div>
