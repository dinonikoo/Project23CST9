import dearpygui.dearpygui as dpg

dpg.create_context()

window_width = 1000
window_height = 600

dpg.create_viewport(title="Test HSE2023", resizable=False, small_icon="logo.ico")
dpg.configure_viewport(0, x_pos=400, y_pos=150, width=window_width, height=window_height)
dpg.set_viewport_max_height(window_height)
dpg.set_viewport_max_width(window_width)

# Главное окно
with dpg.window(no_resize=True, no_title_bar=True,
                tag="main") as main:
    with dpg.group(horizontal=True):
        group = dpg.add_text(
            default_value="23КНТ-9",
            pos = [window_width//2 - 70, window_height//2 - 220],
            color=[93, 93, 93]
        )
        title = dpg.add_text(
            default_value="Какой язык программирования тебе подходит?",
            pos=[window_width//2 - 420, window_height//2 - 100]
        )
        dpg.bind_item_font(title, custom_font)
        start_button = dpg.add_button(label="Начать", pos = [window_width//2 - 80, window_height//2],callback=open_q1)
        dpg.bind_item_font(start_button, custom_font)


dpg.bind_font(default_font)
dpg.set_primary_window(window=main, value=True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()