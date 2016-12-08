SCC-0661 Multimídia e Hipermídia
Trabalho 2: Modelagem de um sistema de Imobiliária

-----------------------------------------
O objetivo deste trabalho é realizar toda modelagem do sistema utilizando linguagens declarativas:
XML, XML Schema, XSLT e RSS.
Parser com uso de Python. Detalhes do projeto no arquivo pdf

-----------------------------------------
Alunos:
Leandro Bellini
Pedro Fini
Thales Lopes
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


