import flet as ft

from tab_bar import TabItem, TabBar


def main(page: ft.Page):
    # #
    # page.add(ft.SafeArea(ft.Text("Hello, Flet!")))
    # #
    # t = ft.Text(value="Hello, world!", color="green")
    # page.controls.append(t)
    # page.update()
    # #
    # t = ft.Text()
    # page.add(t)  # 是 page.controls.append(t) 和 page.update() 的快捷方式
    # for i in range(10):
    #     t.value = f"Step {i}"
    #     page.update()
    #     time.sleep(1)
    status_bar = ft.Container(
        content=ft.Text(value='状态栏', color='#D0D2D7', size=40, ),
        alignment=ft.alignment.center,
        height=80,
        bgcolor='#E5E6EB',
    )
    content = ft.Container(
        # content=ft.Text(value='内容区', color='#D0D2D7', size=40, ),
        content=TabBar(
            children=[
                TabItem(text='1212121', icon=ft.icons.CONTACTS),
                TabItem(text='4545454', icon=ft.icons.ACCESSIBILITY),
                TabItem(text='8989898', icon=ft.icons.MOBILE_FRIENDLY),
                TabItem(text='8989898', icon=ft.icons.MOBILE_FRIENDLY),
                TabItem(text='8989898', icon=ft.icons.MOBILE_FRIENDLY),
                TabItem(text='8989898', icon=ft.icons.MOBILE_FRIENDLY),
            ],
            selected_index=0
        ),
        alignment=ft.alignment.top_left,
        bgcolor='#FFFFFF',
        expand=True)
    dock_bar = ft.Container(
        content=ft.Text(value='Dock栏', color='#D0D2D7', size=40, ),
        alignment=ft.alignment.center,
        height=120,
        bgcolor='#5F6268',
    )
    page.padding = 0
    page.spacing = 0
    page.add(status_bar, content, dock_bar)


if __name__ == '__main__':
    ft.app(main)
