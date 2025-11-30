# Simulação Educacional de Malware: Ransomware e Keylogger em Python

**⚠️ AVISO LEGAL**: Este projeto é **exclusivamente educacional** para estudos em segurança da informação. Execute **apenas em ambiente isolado** (VM, sandbox). Uso indevido viola leis (ex: art. 154-A CP brasileiro). Não sou responsável por misuse.

## Descrição
Implementação prática de simulações seguras de ransomware (criptografia reversível) e keylogger (captura de teclas). Inclui reflexões sobre defesas. Baseado no desafio de bootcamp de segurança.

### Objetivos
- Entender mecânicas de malwares comuns.
- Programar em Python de forma ética.
- Documentar defesas (antivírus, backups, conscientização).

## Estrutura do Projeto

├── README.md                  # Este arquivo

├── requirements.txt           # Dependências Python

├── .gitignore                 # Ignora arquivos sensíveis

├── ransomware/                # Simulação de ransomware

│   ├── ransom_simulator.py

│   ├── test_files/            # Arquivos de teste (gerados em runtime)

│   └── images/                # Screenshots opcionais

├── keylogger/                 # Simulação de keylogger

│   ├── keylogger_simulado.py

│   ├── stealth_mode.py        # Técnicas furtivas (educacional)

│   ├── email_sender_simulado.py  # Envio simulado

│   └── logs/                  # Logs gerados

└── defense/                   # Documentação de defesas

└── defesa_contra_malware.md


## Como Usar (Seguro!)
1. Clone o repo: `git clone https://github.com/lcardeal/Security.git`
2. Vá pra pasta: `cd Security/Bootcamp2`
3. Instale deps: `pip install -r requirements.txt`
4. Teste ransomware: `cd ransomware && python ransom_simulator.py` (use `python ransom_simulator.py decrypt` pra reverter)
5. Teste keylogger: `cd keylogger && python keylogger_simulado.py` (Ctrl+C pra parar)
6. **Sempre em VM!** Tire snapshot antes.

## Aprendizados
- Malwares exploram brechas humanas (phishing) e técnicas (SMB/RDP).
- Defesas: Backups 3-2-1, EDR, treinamento.

Feito em Novembro/2025 para Bootcamp2 de segurança. Contribuições bem-vindas (éticas)!

![Ransomware Demo](ransomware/images/ransomware_before.png)
