import requests

class BooksApiClient:
    '''
    1. Folosind endpoint-ul de authentication, genereaza un access token
    (fa asta in constructor, client name si email ar trebui sa fie atribute).
    '''
    # constructorul
    def __init__(self, client, email):
        self.client = client
        self.email = email
        # crearea tokenului care o salvam in self.token
        self.token = self._generate_token()
        # functia token-ului care va fi protected _
    def _generate_token(self):
        json_data = {
                "clientName": self.client,  # datele sunt luate din body de la API
                "clientEmail": self.email
        }
        response = requests.post(url="https://simple-books-api.glitch.me/api-clients/", json=json_data)
        print(response.json())
        return response.json()["accessToken"] # facem referire la token ca sa accesam valoarea lui

    '''
    2. Adaugă o metoda prin care poți vedea toate comenzile.
    '''


    def view_all_orders(self):
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get("https://simple-books-api.glitch.me/orders", headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    '''
    3. Adaugă o metoda prin care poți vedea toate cărțile.
    '''

    def view_all_books(self):
        response = requests.get("https://simple-books-api.glitch.me/books")
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
    '''
    4. Adaugă o metoda prin care poți posta o comanda.
    '''

    def post_order(self, book_id, customer_name):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        json_data = {
            "bookId": book_id,
            "customerName": customer_name
        }
        response = requests.post(url="https://simple-books-api.glitch.me/orders", json=json_data, headers=headers)

        if response.status_code == 201:  # Codul 201 indica faptul ca resursa a fost creata cu succes
            return response.json()
        else:
            response.raise_for_status()
    '''
    5. Adaugă o metoda prin care poți șterge o comanda.
    '''

    def delete_order(self, order_id):
        headers = {
            "Authorization": f"Bearer {self.token}"
        }

        response = requests.delete(url=f"https://simple-books-api.glitch.me/orders/{order_id}", headers=headers)

        if response.status_code == 204:  # Codul 204 indică faptul că cererea a fost procesată cu succes, dar nu există conținut de returnat
            return "Order deleted successfully."
        else:
            response.raise_for_status()

user = BooksApiClient("Marius5", "marius.selegean5@example.com") # se schimba userul si emailul de ori de cate ori se ruleaza un api care necesita token.
print(user.token)
orders = user.view_all_orders()
print(orders)

all_books = user.view_all_books()
print(all_books)

order_response = user.post_order(book_id=1, customer_name="Marius")
print(order_response)

delete_response = user.delete_order(order_id=12345)  # se inlocuieste 12345 cu ID-ul real al comenzii
print(delete_response)

