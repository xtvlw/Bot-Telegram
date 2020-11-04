from os import system, listdir
MangaName = "Koe-no-Katachi"

class decode:
    def decoder(self, MangaName):
        dir = listdir("/home/manjaro/Modelos/") #list all archives and folders in this locol
        for i in range(len(dir)):
            system(f"unzip /home/manjaro/Modelos/{dir[i]}") #unzip all archives to a folder
            dc.mover(MangaName, i) #move the archives to their respectives folders
            pt.ImgDetect(i, MangaName) #detect the image format to converter in PDF

    def mover(self, MangaName, capter):
        system(f"mkdir -p /home/manjaro/Downloads/books/{MangaName} && \
        mv /home/manjaro/Documentos/python/bot-telegram/content /home/manjaro/Downloads/books/{MangaName} && \
        cd /home/manjaro/Downloads/books/{MangaName} && mv content capitulo-{capter}") #change the name of the folder to the respective capter

class PDFtransformer:
    def ImgDetect(self, i, MangaName):
        type = listdir(f"/home/manjaro/Downloads/books/{MangaName}/capitulo-{i}") #get this local directory to verify the image format, to converter in a pdf file
        typeImage = type[0][type[0].find('.'):] #get the final of the name of the archive, EX: teste.png => .png
        pt.transformer(f"capitulo-{i}", f"/home/manjaro/Downloads/books/", f"{MangaName}", str(typeImage)) #send informations to converte the images in a pdf file

    def transformer(self, FolderName, diretory, MangaName, ImgFormat):
        system(f"convert {diretory}{MangaName}/{FolderName}/*{ImgFormat} {FolderName}-pdf.pdf") #convert all the images in a directory in a single pdf file
        system(f"mkdir -p /home/manjaro/Downloads/books/{MangaName}PDF && \
        mv /home/manjaro/Documentos/python/bot-telegram/{FolderName}-pdf.pdf /home/manjaro/Downloads/books/{MangaName}PDF/")#move all the PDFs to the correcdt directory

    def JoinPdf(self, MangaName):
        system(f"pdftk /home/manjaro/Downloads/books/{MangaName}PDF/*.pdf cat output {MangaName}CompletePDF.pdf \
        && mv /home/manjaro/Documentos/python/bot-telegram/{MangaName}CompletePDF.pdf /home/manjaro/Downloads/books/") #move the bigger PDF to the correct folder


dc = decode()
pt = PDFtransformer()

dc.decoder(MangaName) #strat the unzip process
pt.JoinPdf(MangaName) #start the process to make a bigger PDF
