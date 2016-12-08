#usado para setar caracteres especiais
import sys, os
reload(sys)
sys.setdefaultencoding("utf-8")

#bibliotecas xml do python
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.etree import ElementTree
from xml.dom import minidom

#estrutura basica para validar o modelo no txt, que depois sera validado no schema tmb(xsd)
class Validador():
	finalidade = None
	dimensoes = None
	areaConstruida = None
	terreno = None
	codigoUnico = None 
	endereco = None
	descricao  = None
	contato  = None
	valor = None
	financiamento = None 
	iptu = None
	apartamento = None 
	condominio  = None
	venda = None
	aluguel = None

	def __init__(self):
		self.zerar()

	def zerar(self):
		self.finalidade = 0
		self.dimensoes = 0
		self.area = 0
		self.construcao = 0
		self.terreno = 0
		self.endereco = 0
		self.descricao = 0
		self.contato = 0
		self.valor = 0
		self.financiamento = 0
		self.iptu = 0
		self.apartamento = 0
		self.condominio = 0
		self.venda = 0
		self.aluguel = 0

	def validarDados(self):
		#Vejo campos que TODO arquivo txt deve ter para seguir as regras do modelo
		if not (self.finalidade and self.dimensoes and self.endereco and self.descricao and self.contato):
			print "\tAtencao: Falta dados basicos do modelo!!!"
			#python nao tem o famoso switch/case :/
			if not self.finalidade:
				print "\tCampo <Finalidade> nao encontrado! XML nao sera validado pelo XML Schema!!"
			if not self.dimensoes:
				print "\tCampo <Dimensao> nao encontrado! XML nao sera validado pelo XML Schema!!"
			if not self.endereco:
				print "\tCampo <Endereco> nao encontrado! XML nao sera validado pelo XML Schema!!"
			if not self.descricao:
				print "\tCampo <Descricao> nao encontrado! XML nao sera validado pelo XML Schema!!"
			if not self.contato:
				print "\tCampo <Contato> nao encontrado! XML nao sera validado pelo XML Schema!!"

		#Terrenos soh podem estar a venda
		if self.terreno:
			if not self.venda:
				print "\tAtencao!!! Um terreno tem que estar em VENDA!!! Observe o arquivo de entrada"

		#toda venda deve acompanhar valor e financiamento
		if self.venda:
			if not self.valor:
				print "\tCampo <Valor> nao encontrado para o caso de uma venda! Verifique!!"
			if not self.financiamento:
				print "\tCampo <Financiamento> nao encontrado para o caso de uma venda! Verifique!!"

		#todo aluguel deve ter os campos valor, IPTU! No caso de apartamentos, deve ter o campo condominio
		if self.aluguel:
			if not self.valor:
				print "\tCampo <Valor> nao encontrado para o caso de uma aluguel! Verifique!!"
			if not self.iptu:
				print "\tCampo <IPTU> nao encontrado para o caso de uma aluguel! Verifique!!"
			if self.apartamento:
				if not self.condominio:
					print "\tCampo <Condominio> nao encontrado para o caso de uma aluguel de apartamento! Verifique!!"



#imprime a estrutura do XML formatada
def stringEstruturada(elem):
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

#faz a leitura principal do txt
def readBD(arquivo, saida):
	print "--> Criacao do arquivo XML a partir do arquivo "+arquivo

	validar = Validador()

	try:
		with open(arquivo) as fp:
			raiz = Element('Raiz')
			item = None
			validar.zerar()

			for line in fp:
				if "Codigo" in line:
					#Novo item! Tenho que gravar ultimo item
					if item is not None:
						validar.validarDados() #Valida dados do ultimo item que sera adicionado

					item = SubElement(raiz, 'Item')
					validar.zerar()

				if "Finalidade" in line:
					validar.finalidade = 1

				if "terreno" in line:
					validar.terreno = 1

				if "venda" in line:
					validar.venda = 1

				if "Dimensao" in line:
					validar.dimensoes = 1

				if "Area" in line:
					validar.area = 1

				if "Construcao" in line:
					validar.construcao = 1

				if "Endereco" in line:
					validar.endereco = 1

				if "Descricao" in line:
					validar.descricao = 1

				if "Contato" in line:
					validar.contato = 1

				if "Valor" in line:
					validar.valor = 1

				if "Financiamento" in line:
					validar.financiamento = 1

				if "IPTU" in line:
					validar.iptu = 1

				if "apartamento" in line:
					validar.apartamento = 1

				if "Condominio" in line:
					validar.condominio = 1

				if "aluguel" in line:
					validar.aluguel = 1


				#vou separar a string chave:valor
				try:
					dados = line.split(':')
					key = dados[0].strip()  
					value = dados[1].strip()

					child = SubElement(item, key)
					child.text = value
				except:
					print "Error: Problemas ao fazer o parser! Verifique propriedade:valor nos campos do arquivo de entrada"
					sys.exit(1)

			try:
				validar.validarDados()

				#gravo XML final
				destino = open(saida, 'w+')
				destino.write(stringEstruturada(raiz))
				destino.close()
				fp.close()
			except:
				print "Error: Problemas ao salvar arquivo de destino xml"
				sys.exit(1)

			print "--> Arquivo "+saida+" criado com sucesso"
	except:
		print "Error: Problemas ao ler o arquivo de entrada " + arquivo
		sys.exit(1)



	return;

if len(sys.argv) < 3:
	print "Error: Use --> python entrada.txt destino.xml"
	sys.exit(-1)

entrada = sys.argv[1]
destino = sys.argv[2]

#lendo o txt e criando o arquivo xml
readBD(entrada, destino)

#validando o xml com o xmllint e o xsd
cmd = os.popen('xmllint --noout --schema schema.xsd destino.xml')
