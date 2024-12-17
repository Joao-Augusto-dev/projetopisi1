import os
import re

dados_usuarios = {}
urls = {
    "https://www.google.com", "https://www.google.com.br", "www.google.com.br", "www.google.com.",
    "https://www.youtube.com", "https://www.globo.com", "https://www.whatsapp.com", "https://www.instagram.com/"
    "https://www.facebook.com/", "https://www.uol.com.br/", "https://www.mercadolivre.com.br/", "https://www.amazon.com.br/",
    "https://chatgpt.com/", "https://x.com/", "https://www.caixa.gov.br/", "https://www.santander.com.br/", "https://www.bb.com.br/"
    "https://shopee.com.br/", "https://www.tiktok.com/", "https://www.netflix.com/br/", "https://www.primevideo.com/", "https://www.max.com/br/pt",
    "https://pt.wikipedia.org/", "https://www.twitch.tv/", "https://discord.com/", "https://nubank.com.br/", "https://www.detran.pe.gov.br/", "https://servicos.compesa.com.br/",
    "https://www.neoenergia.com/", "https://sigs.ufrpe.br/", "https://www.ufrpe.br/", "https://g1.globo.com/", "https://www.mozilla.org/", "https://pt.aliexpress.com/",
    "https://www.microsoft.com/pt-br/", "https://github.com/", "https://web.telegram.org/a/", "https://web.whatsapp.com/", "https://www.gov.br/pt-br",
    "https://br.pinterest.com/", "https://www.reddit.com/", "https://www.olx.com.br/", "https://www.linkedin.com/", "https://code.visualstudio.com/", "https://www.jetbrains.com/pt-br/pycharm/",
    "https://workspace.google.com/intl/pt-BR/gmail/", "https://mail.google.com/", "https://www.google.com.br/maps/", "https://workspace.google.com/intl/pt-BR/products/meet/", "https://www.americanas.com.br/",
    "https://workspace.google.com/intl/pt-BR/products/drive/", "https://sites.google.com/view/classroom-workspace/", "https://www.crunchyroll.com/pt-br/", "https://www.correios.com.br/", "https://www.magazineluiza.com.br/",
    "https://www.casasbahia.com.br/", "https://www.reclameaqui.com.br/", "https://www.zoom.com/pt", "https://www.oi.com.br/", "https://www.claro.com.br/", "https://www.tim.com.br/pe", "https://www.tim.com.br/", "https://vivo.com.br/para-voce",
    "https://vivo.com.br/", "https://www.ifood.com.br/", "https://www.cittamobi.com.br/", "https://www.decolar.com/", "https://www.airbnb.com.br/", "https://veja.abril.com.br/", "https://assine.abril.com.br/", "https://www.cnnbrasil.com.br/",
    "https://www.tudogostoso.com.br/", "https://store.steampowered.com/", "https://store.epicgames.com/", "https://www.nintendo.com/", "https://www.youtube.com/"
}

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_email():
    while True:
        email = input("Digite seu email: (Ex: usuario@gmail.com) ").strip().lower()
        erros = []
        if "@" not in email:
            erros.append("faltando '@'")
        if not re.search(r"\.(com|org|br)$", email):
            erros.append("faltando ou domínio inválido (.com, .org, .br)")
        if not re.search(r"@(gmail|hotmail|outlook)\.com", email):
            erros.append("provedor de domínio inválido (gmail, hotmail, outlook)")
        
        if not erros:
            return email
        print(f"Email inválido: {', '.join(erros)}")

def validar_senha():
    while True:
        senha = input("Digite sua senha (Ex: Senha123): ").strip()
        erros = []
        if len(senha) < 8:
            erros.append("precisa ter pelo menos 8 caracteres")
        if not re.search(r"[A-Z]", senha):
            erros.append("precisa conter pelo menos uma letra maiúscula")
        if not re.search(r"[0-9]", senha):
            erros.append("precisa conter pelo menos um número")
        
        if erros:
            print(f"Senha inválida: {', '.join(erros)}")
            continue

        confirmar_senha = input("Confirme sua senha: ").strip()
        if confirmar_senha == senha:
            return senha
        else:
            print("As senhas não coincidem.")

def validar_url():
    while True:
        url = input("Copie e cole uma URL do seu navegador ou digite no formato 'https://www.google.com.br/': ").strip().lower()
        
        # Compara diretamente com a lista de URLs conhecidas
        if url in urls:
            print("✅ URL válida e está presente na lista de URLs seguras.")
            return url
        else:
            print("❌ URL inválida: Não consta na lista de URLs seguras.")
            print(f"Você digitou: {url}")
            print("Tente novamente ou verifique a URL inserida.")


def validar_telefone():
    while True:
        telefone = input("Digite um número de telefone (Ex: (DDD) 9 1234-5678 ou similar): ").strip()
        telefone_limpo = re.sub(r"\D", "", telefone)  # Remove caracteres não numéricos
        if len(telefone_limpo) > 15:
            print("Número inválido. Deve conter no máximo 15 dígitos.")
            continue

        spam_palavras = [
            ("0303", "canal de vendas"), ("9090", "chamada a cobrar"),
            ("0555", "possível spam"), ("05555", "possível spam")
        ]

        for prefixo, descricao in spam_palavras:
            if telefone_limpo.startswith(prefixo):
                print(f"Número marcado como {descricao}.")
                return

        ddds = {
            "81": "PE", "87": "PE", "82": "AL", "71": "BA", "72": "BA",
            "73": "BA", "74": "BA", "75": "BA", "76": "BA", "77": "BA",
            "85": "CE", "88": "CE", "98": "MA", "99": "MA", "83": "PB",
            "86": "PI", "89": "PI", "84": "RN", "79": "SE", "61": "DF",
            "62": "GO", "64": "GO", "65": "MT", "66": "MT", "67": "MS",
            "27": "ES", "28": "ES", "31": "MG", "32": "MG", "33": "MG",
            "34": "MG", "35": "MG", "36": "MG", "37": "MG", "38": "MG",
            "21": "RJ", "22": "RJ", "24": "RJ", "11": "SP", "12": "SP",
            "13": "SP", "14": "SP", "15": "SP", "16": "SP", "17": "SP",
            "18": "SP", "19": "SP", "41": "PN", "42": "PN", "43": "PN",
            "44": "PN", "45": "PN", "46": "PN", "51": "RS", "52": "RS",
            "53": "RS", "54": "RS", "55": "RS", "47": "SC", "48": "SC",
            "49": "SC", "68": "AC", "96": "AP", "92": "AM", "97": "AM",
            "91": "PA", "93": "PA", "94": "PA", "69": "RO", "95": "RR",
            "63": "TO"
        }
        ddd = telefone_limpo[:2]
        if ddd in ddds:
            print(f"Número pertence a {ddds[ddd]}.")
            return
        print("Formato de número inválido.")

def menu_principal():
    while True:
        limpar_terminal()
        print("\nMenu Principal:")
        print("1. Cadastrar Email e Senha")
        print("2. Validar URL")
        print("3. Validar Número de Telefone")
        print("4. Mostrar Cadastro")
        print("5. Atualizar Cadastro")
        print("6. Excluir Cadastro")
        escolha = input("Escolha uma opção: ").strip()
        
        if escolha == "1":
            limpar_terminal()
            email = validar_email()
            senha = validar_senha()
            dados_usuarios[email] = senha
            print("Cadastro realizado com sucesso.")
            input("Pressione Enter para continuar...")

        elif escolha == "2":
            limpar_terminal()
            validar_url()
            input("Pressione Enter para continuar...")

        elif escolha == "3":
            limpar_terminal()
            validar_telefone()
            input("Pressione Enter para continuar...")

        elif escolha == "4":
            limpar_terminal()
            if not dados_usuarios:
                print("Não há nenhum registro ainda.")
            else:
                for email, senha in dados_usuarios.items():
                    print(f"Email: {email}, Senha: {'*' * len(senha)}")
                    mostrar = input("Deseja ver a senha cadastrada? (s/n): ").strip().lower()
                    if mostrar == "s":
                        print(f"Senha cadastrada: {senha}")
            input("Pressione Enter para continuar...")

        elif escolha == "5":
            limpar_terminal()
            dados_usuarios.clear()
            print("Cadastro excluído. Vamos criar um novo cadastro.")
            email = validar_email()
            senha = validar_senha()
            dados_usuarios[email] = senha
            print("Cadastro atualizado com sucesso.")
            input("Pressione Enter para continuar...")

        elif escolha == "6":
            limpar_terminal()
            dados_usuarios.clear()
            print("Todos os cadastros foram atualizados.")
            input("Pressione Enter para continuar...")

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()
