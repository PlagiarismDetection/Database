from abc import ABC
from Reader.DOCXReader import DOCX, DOCXReader
from Reader.PDFReader import PDFReader
from Database.DatabaseConnection import DatabaseConnection


class PushData(ABC):
    def __init__(self, CONNECTION_STRING, collection_name):
        super().__init__()
        self.dbname = DatabaseConnection.connect(
            CONNECTION_STRING, collection_name)

    @staticmethod
    def createDocuments(fileObject):
        item = {'Title': fileObject.getTitle(),
                'Author': fileObject.getAuthor(),
                'Content': fileObject.getContent(),
                'Content-type': fileObject.getType(),
                'Created-time': fileObject.getDate()}
        return item

    @classmethod
    def pdf_push(cls, dbname, folder):
        pdf_data = PDFReader.getPDFList(folder)
        pdf_docs = list(map(lambda data: cls.createDocuments(data), pdf_data))
        if(pdf_docs != []):
            collection_name = dbname[folder]
            collection_name.insert_many(pdf_docs)
        PDFReader.clean(pdf_data)

    @classmethod
    def docx_push(cls, dbname, folder):
        docx_data = DOCXReader.getDOCXList(folder)
        docx_docs = list(
            map(lambda data: cls.createDocuments(data), docx_data))
        if(docx_docs != []):
            collection_name = dbname[folder]
            collection_name.insert_many(docx_docs)
        DOCXReader.clean(docx_data)

    def push(self, collection_eng, collection_vie):
        self.pdf_push(self.dbname, collection_eng)
        self.pdf_push(self.dbname, collection_vie)
        self.docx_push(self.dbname, collection_eng)
        self.docx_push(self.dbname, collection_vie)
