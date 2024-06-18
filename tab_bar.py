from typing import List

import flet as ft


class TabItem(ft.Container):
    selected = False
    text = None
    icon = None

    def __init__(self, text='', icon=ft.icons.ABC):
        super().__init__()
        self.selected = False
        self.text = text
        self.icon = icon
        self.render()

    def render(self):
        self.bgcolor = '#E5E6EB' if self.selected else '#FFFFFF',
        self.content = ft.Row(
            width=320,
            height=120,
            controls=[
                ft.Icon(self.icon, size=80, color='#1D2129' if self.selected else '#5F6268', ),
                ft.Text(value=self.text, size=30, color='#1D2129' if self.selected else '#5F6268', )
            ],
            spacing=20,
            alignment=ft.alignment.center_left,
        )

    def select(self):
        self.selected = True
        self.render()
        return self.selected

    def unselect(self):
        self.selected = False
        self.render()
        return self.selected


class TabBar(ft.ListView):
    selected_index = 0

    def __init__(self, children: List[TabItem] = None, selected_index=0):
        super().__init__()
        self.auto_scroll = False
        self.horizontal = False
        self.selected_index = selected_index
        self.controls = children
        for index, child in enumerate(self.controls):
            child.on_click = lambda e, i=index: self.select_child(i)

    def did_mount(self):
        super().did_mount()
        self.select_child(self.selected_index)

    def select_child(self, selected_index):
        print(self.controls)
        print(selected_index)
        self.selected_index = selected_index
        for index, child in enumerate(self.controls):
            if index == selected_index:
                child.select()
            else:
                child.unselect()
        self.update()
