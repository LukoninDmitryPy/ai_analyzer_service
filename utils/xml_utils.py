from fastapi import UploadFile
import xml.etree.ElementTree as ET


async def get_sales(file_contents: UploadFile, arg_find: str=None, arg_findall: str=None) -> list[ET.Element]:
    try:
        date = ET.fromstring(file_contents).attrib['date']
    except ET.ParseError as e:
        raise Exception(f"Error parsing XML on date: {e}")
    try:
        sales = ET.fromstring(file_contents).findall('products/product')
    except ET.ParseError as e:
        raise Exception(f"Error parsing XML on body: {e}")
    products=[]
    try:
        for sale in sales:
            product = {
                'id': sale.find('id').text,
                'name': sale.find('name').text,
                'quantity': int(sale.find('quantity').text),
                'price': float(sale.find('price').text),
                'category': sale.find('category').text,
                'date': date
            }
            products.append(product)
        return products
    except Exception as e:
        raise Exception(f"Error on create list of products: {e}")