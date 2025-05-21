#task1
filename = "sample.txt"

try:
    with open(filename, 'r') as file:
        print("Reading file content:")
        for line_number, line in enumerate(file, start=1):
            print(f"Line {line_number}: {line.strip()}")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")


filename = "output.txt"
#task2
# Step 1: Take initial input and write to the file
initial_text = input("Enter text to write to the file: ")
with open(filename, 'w') as file:
    file.write(initial_text + "\n")
print("Data successfully written to", filename)

# Step 2: Take additional input and append to the same file
additional_text = input("Enter additional text to append: ")
with open(filename, 'a') as file:
    file.write(additional_text + "\n")
print("Data successfully appended.")

# Step 3: Read and display the full content of the file
print("\nFinal content of", filename + ":")
with open(filename, 'r') as file:
    content = file.read()
    print(content)
