from program_files.passive.pdf.base import PDFLoaderBase
from program_files.passive.pdf.loader import PypdfLoader


class FakePage:

    def __init__(self, text: str | None):
        self._text = text

    def extract_text(self):
        return self._text


class FakeReader:

    def __init__(self):
        self.pages = [
            FakePage("page1"),
            FakePage("page2")
        ]


# ====== PDFLoaderBase.load_pdf() ======

def test_load_pdf(monkeypatch):

    monkeypatch.setattr(
        "pathlib.Path.exists",
        lambda self: True
    )

    monkeypatch.setattr(
        "pdf.pypdf_loader.PdfReader",
        lambda _: FakeReader()
    )

    pdf_loader: PDFLoaderBase = PypdfLoader()

    docs = pdf_loader.load_pdf()

    assert len(docs) == 2

    assert docs[0].page == 1
    assert docs[0].text == "page1"

    assert docs[1].page == 2
    assert docs[1].text == "page2"


def test_load_pdf_empty_text(monkeypatch):

    class EmptyReader:

        pages = [
            FakePage(None)
        ]

    monkeypatch.setattr(
        "pdf.pypdf_loader.PdfReader",
        lambda _: EmptyReader()
    )

    pdf_loader: PDFLoaderBase = PypdfLoader()

    docs = pdf_loader.load_pdf()

    assert len(docs) == 1
    assert docs[0].text == ""


def test_load_pdf_source_is_str(monkeypatch):

    monkeypatch.setattr(
        "pdf.pypdf_loader.PdfReader",
        lambda _: FakeReader()
    )

    pdf_loader: PDFLoaderBase = PypdfLoader()

    docs = pdf_loader.load_pdf()

    assert isinstance(docs[0].source, str)

print(PypdfLoader)
print(type(PypdfLoader))
