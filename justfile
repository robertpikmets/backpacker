# List all available recipes
default:
	just --list

# Run checks
check:
	ruff check backpacker

# Automatically fix all formating
format:
	ruff format backpacker