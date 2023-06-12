import tkinter as tk

# Create a new window
window = tk.Tk()

# Set the window title
window.title("Information")

# Set the window size
window.geometry("1280x720")  # Width x Height

# Set the background color
window.configure(bg="black")

# Create the "Number of Defects Detected" label
defects_label = tk.Label(window, text="Number of Defects Detected =", fg="white", bg="black", font=("Arial", 16))

# Create the "Comment/Result" label
comment_label = tk.Label(window, text="Comment/Result =", fg="white", bg="black", font=("Arial", 16))

# Use the grid layout manager to position the labels
defects_label.grid(row=0, column=0, padx=10, pady=10)
comment_label.grid(row=1, column=0, padx=10, pady=10)

# Run the main event loop
window.mainloop()
