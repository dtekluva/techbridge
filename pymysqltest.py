import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='',
                             db='shop',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
# # # TO ADD OR ALTER DATABASE
# try:
#     with connection.cursor() as cursor:
#         # Create a new record
#         sql = "INSERT INTO `members` (name, age, hobby) VALUES ('kunle', 15, 'code python')"

#         cursor.execute(sql)

#     # connection is not autocommit by default. So you must commit to save
#     # your changes.
#     connection.commit()

# finally:
    # connection.close()

# TO RETRIEVE FROM DATABASE
# try:
#     with connection.cursor() as cursor:
#         # Create a new record
#         sql = "SELECT * FROM members"

#         cursor.execute(sql)

#     data = cursor.fetchall()
    
#     for member in data:

#         print(member.get('name'))

# finally:
#     connection.close()

# TO RETRIEVE FROM DATABASE
try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = """
                    SELECT customer.name as `Customer name`, product.name as `product name`, purchase.qty, purchase.total_price, purchase.order_date FROM purchase
                    JOIN product
                    ON purchase.prod_id = product.id
                    JOIN customer 
                    ON customer.id = purchase.cust_id
            """

        cursor.execute(sql)

    data = cursor.fetchall()
    # print(data)
    
    for member in data:

        print(member)

finally:
    connection.close()