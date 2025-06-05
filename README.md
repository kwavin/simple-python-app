simple-python-app

# Simple Python Calculator

A basic calculator application to demonstrate Jenkins CI/CD pipeline functionality.

## Features

- Basic arithmetic operations (add, subtract, multiply, divide)
- Power calculations
- Error handling for division by zero
- Comprehensive unit tests

## Files

- `main.py` - Main calculator application
- `test_calculator.py` - Unit tests
- `requirements.txt` - Python dependencies
- `README.md` - This file

## Usage

### Run the Application

```bash
python3 main.py
```

### Run Tests

```bash
# Using unittest (built-in)
python3 -m unittest test_calculator.py -v

# Or using pytest (if installed)
python3 -m pytest test_calculator.py -v
```

### Install Dependencies

```bash
pip3 install -r requirements.txt
```

## Sample Output

```
Welcome to the Simple Calculator!
========================================
Addition: 10 + 5 = 15
Subtraction: 10 - 3 = 7
Multiplication: 4 * 7 = 28
Division: 15 / 3 = 5.0
Power: 2^3 = 8
========================================
Calculator demo completed successfully!
```

## Jenkins Pipeline

This project is designed to work with a Jenkins CI/CD pipeline that will:

1. **Checkout** - Pull code from GitHub
2. **Setup** - Install Python dependencies
3. **Test** - Run unit tests with coverage
4. **Quality Check** - Run flake8 linting
5. **Build** - Package the application
6. **Deploy** - Deploy to target environment

## Testing the Pipeline

The application includes:
- ✅ Multiple test cases (12 tests total)
- ✅ Edge case testing
- ✅ Error condition testing
- ✅ Clean, readable code that passes flake8
- ✅ Proper documentation

Perfect for demonstrating a complete CI/CD workflow!

## License

This is a simple demo application for educational purposes.
