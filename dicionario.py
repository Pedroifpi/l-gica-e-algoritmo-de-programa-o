def incluir_contato(n):
    lista=[]
    for i in range(n):
        nome=input("degite o nome do contato:")
        telefone=input("degite o telefone do contato:")
        email=input("degite o email do contato:")
        contatos={"nome":nome,"telefone":telefone,"email":email}
        lista.append(contatos)
    return lista
def main():
    n=int(input("degite o numero de contatos que deseja incluir:"))
    contatos=incluir_contato(n)
    for nomes in contatos:
        print("nome:",nomes.get("nome"))
        print("telefone:",nomes.get("telefone"))
        print("email:",nomes.get("email"))
        
if __name__=="__main__":
 main()