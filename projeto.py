import os
import re

dados_usuarios = {}
urls = {
    "ecommerce": {
        "https://www.mercadolivre.com.br/",
        "https://www.amazon.com.br/",
        "https://www.americanas.com.br/",
        "https://www.magazineluiza.com.br/",
        "https://www.casasbahia.com.br/",
        "https://shopee.com.br/"
    },
    "bancos": {
        "https://www.caixa.gov.br/",
        "https://www.santander.com.br/",
        "https://www.bb.com.br/",
        "https://nubank.com.br/"
    },
    "operadoras": {
        "https://www.oi.com.br/",
        "https://www.claro.com.br/",
        "https://www.tim.com.br/pe",
        "https://www.tim.com.br/",
        "https://vivo.com.br/para-voce",
        "https://vivo.com.br/"
    },
    "jogos": {
        "https://store.steampowered.com/",
        "https://store.epicgames.com/",
        "https://www.nintendo.com/",
        "https://www.crunchyroll.com/pt-br/"
    },
    "governo": {
        "https://www.gov.br/pt-br",
        "https://www.detran.pe.gov.br/",
        "https://servicos.compesa.com.br/",
        "https://www.neoenergia.com/"
    }
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
        for categoria, lista in urls.items():
            if url in lista:
                print(f"✅ URL válida e está presente na categoria: {categoria.capitalize()}.")
                return url
        print("❌ URL inválida: Não consta na lista de URLs seguras.")
        print(f"Você digitou: {url}")
        print("Tente novamente ou verifique a URL inserida.")

def validar_telefone():
    while True:
        telefone = input("Digite um número de telefone (Ex: (DDD) 9 1234-5678 ou similar): ").strip()
        telefone_limpo = re.sub(r"\D", "", telefone)
        if len(telefone_limpo) > 15:
            print("Número inválido. Deve conter no máximo 15 dígitos.")
            continue

        spam_palavras = [("0303", "canal de vendas"), ("0555", "possível spam")]

        for prefixo, descricao in spam_palavras:
            if telefone_limpo.startswith(prefixo):
                print(f"Número marcado como {descricao}.")
                return

        ddds = {
            "81": "PE", "87": "PE", "82": "AL", "71": "BA", "85": "CE",
            "98": "MA", "83": "PB", "86": "PI", "84": "RN", "79": "SE"
        }
        ddd = telefone_limpo[4:6] if telefone_limpo.startswith("9090") else telefone_limpo[:2]
        
        if telefone_limpo.startswith("9090"):
            if ddd in ddds:
                print(f"Número a cobrar do DDD {ddd}, localizado em {ddds[ddd]}.")
                return
            print("Número a cobrar, mas DDD inválido.")
            return
        elif ddd in ddds:
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
