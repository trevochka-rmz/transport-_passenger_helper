
import flet as ft

def ScheduleView(router):
    
    content = ft.Column(          
            [
                ft.Row(
                [
                    ft.Text("Расписание", size=30), 
                    ft.IconButton( icon = ft.icons.SCHEDULE,icon_size=30),
                    ], 
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    ft.Image(src=f"/raspisanie.png", width=1000,border_radius=10)
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
            ]
        )
    
    
    
    
    
    
    
    
    
    return content