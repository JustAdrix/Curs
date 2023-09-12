import requests
import time
import json
import os

TOKEN_STORAGE = "token_storage.json"
TOKEN_EXPIRY_TIME = 7 * 24 * 60 * 60  # 7 days in seconds


class BooksApiClient:
    def __init__(self, client):
        self.client = client
        self.email = f"{client}@example.com"
        self.token = self._get_or_generate_token()

    def _get_or_generate_token(self):
        if os.path.exists(TOKEN_STORAGE):
            with open(TOKEN_STORAGE, 'r') as f:
                data = json.load(f)
                token_expiry_time = data['expiry_time']
                if time.time() < token_expiry_time:
                    return data['token']

        # If we reached here, either token is expired or doesn't exist
        token = self._generate_new_token()
        expiry_time = time.time() + TOKEN_EXPIRY_TIME
        with open(TOKEN_STORAGE, 'w') as f:
            json.dump({"token": token, "expiry_time": expiry_time}, f)

        return token

    def _generate_new_token(self):
        json_data = {
            "clientName": self.client,
            "clientEmail": self.email
        }
        response = requests.post(url="https://simple-books-api.glitch.me/api-clients/", json=json_data)

        response_data = response.json()
        if "accessToken" in response_data:
            return response_data["accessToken"]
        else:
            raise Exception(response_data.get('error', 'Unknown error occurred while generating token'))

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

        if response.status_code == 201:  # Codul 201 indică faptul că resursa a fost creată cu succes
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


# Test
try:
    user = BooksApiClient("Marius")
    print(user.token)
    # rest of the operations...
except Exception as e:
    print(f"An error occurred: {e}")

user = BooksApiClient("Marius")
print(user.token)
orders = user.view_all_orders()
print(orders)

all_books = user.view_all_books()
print(all_books)

order_response = user.post_order(book_id=1, customer_name="Marius")
print(order_response)

#delete_response = user.delete_order(order_id=12345)  # Înlocuiți 12345 cu ID-ul real al comenzii
#print(delete_response)
