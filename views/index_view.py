from typing import Union
import flet as ft
from views.Router import Router, DataStrategyEnum
# from State import global_state, State
import sqlite3
import random

def IndexView(router_data: Union[Router, str, None] = None):
    id = random.randint(1,100) 
    # def send_data(e: ft.ControlEvent):
    #     if text_field.value == "":
    #         return
    #     if router_data and router_data.data_strategy == DataStrategyEnum.QUERY:
    #         e.page.go("/data", data=text_field.value)
    #     elif router_data and router_data.data_strategy == DataStrategyEnum.ROUTER_DATA: 
    #         router_data.set_data("data", text_field.value)
    #         e.page.go("/data", data=text_field.value)
    #     elif router_data and router_data.data_strategy == DataStrategyEnum.CLIENT_STORAGE:
    #         e.page.client_storage.set("data", text_field.value)
    #         e.page.go("/data")
    #     elif router_data and router_data.data_strategy == DataStrategyEnum.STATE:
    #         state = State("data", text_field.value)
    #         e.page.go("/data")
    #     else:
    #         e.page.go("/data")
    def food_go(e: ft.ControlEvent):
        # db = sqlite3.connect('helper.help')
        # cur = db.cursor()
        # cur.execute(f"INSERT INTO users VALUES(NULL,'{}'))")
        # db.close()
        e.page.go('/food')
    def services_go(e: ft.ControlEvent):
        e.page.go('/services')
    def schedule_go(e: ft.ControlEvent):
        e.page.go('/schedule')
    def report_go(e: ft.ControlEvent):
        e.page.go('/report')
    def weather_go(e: ft.ControlEvent):
        e.page.go('/weather')
    def setup_go(e: ft.ControlEvent):
        e.page.go('/settings')


    text_field = ft.TextField()
    # send_button = ft.ElevatedButton("Send")
    # image1 = ft.Image(src=f"/food.png", width=200)
    food_drinks_button = ft.IconButton( icon = ft.icons.FOOD_BANK,icon_size=170)
    services_button = ft.IconButton( icon = ft.icons.ROOM_SERVICE,icon_size=170)
    schedule_button = ft.IconButton( icon = ft.icons.SCHEDULE,icon_size=170)
    report_button = ft.IconButton( icon = ft.icons.REPORT,icon_size=170)
    weather_button = ft.IconButton( icon = ft.icons.CLOUD,icon_size=170)
    setup_button = ft.IconButton( icon = ft.icons.SETTINGS,icon_size=170)

    
    food_drinks_button.on_click = food_go
    services_button.on_click = services_go
    schedule_button.on_click = schedule_go
    report_button.on_click = report_go
    weather_button.on_click = weather_go
    setup_button.on_click = setup_go

    # send_button.on_click = send_data
    content = ft.Column(
            [
                ft.Row(
                [
                    ft.Text(
                        "Здесь вы можете выбрать любую услугу и мы сразу уведомим работника",
                        size=30),
                ], 
                alignment=ft.MainAxisAlignment.CENTER
            ),

            
            ft.Row(
            [
                food_drinks_button,
                services_button,
                schedule_button
            ],
            alignment=ft.MainAxisAlignment.CENTER, spacing = 70
            ),
            ft.Row(
            [
                report_button,
                weather_button,
                setup_button
            ],
            alignment=ft.MainAxisAlignment.CENTER , spacing = 70
            )
            
        ]
        )
    
    return content


