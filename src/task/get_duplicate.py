from collections import defaultdict
import mysql.connector

def fetch_products_duplicate(mysql_config):
    query = """
            SELECT p1.id AS main_product_id,
                p2.id AS duplicate_product_id,
                concat_ws('-',p1.title, p1.category, p1.gender, p1.id) AS title,
                p1.external_id,
                p1.description
            FROM products p1
            INNER JOIN products p2 ON
            SUBSTRING_INDEX(p1.tags, 'ProductID: ', -1) = SUBSTRING_INDEX(p2.tags, 'ProductID: ', -1) AND
            p1.gender = p2.gender AND
            p1.category = p2.category AND
            p1.id != p2.id
            GROUP BY p1.id, p2.id;
    """
    connection = mysql.connector.connect(**mysql_config)
    cursor = connection.cursor()
    cursor.execute(query)
    products = cursor.fetchall()
    cursor.close()
    connection.close()
    return products

def group_products(products):
    product_groups = defaultdict(list)
    for product in products:
        main_product_id, duplicate_product_id, title, external_id = product[0], product[1], product[2], product[3]
        key = title
        product_groups[key].append((main_product_id, duplicate_product_id, title, external_id))
    return product_groups