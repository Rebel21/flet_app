import flet as ft
from dotenv import load_dotenv

load_dotenv()
from clients.timeweb.api_client import TimeWebApiClient


def main(page: ft.Page):
    page.title = "TimeWeb monitor"
    page.theme_mode = 'dark'
    page.window_width = 400
    page.window_height = 800

    tw_client = TimeWebApiClient()
    servers = tw_client.get_servers()
    finance_info = tw_client.get_finance_info()['finances']

    def update_info(e):
        servers = tw_client.get_servers()
        lv.controls = [
            ft.ListTile(
                leading=ft.Icon(ft.icons.COMPUTER, color=ft.colors.GREEN if server['status'] == 'on' else ft.colors.RED),
                title=ft.Text(server['name']),
                subtitle=ft.Text(f"{server['os']['name']} | {server['os']['version']}")) for server in servers['servers']]
        lv.update()

    page.appbar = ft.AppBar(
        leading_width=40,
        title=ft.Text(f"Balance: {finance_info['balance']} {finance_info['currency']}", color=ft.colors.BLACK),
        center_title=True,
        bgcolor=ft.colors.ORANGE_ACCENT,
    )

    lv = ft.ListView(expand=1, spacing=10, padding=10)

    lv_data = [
        ft.ListTile(
            leading=ft.Icon(ft.icons.COMPUTER, color=ft.colors.GREEN if server['status'] == 'on' else ft.colors.RED),
            title=ft.Text(server['name']),
            subtitle=ft.Text(f"{server['os']['name']} | {server['os']['version']}")) for server in servers['servers']]

    lv.controls = lv_data
    refresh_btn = ft.ElevatedButton(text="Get status", icon=ft.icons.ARROW_UPWARD,
                                    color=ft.colors.ORANGE, on_click=update_info)
    page.add(lv, refresh_btn)


ft.app(target=main)
