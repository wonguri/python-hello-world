import tkinter as tk
from tkinter import ttk, messagebox

class HelloWorldApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hello World GUI Application")
        self.root.geometry("400x300")
        
        # 제목 레이블
        title_label = tk.Label(
            root, 
            text="Python GUI 애플리케이션",
            font=("Arial", 18, "bold"),
            pady=20
        )
        title_label.pack()
        
        # 입력 프레임
        input_frame = tk.Frame(root)
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="이름:").grid(row=0, column=0, padx=5)
        self.name_entry = tk.Entry(input_frame, width=20)
        self.name_entry.grid(row=0, column=1, padx=5)
        
        # 버튼
        button_frame = tk.Frame(root)
        button_frame.pack(pady=20)
        
        greet_btn = tk.Button(
            button_frame,
            text="인사하기",
            command=self.greet,
            bg="#4CAF50",
            fg="white",
            padx=20,
            pady=10,
            font=("Arial", 12)
        )
        greet_btn.pack(side=tk.LEFT, padx=5)
        
        clear_btn = tk.Button(
            button_frame,
            text="초기화",
            command=self.clear,
            bg="#f44336",
            fg="white",
            padx=20,
            pady=10,
            font=("Arial", 12)
        )
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # 결과 레이블
        self.result_label = tk.Label(
            root,
            text="",
            font=("Arial", 14),
            fg="#2196F3"
        )
        self.result_label.pack(pady=20)
        
        # 하단 정보
        info_label = tk.Label(
            root,
            text="Python + Tkinter로 만든 GUI 애플리케이션",
            font=("Arial", 9),
            fg="gray"
        )
        info_label.pack(side=tk.BOTTOM, pady=10)
    
    def greet(self):
        name = self.name_entry.get()
        if name:
            self.result_label.config(text=f"안녕하세요, {name}님! 👋")
            messagebox.showinfo("환영합니다", f"{name}님, 환영합니다!")
        else:
            messagebox.showwarning("경고", "이름을 입력해주세요!")
    
    def clear(self):
        self.name_entry.delete(0, tk.END)
        self.result_label.config(text="")

def main():
    root = tk.Tk()
    app = HelloWorldApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
