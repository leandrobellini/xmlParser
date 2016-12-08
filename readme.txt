SCC-0661 Multimídia e Hipermídia
Trabalho 2: Modelagem de um sistema de Imobiliária

-----------------------------------------
Alunos:
Leandro Luis Bellini - 7572908
Pedro Henrique Fini - 7704985
Thales Lopes Correia da Silva - 7546742
-----------------------------------------


Uso do programa:
	python programa.py entrada.txt saida.xml


Exemplo:
	$python parser.py bd.txt destino.xml 


Obs: o programa já faz a validaçao com o XSD utilizando o arquivo padrao schema.xsd,
basta modoficiar a ultima linha do codigo para utilizar outros arquivos 


Para instalar o xmllint no ubuntu, use: 
	sudo apt-get install libxml2-utils


Para validar um arquivo XML a partir do schema, use:
	xmllint --noout --schema schema.xsd destino.xml


