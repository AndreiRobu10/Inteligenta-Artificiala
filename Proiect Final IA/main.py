from bs4 import BeautifulSoup
import requests

print("Cautare Emag")
print("Introduceti brandul pe care il preferati(optional): ")
product_brand = input(">>>")
print("Introduceti pretul maxim: ")
product_max_price = float(input(">>>"))
print("Incepe cautarea...")

def gaseste_produse():
    html_text = requests.get('https://www.emag.ro/telefoane-mobile/c?ref=hp_menu_quick-nav_1_16&type=category').text
    soup = BeautifulSoup(html_text, 'lxml')
    products = soup.find_all('div', class_ = 'card-item card-standard js-product-data')
    for i, product in enumerate(products):
        details = product.find('div', class_ = 'pad-hrz-xs')
        product_name = details.find('h2', class_ = 'card-v2-title-wrapper').text
        product_price = product.find('p', class_ = 'product-new-price').text.replace(' Lei', '')
        product_price = product_price.replace('.','')
        product_price = product_price.replace(',','.')
        product_price = product_price.replace('de la ','')
        product_link = details.h2.a['href']
        if product_brand in product_name and product_max_price > float(product_price):
            with open(f'Extra/Produsul {i}.txt', 'w') as f:
                f.write(f"Numele Produsului: {product_name.strip()} \n")
                f.write(f"Pretul Produsului: {product_price.strip()} Lei \n")
                f.write(f"Link: {product_link.strip()} \n")
                print(f"Produsul {i} a fost salvat.")

if __name__ == '__main__':
    gaseste_produse()