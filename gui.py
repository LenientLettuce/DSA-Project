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

    # file selection
    filename = "None"

    def select_file():
        nonlocal filename
        nonlocal filename_display
        file = tkinter.filedialog.askopenfile()
        filename = file.name.split("/")[-1]
        filename_display.config(text=f"Selected file = {filename}")

    file_frame = tk.Frame(page)
    file_frame.pack(fill="x", pady=5)

    file_select = tk.Button(file_frame, text="Select File", width=15, command=lambda: select_file())
    file_select.pack(side="left", padx=8)
    filename_display = tk.Label(file_frame, text=f"Selected file = {filename}")
    filename_display.pack(side="right", ipady=5, padx=8)

    # image display
    display_original = tk.Button(page, text="Display Original", width=15)
    display_original.pack(anchor="w", padx=8, ipady=5)

    # Downscaling frame
    downscale_frame = tk.Frame(page)
    downscale_frame.pack(fill="x", pady=5)
    
    # scale factor select
    scale_factor_frame = tk.Frame(downscale_frame)
    scale_factor_frame.pack(side="left", pady=5, padx=10)

    scale_factor_label = tk.Label(scale_factor_frame, text="Select Scale Factor")
    scale_factor_label.pack()
    v = tk.IntVar(value=4)

    tk.Radiobutton(scale_factor_frame, text="4", variable=v, value=4).pack()
    tk.Radiobutton(scale_factor_frame, text="8", variable=v, value=8).pack()
    
    # run downscaling and display
    downscale_button = tk.Button(downscale_frame, text="Downscale", width=15)
    downscale_button.pack(side="right", ipady=5, padx=10)

    # AI upscale and display
    upscale_button = tk.Button(page, text="AI-based Upscale", width=15)
    upscale_button.pack(ipady=5)

    space = tk.Label(page, text="").pack(ipady=5)

    main_return = tk.Button(page, text="Back to main", width=15, command=lambda: (page.destroy(), main_page()))
    main_return.pack(anchor="sw")

    tk.mainloop()

main_page()