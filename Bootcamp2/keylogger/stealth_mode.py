# Exemplo de técnicas que malwares usam (NÃO EXECUTE FORA DE VM)
import ctypes
import os
import sys

def esconder_janela_console():
    """Esconde a janela do terminal (Windows)"""
    try:
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    except:
        pass

def adicionar_ao_startup():
    """Adiciona ao Registro do Windows (apenas exemplo)"""
    print("[!] Exemplo de persistência - NÃO EXECUTADO")
    # Exemplo comentado: reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v Update /t REG_SZ /d "python keylogger.py" /f

def renomear_para_sistema():
    """Muda nome do executável para parecer legítimo"""
    novos_nomes = ["svchost.exe", "explorer.exe", "winlogon.exe"]
    print(f"[!] Em ambiente real, poderia se chamar: {novos_nomes[0]}")

if __name__ == "__main__":
    print("[+] Demonstração de técnicas stealth (educacional apenas)")
    esconder_janela_console()  # Teste só em VM
