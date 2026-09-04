def calculate(first_number, operator, second_number):
	if operator == "+":
		return first_number + second_number
	if operator == "-":
		return first_number - second_number
	if operator == "*":
		return first_number * second_number
	if operator == "/":
		if second_number == 0:
			raise ValueError("Cannot divide by zero.")
		return first_number / second_number
	raise ValueError("Unsupported operation. Use +, -, *, or /.")


def main():
	first_number = float(input("Enter the first number: "))
	operator = input("Enter an operation (+, -, *, /): ").strip()
	second_number = float(input("Enter the second number: "))

	try:
		result = calculate(first_number, operator, second_number)
		print(f"Result: {result}")
	except ValueError as error:
		print(f"Error: {error}")


if __name__ == "__main__":
	main()
