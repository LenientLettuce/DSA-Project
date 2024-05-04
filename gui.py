import tkinter as tk
import tkinter.filedialog

title_font = ("TkDefaultFont", 20)

def main_page():
    page = tk.Tk()
    title = tk.Label(page, text="Quadtree Image Maniplation", font=title_font)
    title.pack(ipady=15, ipadx=10)

    button_compression = tk.Button(page, text="Image Compression", width=30).pack(anchor="center")
    button_color_shift = tk.Button(page, text="Color Shifting", width=30).pack(anchor="center")
    button_scaling = tk.Button(page, text="Image Downscaling", width=30, command=lambda: (page.destroy(), scaling_page())).pack(anchor="center")
    button_rotation_shift = tk.Button(page, text="Recursive Rotation Shift", width=30).pack(anchor="center")
    
    page.mainloop()

def scaling_page():
    page = tk.Tk()
    title = tk.Label(page, text="Image Downscaling", font=title_font)
    title.pack(ipady=15, ipadx=10)

    filename = "None"

    def select_file():
        nonlocal filename
        nonlocal filename_display
        file = tkinter.filedialog.askopenfile()
        filename = file.name.split("/")[-1]
        filename_display.config(text=f"Selected file = {filename}")

    file_select = tk.Button(page, text="Select File", width=15, command=lambda: select_file())
    file_select.pack()
    filename_display = tk.Label(page, text=f"Selected file = {filename}")
    filename_display.pack()
    v = tk.IntVar(value=4)
    tk.Radiobutton(page, text="4", variable=v, value=4).pack()
    tk.Radiobutton(page, text="8", variable=v, value=8).pack()

    main_return = tk.Button(page, text="Back to main", width=15, command=lambda: (page.destroy(), main_page()))
    main_return.pack(anchor="sw")

    tk.mainloop()

main_page()