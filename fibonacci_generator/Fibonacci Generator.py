import tkinter as tk

def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

def get_fibonacci():
    number = int(entry.get())
    sequence = fibonacci(number)
    result_label.config(text=f"Fibonacci sequence: {sequence}")

# tkinter main window configuration
root = tk.Tk()
root.title("Fibonacci Sequence Generator")

# Input for the number of elements of the Fibonacci sequence
entry_label = tk.Label(root, text="Enter the number of Fibonacci elements:")
entry_label.pack()
entry = tk.Entry(root)
entry.pack()

# Button to generate the Fibonacci sequence
fib_button = tk.Button(root, text="Generate Fibonacci", command=get_fibonacci)
fib_button.pack()

# Label to display the result
result_label = tk.Label(root, text="Fibonacci sequence: ")
result_label.pack()

# Start tkinter main loop
root.mainloop()
