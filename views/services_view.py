import flet as ft
from data import dataUsers
import pymysql
from my_config import host, user, password, db_name

count_podushka = 0
count_plaits = 0
count_fork = 0
count_soud= 0
count_telephone = 0
count_provodnik = 0
def ServicesView(router):
    def service1(e):
        global count_podushka
        count_podushka+=1
        try:
            connection = pymysql.connect(
                host=host, 
                user = user,
                password=password,
                database= db_name,
                cursorclass=pymysql.cursors.DictCursor)
            print("connect successfully")
        except Exception as ex:
            print("Connection refused...")
            print(ex)
        try:
            
            with connection.cursor() as cursor:
                create_table_quare = f"UPDATE `services` SET count_services = {count_podushka}  WHERE name = 'Подушка';"
                cursor.execute(create_table_quare)

        finally:
            connection.commit()
            connection.close()
        dataUsers["services"]["Подушка"]["count"] = count_podushka

    def service2(e):
        global count_plaits
        count_plaits+=1
        try:
            connection = pymysql.connect(
                host=host, 
                user = user,
                password=password,
                database= db_name,
                cursorclass=pymysql.cursors.DictCursor)
            print("connect successfully")
        except Exception as ex:
            print("Connection refused...")
            print(ex)
        try:
            
            with connection.cursor() as cursor:
                create_table_quare = f"UPDATE `services` SET count_services = {count_plaits}  WHERE name = 'Одеяло';"
                cursor.execute(create_table_quare)

        finally:
            connection.commit()
            connection.close()
        dataUsers["services"]["Одеяло"]["count"] = count_plaits

    def service3(e):
        global count_fork
        count_fork+=1
        try:
            connection = pymysql.connect(
                host=host, 
                user = user,
                password=password,
                database= db_name,
                cursorclass=pymysql.cursors.DictCursor)
            print("connect successfully")
        except Exception as ex:
            print("Connection refused...")
            print(ex)
        try:
            
            with connection.cursor() as cursor:
                create_table_quare = f"UPDATE `services` SET count_services = {count_fork}  WHERE name = 'Приборы';"
                cursor.execute(create_table_quare)

        finally:
            connection.commit()
            connection.close()
        dataUsers["services"]["Приборы"]["count"] = count_fork
        print(dataUsers)

    def service4(e):
        global count_soud
        count_soud+=1
        try:
            connection = pymysql.connect(
                host=host, 
                user = user,
                password=password,
                database= db_name,
                cursorclass=pymysql.cursors.DictCursor)
            print("connect successfully")
        except Exception as ex:
            print("Connection refused...")
            print(ex)
        try:
            
            with connection.cursor() as cursor:
                create_table_quare = f"UPDATE `services` SET count_services = {count_soud}  WHERE name = 'Наушники';"
                cursor.execute(create_table_quare)

        finally:
            connection.commit()
            connection.close()
        dataUsers["services"]["Наушники"]["count"] = count_soud

    def service5(e):
        global count_telephone
        count_telephone+=1
        try:
            connection = pymysql.connect(
                host=host, 
                user = user,
                password=password,
                database= db_name,
                cursorclass=pymysql.cursors.DictCursor)
            print("connect successfully")
        except Exception as ex:
            print("Connection refused...")
            print(ex)
        try:
            
            with connection.cursor() as cursor:
                create_table_quare = f"UPDATE `services` SET count_services = {count_telephone}  WHERE name = 'Телефон';"
                cursor.execute(create_table_quare)

        finally:
            connection.commit()
            connection.close()
        dataUsers["services"]["Телефон"]["count"] = count_telephone

    def service6(e):
        global count_provodnik
        count_provodnik = 1
        try:
            connection = pymysql.connect(
                host=host, 
                user = user,
                password=password,
                database= db_name,
                cursorclass=pymysql.cursors.DictCursor)
            print("connect successfully")
        except Exception as ex:
            print("Connection refused...")
            print(ex)
        try:
            
            with connection.cursor() as cursor:
                create_table_quare = f"UPDATE `services` SET count_services = {count_provodnik}  WHERE name = 'Проводник';"
                cursor.execute(create_table_quare)

        finally:
            connection.commit()
            connection.close()
        dataUsers["services"]["Проводник"]["call"] = count_provodnik

        
    send_button = ft.ElevatedButton("Заказать")
    send_button2 = ft.ElevatedButton("Заказать")
    send_button3 = ft.ElevatedButton("Заказать")
    send_button4 = ft.ElevatedButton("Заказать")
    send_button5 = ft.ElevatedButton("Заказать")
    send_button6 = ft.ElevatedButton("Заказать")
    send_button.on_click = service1
    send_button2.on_click = service2
    send_button3.on_click = service3
    send_button4.on_click = service4
    send_button5.on_click = service5
    send_button6.on_click = service6
    content = ft.Column(          
            [
                ft.Row(
                [
                    ft.Text("Дополнительные услуги", size=30), 
                    ft.IconButton( icon = ft.icons.ROOM_SERVICE,icon_size=30),
                    ], 
                alignment=ft.MainAxisAlignment.CENTER
            ),
                ft.Row([
                    ft.Column(
                    [
                        ft.Image(src=f"/podushka.jpg", width=200, border_radius=100),
                        ft.Text("Подушка"),
                        send_button

                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Column(
                    [
                        ft.Image(src=f"/plaid.jpg", width=200, border_radius=100),
                        ft.Text("Одеяло"),
                        send_button2

                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Column(
                    [
                        ft.Image(src=f"/fork.jpg", width=200, border_radius=100),
                        ft.Text("Приборы"),
                        send_button3

                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                    ),
                ], alignment=ft.MainAxisAlignment.CENTER, spacing = 70

                ) ,
            
                ft.Row([
                    ft.Column(
                    [
                        ft.Image(src=f"/sound.jpg", width=180, border_radius=100),
                        ft.Text("Наушники"),
                        send_button4

                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Column(
                    [
                        ft.Image(src=f"/telephone.jpg", width=200, border_radius=100),
                        ft.Text("Телефон"),
                        send_button5

                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Column(
                    [
                        ft.Image(src=f"/provodnik.jpg", width=200, border_radius=100),
                        ft.Text("Проводник"),
                        send_button6

                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                    ),
                ], alignment=ft.MainAxisAlignment.CENTER, spacing = 70

                ) ,

            ]
        )
    
    
    
    
    
    
    
    
    
    return content