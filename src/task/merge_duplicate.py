

import datetime
import uuid
import mysql.connector

from task.get_duplicate import fetch_products_duplicate, group_products


def insert_duplicate_suggestions(mysql_config, product_groups):
    connection = mysql.connector.connect(**mysql_config)
    cursor = connection.cursor()
    for key, details in product_groups.items():
        product_id = details[0][0]
        title = key
        created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute("INSERT INTO product_duplicates (id, title, created_at) VALUES (%s, %s, %s)", (product_id,title, created_at))

        for detail in details:
            id = str(uuid.uuid4())
            main_product_id, duplicate_product_id, title, external_id = detail
            cursor.execute("SELECT COUNT(*) FROM product_duplicate_lists WHERE product_id = %s", (duplicate_product_id,))
            count = cursor.fetchone()[0]

            if count == 0:
                cursor.execute("INSERT INTO product_duplicate_lists (id, product_duplicate_id, product_id, external_id, created_at) VALUES (%s, %s, %s, %s, %s)",
                                (id, main_product_id, duplicate_product_id, external_id, created_at))

    connection.commit()
    cursor.close()
    connection.close()

def generate_merge_suggestions():
    mysql_config = {
        "host": "localhost",
        "user": "root",
        "password": "0341",
        "database": "baltini"
    }

    products = fetch_products_duplicate(mysql_config)
    product_groups = group_products(products)

    insert_duplicate_suggestions(mysql_config, product_groups)
    return
