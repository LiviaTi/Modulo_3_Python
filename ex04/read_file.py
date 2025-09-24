import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print("Erro: Arquivo não encontrado.")
        except IsADirectoryError:
            print("Erro: O argumento enviado é um diretório.")
        except Exception as e:
            print(f"Erro inesperado: {type(e).__name__}")
    else:
        print("Erro: Por favor, forneça o caminho do arquivo como argumento.")
