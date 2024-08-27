import http.client
import json


def fetch_data(api_url):
    # Function to fetch data from API
    conn = http.client.HTTPSConnection("apex.oracle.com")
    conn.request("GET", api_url)
    response = conn.getresponse()

    if response.status == 200:
        # If the response status is 200 (OK), parse and return the data
        data = response.read()
        return json.loads(data.decode('utf-8'))
    else:
        # If the response status is not 200, print an error message and return None
        print(f"Failed to fetch data from API. Status: {response.status}")
        return None


def customer_functionality():
    # Function to handle customer functionality

    # Input discount code
    discount_code = input("Enter your discount code (or 'NONE' if not applicable): ").upper()

    # Fetching customer data
    customer_id = input("Enter your customer ID: ")

    # Connect to the customer API and retrieve customer data
    customer_api = f"https://apex.oracle.com/pls/apex/ifs354_group/test/luxe_customer?CUSTOMER_ID={customer_id}"
    customer_data = fetch_data(customer_api)

    if customer_data and "items" in customer_data:
        # Check if customer data is retrieved successfully

        print("Connection successful!")

        # Extract the discount code associated with the customer, use upper to make all inputted uppercase.
        customer_discount_code = customer_data["items"][0]["discount_code"].upper()

        # Check if discount code is "NONE" or matches the provided discount code
        if discount_code == "NONE" or discount_code == customer_discount_code:
            print("Discount code is correct.")

            # Calculate order price before discount
            order_price_before_discount = customer_data["items"][0]["order_price"]
            print(f"Order Price (before discount): R{order_price_before_discount}")

            # Calculate shipping cost
            if order_price_before_discount > 500:
                shipping_cost = 0  # Free shipping for orders over R500
            else:
                shipping_cost = 60  # R10 shipping cost for orders under R500
            print(f"Shipping Cost: R{shipping_cost}")

            # Calculate order price after discount (if applicable)
            if discount_code != "NONE":
                discounted_price = order_price_before_discount * 0.85  # 15% discount
                total_price = discounted_price + shipping_cost
                print(f"Order Price (after 15% discount and shipping): R{total_price}")
            else:
                total_price = order_price_before_discount + shipping_cost
                print(f"Order Price (after shipping, no discount applied): R{total_price}")

            # Add order status under order details
            order_status = customer_data["items"][0]["order_status"]
            print(f"Order Status: {order_status}")

        else:
            print("Invalid discount code. Please try again.")

    else:
        print("No customer data found.")


# End of customer functionality

customer_functionality()