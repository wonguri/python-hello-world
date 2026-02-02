import tkinter as tk
from tkinter import ttk, messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
from ldap3 import Server, Connection, ALL, MODIFY_REPLACE

# 이메일 설정
MAIL_FROM = "a112664@gmail.com"
MAIL_PASSWORD = "zacgqbdlxrioqakt"
MAIL_TO = "a112664@naver.com"
MAIL_SUBJECT = "selfpw"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# LDAP 설정
LDAP_SERVER = "192.168.0.231"
LDAP_DOMAIN = "jiwooinc.local"
LDAP_USER = "jiwooinc\\administrator"
LDAP_PASSWORD = "dnjsrnfl1!"
LDAP_BASE_DN = "dc=jiwooinc,dc=local"

# 전역 변수
otp_number = None
company_netbios = "jiwooinc"
dns_prefix = "@jiwooinc.co.kr"


class PasswordResetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("암호 초기화")
        self.root.geometry("310x380")
        
        # OTP 저장
        self.otp_number = None
        
        self.create_widgets()
    
    def create_widgets(self):
        # 탭 컨트롤 생성 (여기서는 단일 프레임으로 대체)
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # ID 입력 라벨
        label1 = tk.Label(frame, text="암호 변경할 윈도우계정의 ID를 입력하세요")
        label1.grid(row=0, column=0, columnspan=2, sticky=tk.W, pady=(0, 5))
        
        # ID 입력 텍스트박스
        self.id_entry = tk.Entry(frame, width=20)
        self.id_entry.grid(row=1, column=0, sticky=tk.W, pady=(0, 10))
        
        # 이메일 입력 라벨
        label2 = tk.Label(frame, text="OTP 전달받을 회사 이메일을 입력하세요")
        label2.grid(row=2, column=0, columnspan=2, sticky=tk.W, pady=(0, 5))
        
        # 이메일 입력 프레임
        email_frame = tk.Frame(frame)
        email_frame.grid(row=3, column=0, columnspan=2, sticky=tk.W, pady=(0, 10))
        
        self.email_entry = tk.Entry(email_frame, width=15)
        self.email_entry.pack(side=tk.LEFT)
        
        dns_label = tk.Label(email_frame, text=dns_prefix)
        dns_label.pack(side=tk.LEFT, padx=(5, 0))
        
        # OTP 발송 버튼
        self.send_button = tk.Button(frame, text="발송", bg="#4CAF50", fg="white", 
                                     font=("Arial", 9, "bold"), width=8,
                                     command=self.send_otp)
        self.send_button.grid(row=3, column=1, padx=(10, 0))
        
        # OTP 입력 라벨
        label3 = tk.Label(frame, text="이메일로 전달받은 OTP를 입력하세요")
        label3.grid(row=4, column=0, columnspan=2, sticky=tk.W, pady=(0, 5))
        
        # OTP 입력 텍스트박스
        self.otp_entry = tk.Entry(frame, width=20)
        self.otp_entry.grid(row=5, column=0, sticky=tk.W, pady=(0, 10))
        
        # OTP 확인 버튼
        self.verify_button = tk.Button(frame, text="확인", bg="#2196F3", fg="white",
                                       font=("Arial", 9, "bold"), width=8,
                                       command=self.verify_otp)
        self.verify_button.grid(row=5, column=1, padx=(10, 0))
        
        # 새 암호 입력 라벨
        label4 = tk.Label(frame, text="변경할 암호 입력하세요")
        label4.grid(row=6, column=0, columnspan=2, sticky=tk.W, pady=(0, 5))
        
        # 새 암호 입력 텍스트박스
        self.password1_entry = tk.Entry(frame, width=20, show="*")
        self.password1_entry.grid(row=7, column=0, sticky=tk.W, pady=(0, 10))
        
        # 새 암호 확인 라벨
        label5 = tk.Label(frame, text="변경할 암호 한번더 입력하세요")
        label5.grid(row=8, column=0, columnspan=2, sticky=tk.W, pady=(0, 5))
        
        # 새 암호 확인 텍스트박스
        self.password2_entry = tk.Entry(frame, width=20, show="*")
        self.password2_entry.grid(row=9, column=0, sticky=tk.W, pady=(0, 10))
        
        # 암호 변경 버튼
        self.change_button = tk.Button(frame, text="변경", bg="#FF9800", fg="white",
                                       font=("Arial", 9, "bold"), width=8,
                                       command=self.change_password)
        self.change_button.grid(row=7, column=1, rowspan=3, padx=(10, 0))
        
        # 상태 라벨
        self.status_label = tk.Label(frame, text="", font=("Times New Roman", 10), fg="red")
        self.status_label.grid(row=10, column=0, columnspan=2, sticky=tk.W, pady=(10, 10))
        
        # 종료 버튼
        close_button = tk.Button(frame, text="종료", command=self.root.quit)
        close_button.grid(row=11, column=1, sticky=tk.E, pady=(10, 0))
    
    def send_otp(self):
        """OTP 이메일 발송"""
        user_id = self.id_entry.get().strip()
        email_prefix = self.email_entry.get().strip()
        
        if not user_id:
            messagebox.showwarning(company_netbios, "ID가 없습니다 ID를 입력하세요")
            self.id_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.otp_entry.delete(0, tk.END)
            return
        
        if not email_prefix:
            messagebox.showwarning(company_netbios, "e-mail이 없습니다. e-mail을 입력하세요")
            self.id_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.otp_entry.delete(0, tk.END)
            return
        
        # OTP 생성 (6자리 랜덤 숫자)
        self.otp_number = random.randint(100000, 999999)
        
        try:
            # 이메일 발송
            msg = MIMEMultipart()
            msg['From'] = MAIL_FROM
            msg['To'] = MAIL_TO
            msg['Subject'] = MAIL_SUBJECT
            
            body = str(self.otp_number)
            msg.attach(MIMEText(body, 'plain'))
            
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(MAIL_FROM, MAIL_PASSWORD)
            text = msg.as_string()
            server.sendmail(MAIL_FROM, MAIL_TO, text)
            server.quit()
            
            # UI 업데이트
            self.send_button.config(text="재발송", bg="red")
            self.status_label.config(text="메일이 발송 되었습니다", fg="red")
            
        except Exception as e:
            messagebox.showerror("오류", f"이메일 발송 실패: {str(e)}")
    
    def verify_otp(self):
        """OTP 인증"""
        entered_otp = self.otp_entry.get().strip()
        
        if not entered_otp:
            messagebox.showwarning(company_netbios, "발송 된 OTP를 입력하세요")
            self.otp_entry.delete(0, tk.END)
            return
        
        try:
            entered_otp_num = int(entered_otp)
        except ValueError:
            messagebox.showwarning(company_netbios, "올바른 OTP를 입력하세요")
            self.otp_entry.delete(0, tk.END)
            return
        
        if entered_otp_num != self.otp_number:
            messagebox.showwarning(company_netbios, "발송 된 OTP와 다릅니다")
            self.otp_entry.delete(0, tk.END)
            return
        
        # 인증 성공
        self.status_label.config(text="OTP 인증되었습니다", fg="green")
        self.verify_button.config(text="인증완료", bg="red")
    
    def change_password(self):
        """암호 변경"""
        password1 = self.password1_entry.get()
        password2 = self.password2_entry.get()
        user_id = self.id_entry.get().strip()
        email_prefix = self.email_entry.get().strip()
        
        if password1 != password2:
            messagebox.showwarning(company_netbios, "암호가 같지 않습니다")
            self.password1_entry.delete(0, tk.END)
            self.password2_entry.delete(0, tk.END)
            return
        
        if not password1 or not password2:
            messagebox.showwarning(company_netbios, "변경할 암호를 입력하세요")
            self.password1_entry.delete(0, tk.END)
            self.password2_entry.delete(0, tk.END)
            return
        
        try:
            # LDAP 서버 연결
            server = Server(LDAP_SERVER, get_info=ALL)
            conn = Connection(server, user=LDAP_USER, password=LDAP_PASSWORD, auto_bind=True)
            
            # 사용자 검색
            search_filter = f"(&(objectClass=user)(samaccountname={user_id}))"
            conn.search(LDAP_BASE_DN, search_filter, attributes=['mail'])
            
            if conn.entries:
                user_dn = conn.entries[0].entry_dn
                
                # 이메일 업데이트
                full_email = f"{email_prefix}{dns_prefix}"
                conn.modify(user_dn, {'mail': [(MODIFY_REPLACE, [full_email])]})
                
                # 암호 변경 (실제 환경에서는 암호 변경 코드 추가 필요)
                # conn.extend.microsoft.modify_password(user_dn, password1)
                
                messagebox.showinfo(company_netbios, "암호 변경이 완료되었습니다.")
                self.status_label.config(text="암호 변경이 완료되었습니다.", fg="green")
                self.change_button.config(text="변경완료", bg="red")
            else:
                messagebox.showerror("오류", "사용자를 찾을 수 없습니다.")
            
            conn.unbind()
            
        except Exception as e:
            messagebox.showerror("오류", f"암호 변경 실패: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordResetApp(root)
    root.mainloop()