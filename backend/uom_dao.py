def get_uoms(connection):
    cursor = connection.cursor()
    query = ("select * from units")
    cursor.execute(query)
    response = []
    for (uom_id, uom_name) in cursor:
        response.append({
            'uom_id': uom_id,
            'uom_name': uom_name
        })
    return response


if __name__ == '__main__':
    from create_conn import connect_db

    connection = connect_db()
    # print(get_all_products(connection))
    print(get_uoms(connection))