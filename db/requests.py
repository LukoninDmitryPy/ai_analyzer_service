from db.models import Product, Answer
from db.connection import Session


session = Session()

def add_products(sales:list[dict]):
    products = []
    for sale in sales:
        product = Product(
            product_id=int(sale['id']),
            name=sale['name'],
            quantity=int(sale['quantity']),
            price=float(sale['price']),
            category=sale['category'],
            date=sale['date']
        )
        products.append(product)

    session.add_all(products)
    session.commit()

def add_answer(result):
    
    answer = Answer(
        answer=str(result),
    )

    session.add(answer)
    session.commit()
