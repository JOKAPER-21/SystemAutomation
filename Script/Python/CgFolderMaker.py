import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime
import os

def submit_form():
    # Retrieve user input
    name = entry_name.get()
    project_name = entry_project.get()
    selected_date = date_entry.get()

    # Check if fields are empty
    if not name or not project_name:
        messagebox.showerror("Error", "All fields are required!")
        return

    # Format the date
    date_object = datetime.strptime(selected_date, "%m/%d/%y")
    formatted_date = date_object.strftime("%y%m%d")  # Format as YYMMDD

    # Create the formatted output
    formatted_output = f"{name}_{formatted_date}_{project_name}"

    # Display the formatted output
    # messagebox.showinfo("Formatted Output", f"Generated Name: {formatted_output}")

    # Create the folder structure in the current folder
    folder_name = formatted_output  # Use the formatted output as the folder name
    current_path = os.getcwd()  # Get the current working directory
    base_path = os.path.join(current_path, folder_name)  # Combine current directory with folder name

    try:
        # Create base folder
        os.makedirs(base_path)

        # Create the subfolder structure
        os.makedirs(os.path.join(base_path, "scene", "export", "fbx"))
        os.makedirs(os.path.join(base_path, "scene", "export", "obj"))
        os.makedirs(os.path.join(base_path, "scene", "export", "usd"))
        os.makedirs(os.path.join(base_path, "scene", "renderOutput", "image", "blender"))
        os.makedirs(os.path.join(base_path, "scene", "renderOutput", "image", "photoshop"))
        os.makedirs(os.path.join(base_path, "scene", "renderOutput", "imageSeq"))
        os.makedirs(os.path.join(base_path, "scene", "renderOutput", "video"))
        os.makedirs(os.path.join(base_path, "scene", "reference"))
        os.makedirs(os.path.join(base_path, "scene", "textures", "cgTextures"))
        os.makedirs(os.path.join(base_path, "scene", "textures", "compTextures"))
        os.makedirs(os.path.join(base_path, "scene", "workfile", "blender"))
        os.makedirs(os.path.join(base_path, "scene", "workfile", "photoshop"))

        os.makedirs(os.path.join(base_path, "final", "export", "fbx"))
        os.makedirs(os.path.join(base_path, "final", "export", "obj"))
        os.makedirs(os.path.join(base_path, "final", "export", "usd"))
        os.makedirs(os.path.join(base_path, "final", "renderOutput", "image"))
        os.makedirs(os.path.join(base_path, "final", "renderOutput", "imageSeq"))
        os.makedirs(os.path.join(base_path, "final", "renderOutput", "video"))
        os.makedirs(os.path.join(base_path, "final", "workfile", "blender"))
        os.makedirs(os.path.join(base_path, "final", "workfile", "photoshop"))

        messagebox.showinfo("Folder Created", f"Folder structure for {formatted_output} created successfully in {current_path}")
    except FileExistsError:
        messagebox.showerror("Error", f"Folder '{formatted_output}' already exists.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while creating folders: {e}")

# Get the current date
current_date = datetime.now()

# Create the main window
root = tk.Tk()
root.title("Folder Maker")

# Set the window dimensions
window_width = 800
window_height = 500

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate position x and y to center the window
position_x = (screen_width - window_width) // 2
position_y = (screen_height - window_height) // 2

# Set the geometry of the window with the calculated position
root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
root.resizable(True, True)  # Allow resizing

# Configure grid to center content
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)

# Add Title Label
title_label = tk.Label(root, text="Folder Maker Application", font=("Helvetica", 18, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=20)

# Create Labels and Entry fields
label_name = tk.Label(root, text="Software Name:", font=("Helvetica", 12))
label_name.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_name = tk.Entry(root, font=("Helvetica", 12))
entry_name.grid(row=1, column=1, padx=10, pady=5, sticky="w")

label_project = tk.Label(root, text="Project Name:", font=("Helvetica", 12))
label_project.grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_project = tk.Entry(root, font=("Helvetica", 12))
entry_project.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Add a Date Selection
label_date = tk.Label(root, text="Select Date:", font=("Helvetica", 12))
label_date.grid(row=3, column=0, padx=10, pady=5, sticky="e")
date_entry = DateEntry(root, 
                       width=18, 
                       background='darkblue', 
                       foreground='white', 
                       borderwidth=4, 
                       year=current_date.year, 
                       month=current_date.month, 
                       day=current_date.day, 
                       font=("Helvetica", 12),
                       showweeknumbers=False)
date_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

# Create Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_form, font=("Helvetica", 12), bg="Green", fg="white")
submit_button.grid(row=4, column=0, columnspan=2, pady=20)

# Run the application
root.mainloop()
