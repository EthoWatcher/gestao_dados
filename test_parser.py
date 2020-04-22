from EW_preprocess_pkg import xml2json as pa
import io


def test_biblioteca():
    f = open("./examples/1e3z1h4.etoxml", "rb") 
    parser = pa.Parse_XML(f)


# def test_biblioteca_criando_arquivo_texto():
#     f = io.StringIO("some initial text data")
#     parser = pa.Parse_XML(f)