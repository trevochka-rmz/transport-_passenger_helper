
import flet as ft
import requests

def WeatherView(router):
    
    city_name = 'Novosibirsk'
    API = 'be7d4686fc8d7c76cb0e0dd00e323aad'
    URL = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API}&&units=metric'
    res = requests.get(URL).json()
    temp = res['main']['temp']
    print(res)
    # send_button = ft.ElevatedButton("Заказать")
    # send_button.on_click = get_info
    content = ft.Column(          
            [
                ft.Row(
                [
                    ft.Text("Погода", size=30), 
                    ft.IconButton( icon = ft.icons.CLOUD,icon_size=30),
                    ], 
                alignment=ft.MainAxisAlignment.CENTER
            ),
                ft.Row(
                    [
                        ft.Image(src=f"/cloudy.png", width=400, border_radius=10)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        ft.Text("Новосибирск", size=20),
                        ft.Text(str(temp)+"°", size=20),
                    ], alignment=ft.MainAxisAlignment.CENTER
                ),

            ]
        )
    
    
    
    
    
    
    
    
    
    return content