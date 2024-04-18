def exc():
	try:
		# Code that may raise an exception
		result = 10 / 0  # Division by zero
	except ZeroDivisionError:
		# Handle specific exception
		print("Division by zero error")
	except Exception as e:
		# Handle other exceptions
		print(f"An error occurred: {e}")
	else:
		# Execute if no exception is raised
		print("No exceptions occurred")
	finally:
		# Always execute, whether an exception occurs or not
		print("Finally block executed")

if __name__ == "__main__":
	exc()