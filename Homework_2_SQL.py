import psycopg2 
conn = psycopg2.connect(dbname="edu_SQL", user="postgres", password="kfvths", host="127.0.0.1", port="5432")  
print("Подключение установлено")
cursor = conn.cursor()
cursor.execute('''
        	CREATE TABLE IF NOT EXISTS customers (
            	customers_id SERIAL PRIMARY KEY,
            	name VARCHAR(50),
            	email VARCHAR(50)
        	);
    	''')

cursor.execute('''
        	CREATE TABLE IF NOT EXISTS orders (
            	orders_id SERIAL PRIMARY KEY,
            	customer_id  INT,
            	order_date DATE,
             CONSTRAINT FK_orders_customer FOREIGN KEY(customer_id) REFERENCES customers(customers_id)
        	);
    	''')

cursor.execute('''
        	CREATE TABLE IF NOT EXISTS order_items (
            	items_id SERIAL PRIMARY KEY,
                order_id INT,
            	product_name  varchar,
            	quantity INT,
                price FLOAT,
             CONSTRAINT FK_order_items_customer FOREIGN KEY(order_id) REFERENCES orders(orders_id)
        	);
    	''')
#Добавление покупателей
cursor.execute('''
               INSERT INTO customers(name, email)
               VALUES 
                    (
	                    ('Иван Иванов'), ('cust@order.com')
                    )               
               ''')

cursor.execute('''
               INSERT INTO customers(name, email)
               VALUES 
                    (
	                    ('Алексей Жилов'), ('alek@order.com')
                    )               
               ''')

cursor.execute('''
               INSERT INTO customers(name, email)
               VALUES 
                    (
	                    ('Андрей Толстой'), ('and@order.com')
                    )               
               ''')
#Вставка заказов
cursor.execute('''
                INSERT INTO orders(customer_id, order_date)
                VALUES (6, '2024/09/25')               
               ''')

cursor.execute('''
                INSERT INTO orders(customer_id, order_date)
                VALUES (1, '2025/10/25')               
               ''')
#Дописать запросы на вставку в orders

#Вставка товаров
cursor.execute('''
                INSERT INTO order_items (order_id, product_name, quantity, price)
                VALUES (1, 'Tomato', 10, 10.50)               
               ''')
#Дописать запросы на вставку в order_items


cursor.execute('''
               SELECT orders_id, order_date
               FROM orders
               JOIN customers ON customers.customers_id = orders.customer_id
               WHERE customers.name = 'Иван Иванов'
''')
rows = cursor.fetchall()
print(rows)         
cursor.close()
conn.close()

