'''4 – Solicite ao usuário um superpoder entre três opções: “força”, “velocidade” ou “voo”.
Use estruturas de decisão para exibir uma frase que diga qual super-herói você seria com
base na escolha:
• Se escolher “força”: exiba “Você seria o Hulk!”;
• Se escolher “velocidade”: exiba “Você seria o Flash!”;
• Se escolher “voo”: exiba “Você seria o Superman!”.'''

superpoder = input('Qual superpoder você gostaria de ter: força, velocidade ou voo?')
if superpoder == 'força':
    print ('Você seria o Hulk!')
if superpoder == 'velocidade':
    print ('Você seria o Flash!')
if superpoder == 'voo':
    print ('Você seria o Superman!')