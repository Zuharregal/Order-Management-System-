import http.client
import json


def fetch_data(api_url):
    conn = http.client.HTTPSConnection("apex.oracle.com")
    conn.request("GET", api_url)
    response = conn.getresponse()

    if response.status == 200:
        data = response.read()
        return json.loads(data.decode('utf-8'))
    else:
        print(f"Failed to fetch data from API. Status: {response.status}")
        return None


def staff_functionality():
    # Fetching all orders data
    all_orders_api = "https://apex.oracle.com/pls/apex/ifs354_group/test/luxe_orders/"
    all_orders_data = fetch_data(all_orders_api)

    if all_orders_data and "items" in all_orders_data:
        print("Connection successful!")
        print("Orders:")

        # Displaying order details for each order
        for order in all_orders_data["items"]:
            order_id = order.get("order_id")
            order_date = order.get("order_date")
            order_price = order.get("order_price")
            customer_id = order.get("customer_id")
            print(
                f"Order ID: {order_id}, Order Date: {order_date}, Order Price: {order_price}, Customer ID: {customer_id}")

        print()  # Empty line for better readability between orders
    else:
        print("No order data found.")


# End of staff functionality

staff_functionality()
