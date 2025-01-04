from fastapi import HTTPException, Request, Response
from lxml import etree
import os

BASE_DIR = "webdav_storage"

def propfind(path: str, request: Request):
    full_path = os.path.join(BASE_DIR, path)
    if not os.path.exists(full_path):
        raise HTTPException(status_code=404, detail="Resource not found")

    # Создаем XML-ответ
    root = etree.Element("d:multistatus", xmlns="DAV:")
    response = etree.SubElement(root, "d:response")
    href = etree.SubElement(response, "d:href")
    href.text = f"/{path}"
    propstat = etree.SubElement(response, "d:propstat")
    prop = etree.SubElement(propstat, "d:prop")
    etree.SubElement(prop, "d:getlastmodified")
    etree.SubElement(prop, "d:getcontentlength")
    etree.SubElement(prop, "d:resourcetype")
    status = etree.SubElement(propstat, "d:status")
    status.text = "HTTP/1.1 200 OK"

    xml_response = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding="UTF-8")
    return Response(content=xml_response, media_type="application/xml")