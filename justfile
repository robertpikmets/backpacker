# List all available recipes
default:
	just --list

# Run checks
check:
	ruff check backpacker

# Linting
lint:
	ruff check --fix

# Automatically fix all formating
format:
	ruff format backpacker