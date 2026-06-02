# logger4dec

A lightweight, decorator-based logger for colorful terminal output in Python.

## 📋 Overview

`logger4dec` is a Python logging utility that makes it easy to add logging to your functions using decorators. It provides colorful, readable terminal output to help you debug and monitor your applications.

## ✨ Features

- **Decorator-based**: Simple `@logger` decorator for easy integration
- **Colorful output**: Beautiful, color-coded log messages for better readability
- **Lightweight**: Minimal dependencies, fast performance
- **Easy to use**: Works with minimal configuration
- **Flexible**: Support for various log levels and custom formatting

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/ifuckingjoke/logger4dec.git
cd logger4dec
```

Or install with pip (if published):

```bash
pip install logger4dec
```

## 📖 Usage

### Basic Usage

```python
from logger4dec import logger

@logger
def my_function(x, y):
    result = x + y
    return result

my_function(5, 3)
```

### With Log Levels

```python
from logger4dec import logger

@logger(level="info")
def process_data(data):
    # Your code here
    return processed_data

@logger(level="debug")
def debug_mode():
    # Detailed debugging information
    pass
```

### Customization

```python
from logger4dec import logger

@logger(name="MyLogger", level="warning")
def important_operation():
    # Your code here
    pass
```

## 🎨 Log Levels

- **INFO**: General information messages
- **DEBUG**: Detailed debugging information
- **WARNING**: Warning messages
- **ERROR**: Error messages
- **CRITICAL**: Critical errors

## 📝 Configuration

Configure logger behavior through decorator parameters:

- `name`: Custom logger name (default: function name)
- `level`: Log level (`debug`, `info`, `warning`, `error`, `critical`)
- `colorize`: Enable/disable colored output (default: `True`)

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
- [Issues](https://github.com/ifuckingjoke/logger4dec/issues)
- [Discussions](https://github.com/ifuckingjoke/logger4dec/discussions)

---
<div align="center">
Made with ❤️ by [ifuckingjoke](https://github.com/ifuckingjoke)
</div>
<div align="center">
ifuckingjoke@proton.me
</div>
