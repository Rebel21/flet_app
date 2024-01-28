import flet as ft
import requests

from clients.timeweb.api_client import TimeWebApiClient


def main(page: ft.Page):
    page.title = "TimeWeb monitor"
    page.theme_mode = 'dark'
    page.window_width = 400
    page.window_height = 400

    servers = TimeWebApiClient().get_servers()

    page.appbar = ft.AppBar(
        leading_width=40,
        title=ft.Text('Machines', color=ft.colors.BLACK),
        center_title=True,
        bgcolor=ft.colors.ORANGE_ACCENT
    )

    lv = ft.ListView(expand=1, spacing=10, padding=10)
    count = 1

    lv_data = [
        ft.ListTile(leading=ft.Icon(ft.icons.SNOOZE), title=ft.Text(server['name']), subtitle=ft.Text(server['comment'])) for server in servers['servers']]

    lv.controls = lv_data

    page.add(lv)


ft.app(target=main)
