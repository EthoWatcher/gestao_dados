import xmltodict

def parser_xml_file_2_dict(file_path):
    with open(file_path) as fd:
        doc = xmltodict.parse(fd.read())
    
    return doc

def parser_xml_file_as_text(file_path):
    with open(file_path) as fd:
        doc = fd.read()
    return doc


def parser_xml_text_2_dict(text):
    doc = xmltodict.parse(text)
    return doc
