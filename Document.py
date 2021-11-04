from abc import ABC
from Reader.DOCXReader import DOCXReader
from Reader.PDFReader import PDFReader
from Database.Connection import Connection


class Document(ABC):
    @staticmethod
    def __createDocuments(fileObject):
        item = {'Title': fileObject.getTitle(),
                'Author': fileObject.getAuthor(),
                'Content': fileObject.getContent(),
                'Content-type': fileObject.getType(),
                'Created-time': fileObject.getDate()}
        return item

    @classmethod
    def __pdf_push(cls, dbname, folder):
        pdf_data = PDFReader.getPDFList(folder)
        pdf_docs = list(
            map(lambda data: cls.__createDocuments(data), pdf_data))
        if(pdf_docs != []):
            collection_name = dbname[folder]
            collection_name.insert_many(pdf_docs)
        PDFReader.clean(pdf_data)

    @classmethod
    def __docx_push(cls, dbname, folder):
        docx_data = DOCXReader.getDOCXList(folder)
        docx_docs = list(
            map(lambda data: cls.__createDocuments(data), docx_data))
        if(docx_docs != []):
            collection_name = dbname[folder]
            collection_name.insert_many(docx_docs)
        DOCXReader.clean(docx_data)

    @classmethod
    def push(cls, dbname, collection):
        cls.__pdf_push(dbname, collection)
        cls.__docx_push(dbname, collection)
