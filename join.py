# -*- coding: utf-8 -*-
"""
Active Directory Domain Join/Unjoin Tool
지우인크 도메인 가입/탈퇴 관리 도구
"""

import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import platform
import os
import sys
import socket
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import base64
from io import BytesIO
from PIL import Image, ImageTk
import shutil
from pathlib import Path
from ldap3 import Server, Connection, ALL, MODIFY_REPLACE
from datetime import datetime

# ===== 설정 값 =====
COMPANY_NAME = "jiwooinc.local"
COMPANY_NETBIOS = "jiwooinc"
COMPANY_DNS1 = "192.168.0.231"
COMPANY_DNS2 = "168.126.63.1"
AD_HOST = "ad1."
LICENSE_EXPIRY = "20261231"
USER_LICENSE_LIMIT = 2000

# LDAP 설정
LDAP_SERVER = "192.168.0.231"
LDAP_BASE_DN = "dc=jiwooinc,dc=local"
LDAP_USER = "jiwooinc\\administrator"
LDAP_PASSWORD = "dnjsrnfl1!"
DOMAIN_ADMIN_ID = "administrator"
DOMAIN_ADMIN_PW = "dnjsrnfl1!"

# 이메일 설정
MAIL_FROM = "a112664@gmail.com"
MAIL_PASSWORD = "zacgqbdlxrioqakt"
MAIL_TO = "a112664@naver.com"
MAIL_SUBJECT = "ad mailer5"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# DNS 설정
SET_DNS_IP = "static"  # "static" 또는 "dhcp"

# UI 색상
BG_COLOR = "#0B4715"
FG_COLOR = "white"

# 로고 이미지 (Base64)
ICON_BASE64 = "iVBORw0KGgoAAAANSUhEUgAAAHwAAAI8CAYAAAA4dBMXAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAXEQAAFxEByibzPwAABItJREFUaEPtWulC4jAQroysiBd4oO6qq+sBLgoK4omsB+qKq7//2zTUMzMcU0mwHMoMpL3MMdckwHH68zbSDQY0qEX86D4ruCyBfdCV/Dg8Pe1PDGehdGYU7n2FxRbIyfGtEdsyxpjuPx7RzAv+1X91ikYVLl5lFh3quM3QXYUv3/Yp89oHAdPoZA+XTMUzhfKSGfc7y9jp5bPFoURsMFYYsBQnxkOlx0/lFzX2MoXsJK+Hn6D2ggpRC8LD8JFmT7gmO5vd1E+o5+RSz2D4Knz3f3kARfJ/pBK9TzAHmnyG5W7Kguv/I/JvD02Izp8Xjx6Vvd3ueQw9F0PvV..." # 생략 (원본 Base64 너무 김)


class ADManagementTool:
    def __init__(self, root):
        self.root = root
        self.root.title("도메인 가입/탈퇴 관리도구")
        self.root.geometry("330x420")
        self.root.configure(bg=BG_COLOR)
        
        # OTP 저장
        self.otp_number = None
        
        # 라이선스 체크
        if not self.check_license():
            messagebox.showerror("License Error", 
                               "회사 또는 라이선스 수량 오류\nPlease contact the manufacturer")
            sys.exit(1)
        
        self.create_widgets()
    
    def check_license(self):
        """라이선스 유효성 체크"""
        try:
            today = datetime.now()
            today_str = today.strftime("%Y%m%d")
            
            if int(today_str) > int(LICENSE_EXPIRY):
                return False
            
            # AD 컴퓨터 개수 체크 (간단히 구현)
            # 실제 환경에서는 LDAP 쿼리로 확인
            return True
        except:
            return True
    
    def create_widgets(self):
        """GUI 위젯 생성"""
        # 탭 컨트롤
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # 탭 생성
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)
        self.tab4 = ttk.Frame(self.notebook)
        
        self.notebook.add(self.tab1, text="■도메인가입")
        self.notebook.add(self.tab2, text="■탈퇴")
        self.notebook.add(self.tab3, text="■프로필복사")
        self.notebook.add(self.tab4, text="■암호초기화")
        
        # 각 탭 UI 생성
        self.create_tab1()  # 도메인 가입
        self.create_tab2()  # 도메인 탈퇴
        self.create_tab3()  # 프로필 복사
        self.create_tab4()  # 암호 초기화
    
    def create_tab1(self):
        """탭1: 도메인 가입"""
        frame = ttk.Frame(self.tab1, padding="10")
        frame.pack(fill='both', expand=True)
        
        # 사용자 ID
        tk.Label(frame, text="사용자 계정").pack(anchor='w')
        self.join_user_id = tk.Entry(frame, width=30)
        self.join_user_id.pack(pady=(0, 10))
        
        # 계정 이름
        tk.Label(frame, text="계정 이름").pack(anchor='w')
        self.join_user_name = tk.Entry(frame, width=30)
        self.join_user_name.pack(pady=(0, 10))
        
        # 컴퓨터 이름
        tk.Label(frame, text="컴퓨터명").pack(anchor='w')
        self.join_computer_name = tk.Entry(frame, width=30)
        self.join_computer_name.insert(0, socket.gethostname())
        self.join_computer_name.config(state='disabled')
        self.join_computer_name.pack(pady=(0, 10))
        
        # 가입 버튼
        btn_frame = tk.Frame(frame)
        btn_frame.pack(pady=20)
        
        join_btn = tk.Button(btn_frame, text="가입", width=10, 
                            bg=BG_COLOR, fg=FG_COLOR,
                            command=self.join_domain)
        join_btn.pack(side='left', padx=5)
        
        cancel_btn = tk.Button(btn_frame, text="취소", width=10,
                              command=self.root.quit)
        cancel_btn.pack(side='left', padx=5)
    
    def create_tab2(self):
        """탭2: 도메인 탈퇴"""
        frame = ttk.Frame(self.tab2, padding="10")
        frame.pack(fill='both', expand=True)
        
        # 현재 도메인 정보
        tk.Label(frame, text="현재 계정 ID").pack(anchor='w')
        current_user = f"{COMPANY_NAME}\\{os.getenv('USERNAME', '')}"
        self.unjoin_current_id = tk.Entry(frame, width=30)
        self.unjoin_current_id.insert(0, current_user)
        self.unjoin_current_id.config(state='disabled')
        self.unjoin_current_id.pack(pady=(0, 10))
        
        # AD 탈퇴 후 사용할 로컬 계정
        tk.Label(frame, text="AD 탈퇴 후 사용할 로컬 계정").pack(anchor='w')
        self.unjoin_local_account = ttk.Combobox(frame, width=28)
        # 실제로는 프로파일 목록을 가져와야 함
        self.unjoin_local_account['values'] = ['administrator', 'user']
        self.unjoin_local_account.pack(pady=(0, 10))
        
        # 탈퇴 버튼
        btn_frame = tk.Frame(frame)
        btn_frame.pack(pady=20)
        
        unjoin_btn = tk.Button(btn_frame, text="탈퇴", width=10,
                              bg="red", fg="white",
                              command=self.unjoin_domain)
        unjoin_btn.pack(side='left', padx=5)
        
        cancel_btn = tk.Button(btn_frame, text="취소", width=10,
                              command=self.root.quit)
        cancel_btn.pack(side='left', padx=5)
    
    def create_tab3(self):
        """탭3: 프로필 복사"""
        frame = ttk.Frame(self.tab3, padding="10")
        frame.pack(fill='both', expand=True)
        
        tk.Label(frame, text="프로필을 복사할 계정 선택").pack(anchor='w')
        self.copy_source_account = ttk.Combobox(frame, width=28)
        self.copy_source_account.pack(pady=(0, 10))
        
        tk.Label(frame, text="현재 컴퓨터명").pack(anchor='w')
        self.copy_computer_name = tk.Entry(frame, width=30)
        self.copy_computer_name.insert(0, socket.gethostname())
        self.copy_computer_name.config(state='disabled')
        self.copy_computer_name.pack(pady=(0, 10))
        
        # 진행률 표시
        self.copy_progress = ttk.Progressbar(frame, length=280, mode='determinate')
        self.copy_progress.pack(pady=10)
        
        # 복사 버튼
        btn_frame = tk.Frame(frame)
        btn_frame.pack(pady=20)
        
        copy_btn = tk.Button(btn_frame, text="프로필복사", width=12,
                            bg=BG_COLOR, fg=FG_COLOR,
                            command=self.copy_profile)
        copy_btn.pack(side='left', padx=5)
        
        cancel_btn = tk.Button(btn_frame, text="취소", width=10,
                              command=self.root.quit)
        cancel_btn.pack(side='left', padx=5)
    
    def create_tab4(self):
        """탭4: 암호 초기화 (OTP)"""
        frame = ttk.Frame(self.tab4, padding="10")
        frame.pack(fill='both', expand=True)
        
        # 사용자 ID
        tk.Label(frame, text="암호 변경할 윈도우계정 ID").pack(anchor='w')
        self.reset_user_id = tk.Entry(frame, width=20)
        self.reset_user_id.pack(pady=(0, 10))
        
        # 이메일
        email_frame = tk.Frame(frame)
        email_frame.pack(anchor='w', pady=(0, 10))
        
        tk.Label(frame, text="OTP 전달받을 회사 이메일").pack(anchor='w')
        self.reset_email = tk.Entry(email_frame, width=15)
        self.reset_email.pack(side='left')
        tk.Label(email_frame, text="@jiwooinc.local").pack(side='left')
        
        # OTP 발송 버튼
        send_btn = tk.Button(frame, text="발송", width=8,
                            bg="green", fg="white",
                            command=self.send_otp)
        send_btn.pack(pady=(0, 10))
        
        # OTP 입력
        tk.Label(frame, text="이메일로 전달받은 OTP 입력").pack(anchor='w')
        self.reset_otp = tk.Entry(frame, width=20)
        self.reset_otp.pack(pady=(0, 5))
        
        verify_btn = tk.Button(frame, text="확인", width=8,
                              bg="blue", fg="white",
                              command=self.verify_otp)
        verify_btn.pack(pady=(0, 10))
        
        # 새 암호
        tk.Label(frame, text="변경할 암호").pack(anchor='w')
        self.reset_password1 = tk.Entry(frame, width=20, show="*")
        self.reset_password1.pack(pady=(0, 10))
        
        tk.Label(frame, text="변경할 암호 한번더").pack(anchor='w')
        self.reset_password2 = tk.Entry(frame, width=20, show="*")
        self.reset_password2.pack(pady=(0, 10))
        
        # 상태 라벨
        self.reset_status = tk.Label(frame, text="", fg="red")
        self.reset_status.pack(pady=5)
        
        # 변경 버튼
        change_btn = tk.Button(frame, text="변경", width=8,
                              bg="orange", fg="white",
                              command=self.change_password)
        change_btn.pack(pady=5)
        
        close_btn = tk.Button(frame, text="종료", width=8,
                             command=self.root.quit)
        close_btn.pack(pady=5)
    
    def join_domain(self):
        """도메인 가입"""
        user_id = self.join_user_id.get().strip()
        user_name = self.join_user_name.get().strip()
        
        if not user_id or not user_name:
            messagebox.showwarning(COMPANY_NETBIOS, "ID가 없습니다 ID를 입력하세요!!")
            return
        
        try:
            # Windows에서만 실행 가능
            if platform.system() != "Windows":
                messagebox.showerror("Error", "이 기능은 Windows에서만 사용 가능합니다")
                return
            
            # DNS 설정
            self.set_dns()
            
            # 도메인 가입 (실제 명령어)
            # Add-Computer cmdlet 사용
            username = f"{user_name}@{COMPANY_NAME}"
            
            messagebox.showinfo(COMPANY_NETBIOS, 
                              "도메인 가입을 시작합니다.\n재부팅이 필요합니다.")
            
            # PowerShell 명령 실행
            ps_cmd = f"""
            $domain = '{COMPANY_NAME}'
            $user = '{username}'
            $pass = Read-Host -AsSecureString -Prompt "암호 입력"
            $credential = New-Object System.Management.Automation.PSCredential($user, $pass)
            Add-Computer -DomainName $domain -Credential $credential -Restart
            """
            
            subprocess.run(["powershell", "-Command", ps_cmd], check=True)
            
        except Exception as e:
            messagebox.showerror("Error", f"도메인 가입 실패: {str(e)}")
    
    def unjoin_domain(self):
        """도메인 탈퇴"""
        try:
            if platform.system() != "Windows":
                messagebox.showerror("Error", "이 기능은 Windows에서만 사용 가능합니다")
                return
            
            result = messagebox.askyesno(COMPANY_NETBIOS, 
                                        "도메인에서 탈퇴하시겠습니까?\n재부팅이 필요합니다.")
            if not result:
                return
            
            ps_cmd = f"""
            $pass = ConvertTo-SecureString '{DOMAIN_ADMIN_PW}' -AsPlainText -Force
            $credential = New-Object System.Management.Automation.PSCredential('{LDAP_USER}', $pass)
            Remove-Computer -UnjoinDomainCredential $credential -PassThru -Verbose -Force -Restart
            """
            
            subprocess.run(["powershell", "-Command", ps_cmd], check=True)
            
        except Exception as e:
            messagebox.showerror("Error", f"도메인 탈퇴 실패: {str(e)}")
    
    def copy_profile(self):
        """사용자 프로필 복사"""
        source = self.copy_source_account.get()
        
        if not source:
            messagebox.showwarning(COMPANY_NETBIOS, "복사할 계정을 선택하세요")
            return
        
        try:
            current_user = os.getenv('USERNAME', '')
            source_path = Path(f"C:\\Users\\{source}")
            target_path = Path(f"C:\\Users\\{current_user}")
            
            if not source_path.exists():
                messagebox.showerror("Error", "원본 프로필을 찾을 수 없습니다")
                return
            
            # 파일 복사
            folders_to_copy = ['Desktop', 'Documents', 'Downloads', 'Pictures', 
                             'Videos', 'Music', 'Favorites', 'AppData']
            
            total = len(folders_to_copy)
            for i, folder in enumerate(folders_to_copy):
                src = source_path / folder
                dst = target_path / folder
                
                if src.exists():
                    shutil.copytree(src, dst, dirs_exist_ok=True)
                
                # 진행률 업데이트
                progress = int((i + 1) / total * 100)
                self.copy_progress['value'] = progress
                self.root.update()
            
            messagebox.showinfo(COMPANY_NETBIOS, "프로필 복사가 완료되었습니다")
            
        except Exception as e:
            messagebox.showerror("Error", f"프로필 복사 실패: {str(e)}")
    
    def send_otp(self):
        """OTP 이메일 발송"""
        user_id = self.reset_user_id.get().strip()
        email = self.reset_email.get().strip()
        
        if not user_id:
            messagebox.showwarning(COMPANY_NETBIOS, "ID가 없습니다 ID를 입력하세요")
            return
        
        if not email:
            messagebox.showwarning(COMPANY_NETBIOS, "e-mail이 없습니다. e-mail을 입력하세요")
            return
        
        # OTP 생성
        self.otp_number = random.randint(100000, 999999)
        
        try:
            # 이메일 발송
            msg = MIMEMultipart()
            msg['From'] = MAIL_FROM
            msg['To'] = MAIL_TO
            msg['Subject'] = MAIL_SUBJECT
            
            body = f"OTP 인증번호: {self.otp_number}"
            msg.attach(MIMEText(body, 'plain'))
            
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(MAIL_FROM, MAIL_PASSWORD)
            server.sendmail(MAIL_FROM, MAIL_TO, msg.as_string())
            server.quit()
            
            self.reset_status.config(text="메일이 발송 되었습니다", fg="red")
            
        except Exception as e:
            messagebox.showerror("오류", f"이메일 발송 실패: {str(e)}")
    
    def verify_otp(self):
        """OTP 인증"""
        entered_otp = self.reset_otp.get().strip()
        
        if not entered_otp:
            messagebox.showwarning(COMPANY_NETBIOS, "발송 된 OTP를 입력하세요")
            return
        
        try:
            if int(entered_otp) != self.otp_number:
                messagebox.showwarning(COMPANY_NETBIOS, "발송 된 OTP와 다릅니다")
                self.reset_otp.delete(0, tk.END)
                return
            
            self.reset_status.config(text="OTP 인증되었습니다", fg="green")
            
        except ValueError:
            messagebox.showwarning(COMPANY_NETBIOS, "올바른 OTP를 입력하세요")
    
    def change_password(self):
        """AD 암호 변경"""
        user_id = self.reset_user_id.get().strip()
        password1 = self.reset_password1.get()
        password2 = self.reset_password2.get()
        
        if password1 != password2:
            messagebox.showwarning(COMPANY_NETBIOS, "암호가 같지 않습니다")
            return
        
        if not password1:
            messagebox.showwarning(COMPANY_NETBIOS, "변경할 암호를 입력하세요")
            return
        
        try:
            # LDAP 서버 연결
            server = Server(LDAP_SERVER, get_info=ALL)
            conn = Connection(server, user=LDAP_USER, password=LDAP_PASSWORD, auto_bind=True)
            
            # 사용자 검색
            search_filter = f"(&(objectClass=user)(samaccountname={user_id}))"
            conn.search(LDAP_BASE_DN, search_filter)
            
            if conn.entries:
                user_dn = conn.entries[0].entry_dn
                
                # 암호 변경
                conn.extend.microsoft.modify_password(user_dn, password1)
                
                messagebox.showinfo(COMPANY_NETBIOS, "암호 변경이 완료되었습니다.")
                self.reset_status.config(text="암호 변경이 완료되었습니다.", fg="green")
            else:
                messagebox.showerror("오류", "사용자를 찾을 수 없습니다.")
            
            conn.unbind()
            
        except Exception as e:
            messagebox.showerror("오류", f"암호 변경 실패: {str(e)}")
    
    def set_dns(self):
        """DNS 설정"""
        if platform.system() != "Windows":
            return
        
        try:
            if SET_DNS_IP == "static":
                ps_cmd = f"""
                $adapters = Get-NetAdapter | Select-Object -ExpandProperty ifIndex
                foreach ($adapter in $adapters) {{
                    Set-DnsClientServerAddress -InterfaceIndex $adapter -ServerAddresses ('{COMPANY_DNS1}', '{COMPANY_DNS2}')
                }}
                """
                subprocess.run(["powershell", "-Command", ps_cmd], check=True)
        except Exception as e:
            print(f"DNS 설정 실패: {e}")


def main():
    root = tk.Tk()
    app = ADManagementTool(root)
    root.mainloop()


if __name__ == "__main__":
    main()
