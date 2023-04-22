import tkinter as tk

class Navigation:
    def __init__(self, master, *pages):
        self.master = master
        self.pages = pages
        self.current_page = None
        self.page_buttons_frame = tk.Frame(self.master)
        self.page_buttons_frame.pack(side=tk.TOP, pady=10)

        for i, page in enumerate(self.pages):
            button = tk.Button(self.page_buttons_frame, text=f"Page {i + 1}", command=lambda p=page: self.show_page(p))
            button.pack(side=tk.LEFT, padx=5)

    def show_page(self, page):
        if self.current_page:
            self.current_page.frame.pack_forget()

        self.current_page = page(self.master)
        self.current_page.frame.pack(fill=tk.BOTH, expand=True)


