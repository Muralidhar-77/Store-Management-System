from create_conn import connect_db

def get_all_products(connection):
    cursor = connection.cursor()
    query = ("select products.product_id, products.p_name, products.unit_id, products.price_per_unit, units.unit_name from products inner join units on products.unit_id=units.unit_id")
    cursor.execute(query)
    response = []
    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'product_id': product_id,
            'name': name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        })
    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "(p_name, unit_id, price_per_unit)"
             "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid

if __name__ == '__main__':
    connection = connect_db()
    # print(get_all_products(connection))
    print(insert_new_product(connection,{
        'product_name':'tooth_paste',
        'uom_id':2,
        'price_per_unit':10
    }))