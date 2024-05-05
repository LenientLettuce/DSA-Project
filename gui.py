import tkinter as tk
import tkinter.filedialog

title_font = ("TkDefaultFont", 20)

def main_page():
    page = tk.Tk()
    title = tk.Label(page, text="Quadtree Image Maniplation", font=title_font)
    title.pack(ipady=15, ipadx=10)

    button_compression = tk.Button(page, text="Image Compression", width=30, command=lambda: (page.destroy(), compression_page())).pack(anchor="center",pady=4)
    button_color_shift = tk.Button(page, text="Color Shifting", width=30, command=lambda: (page.destroy(), color_page())).pack(anchor="center",pady=4)
    button_scaling = tk.Button(page, text="Image Downscaling", width=30, command=lambda: (page.destroy(), scaling_page())).pack(anchor="center",pady=4)
    button_rotation_shift = tk.Button(page, text="Recursive Rotation Shift", width=30, command=lambda: (page.destroy(), rotation_shift_page())).pack(anchor="center",pady=4)

    space = tk.Label(page, text="").pack(ipady=3)
    
    page.mainloop()

def color_page():
    page = tk.Tk()
    title = tk.Label(page, text="Color Manipulation", font=title_font)
    title.pack(ipady=15, ipadx=10)

    button_contrast = tk.Button(page, text="Image Contrast Shift", width=30, command=lambda: (page.destroy())).pack(anchor="center",pady=4)
    button_grayscale = tk.Button(page, text="Image Grayscale Shift", width=30, command=lambda: (page.destroy())).pack(anchor="center",pady=4)
    button_rgb_tint = tk.Button(page, text="Image Color Shift", width=30, command=lambda: (page.destroy())).pack(anchor="center",pady=4)
    button_tinted = tk.Button(page, text="Image Tint", width=30, command=lambda: (page.destroy())).pack(anchor="center",pady=4)

    space = tk.Label(page, text="").pack(ipady=3)
    
    page.mainloop()

# color shift pages
def contrast_page():
    page = tk.Tk()

def grayscale_page():
    page = tk.Tk()

def rgb_tint_page():
    page = tk.Tk()

def tinted_page():
    page = tk.Tk()


# rest of pages

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

def rotation_shift_page():
    page = tk.Tk()
    title = tk.Label(page, text="Rotation Shift", font=title_font)
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

    # rotate frame
    rotate_frame = tk.Frame(page)
    rotate_frame.pack(fill="x", pady=5)
    
    # rotation depth select
    rotation_depth_frame = tk.Frame(rotate_frame)
    rotation_depth_frame.pack(side="left", pady=5, padx=10)

    rotation_depth_label = tk.Label(rotation_depth_frame, text="Choose Rotation Depth")
    rotation_depth_label.pack()
    v = tk.IntVar(value=1)

    depth = tk.Scale(page, from_=1, to=5, variable=v)
    depth.pack(anchor="w", padx=45)
    
    # run downscaling and display
    rotate_button = tk.Button(rotate_frame, text="Rotate", width=15, command=lambda: print(v.get()))
    rotate_button.pack(side="right", ipady=5, padx=10)

    space = tk.Label(page, text="").pack(ipady=5)

    main_return = tk.Button(page, text="Back to main", width=15, command=lambda: (page.destroy(), main_page()))
    main_return.pack(anchor="sw")

    tk.mainloop()

def compression_page():
    page = tk.Tk()
    title = tk.Label(page, text="Image Compression", font=title_font)
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

    # Compression frame
    compression_frame = tk.Frame(page)
    compression_frame.pack(fill="x", pady=10)
    
    # threshold select
    threshold_frame = tk.Frame(compression_frame)
    threshold_frame.pack(side="left", pady=5, padx=10)

    threshold_label = tk.Label(threshold_frame, text="Choose Threshold")
    threshold_label.pack()
    v = tk.IntVar(value=1)

    threshold = tk.Scale(page, from_=1, to=100, variable=v)
    threshold.pack(anchor="w", padx=35, pady=8)
    
    # run compression and display
    compress_button = tk.Button(compression_frame, text="Compress -> Display", width=15)
    compress_button.pack(side="right", ipady=7, padx=10)

    gif_button = tk.Button(page, text="Create GIF", width=15)
    gif_button.pack(anchor="e", ipady=5, padx=10)

    space = tk.Label(page, text="").pack(ipady=10)

    main_return = tk.Button(page, text="Back to main", width=15, command=lambda: (page.destroy(), main_page()))
    main_return.pack(anchor="sw")

    tk.mainloop()

main_page()