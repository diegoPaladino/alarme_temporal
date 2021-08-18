# ocr-pdf-python
import PyPDF2

arquivo = r"C:\Users\diego\OneDrive\Desktop\teste-leitura-excel-python\JA211-201830050-GERALD_LEVI_DE_LIMA_SANTOS.pdf"

lerPdf = PyPDF2.PdfFileReader(arquivo)

pagina = lerPdf.getPage(0)
conteudo = pagina.extractText()

print(conteudo)