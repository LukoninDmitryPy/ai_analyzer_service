from collections import Counter
import requests
import os

from config import OPENAI_KEY, OPENAI_URL


def create_body(products:list[dict]) -> str:
    date = products[0]['date']
    total_revenue = 0
    all_products = []
    categories = []
    for i in products:
        total_revenue += i['price']
        all_products.append(i['name'])
        if i['category'] not in categories:
            categories.append(i['category'])
        
    count = Counter(all_products)
    top_products = count.most_common(3)
    
    body= f"""Проанализируй данные о продажах за {date}:
1. Общая выручка: {total_revenue}
2. Топ-3 товара по продажам: {str(top_products)}
3. Распределение по категориям: {str(categories)}

Составь краткий аналитический отчет с выводами и рекомендациями."""
    return body

def send_request_to_ai(products):
    prompt = create_body(products)
    params = {
        "prompt": prompt,
        "max_tokens": 256,
        "temperature": 0.7,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENAI_KEY')}",
        "Content-Type": "application/json"
    }
    response = requests.post(os.getenv('OPENAI_URL'), headers=headers, json=params)

    if response.status_code == 200:
        answer = response.json()["choices"][0]["text"]
        return answer
    else:
        raise Exception(f"Error while send to ai: {response.status_code}")
