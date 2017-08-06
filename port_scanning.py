import os
print("+--------------------------------------+")
print(" BEM VINDO AO IF-PORTSCANNING >>>> v1.0")
print("+--------------------------------------+")
print(" >>Este programa foi feito PARA UM TRABALHO")
print(" >>Qualquer uso indevido não é de responsabilidade dos autores.")
print("----------------------------------------")
print("Exemplo de padrões para os IPS: 127.0.0.1-254")
ips_para_scannear = input("Digite a faixa de IPS para Escanear: ")

p = os.popen('C:\\Users\\marci\\Desktop\\nmap\\nmap\\nmap.exe nmap -F '+ips_para_scannear,"r")
while 1:
    line = p.readline()
    if not line: break
    print(line)


