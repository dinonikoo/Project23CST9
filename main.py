import dearpygui.dearpygui as dpg

dpg.create_context()

window_width = 1000
window_height = 600

# Шрифты
with dpg.font_registry():
    with dpg.font(file="fonts/content.ttf", size=30) as default_font:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
    with dpg.font(file="fonts/content.ttf", size=40) as custom_font:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
    with dpg.font(file="fonts/content.ttf", size=100) as big_font:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)

dpg.create_viewport(title="Test HSE2023", resizable=False, small_icon="logo.ico")
dpg.configure_viewport(0, x_pos=400, y_pos=150, width=window_width, height=window_height)
dpg.set_viewport_max_height(window_height)
dpg.set_viewport_max_width(window_width)

def open_q1():
    dpg.configure_item("main", show=False)
    dpg.configure_item("q1", show=True)
    dpg.set_primary_window("q1",True)

def return_1():
    dpg.configure_item("1c", show=False)
    dpg.configure_item("main", show=True)
    dpg.set_primary_window("main", True)

def return_2():
    dpg.configure_item("pascal", show=False)
    dpg.configure_item("main", show=True)
    dpg.set_primary_window("main", True)

def return_3():
    dpg.configure_item("cpp", show=False)
    dpg.configure_item("main", show=True)
    dpg.set_primary_window("main", True)

def return_4():
    dpg.configure_item("swift", show=False)
    dpg.configure_item("main", show=True)
    dpg.set_primary_window("main", True)

def return_5():
    dpg.configure_item("csharp", show=False)
    dpg.configure_item("main", show=True)
    dpg.set_primary_window("main", True)

def return_6():
    dpg.configure_item("python", show=False)
    dpg.configure_item("main", show=True)
    dpg.set_primary_window("main", True)

def return_7():
    dpg.configure_item("javascript", show=False)
    dpg.configure_item("main", show=True)
    dpg.set_primary_window("main", True)

def return_8():
    dpg.configure_item("php", show=False)
    dpg.configure_item("main", show=True)
    dpg.set_primary_window("main", True)

def return_9():
    dpg.configure_item("java", show=False)
    dpg.configure_item("main", show=True)
    dpg.set_primary_window("main", True)

def return_0():
    dpg.configure_item("who", show=False)
    dpg.configure_item("main", show=True)
    dpg.set_primary_window("main", True)


# Вопрос 1
with dpg.window(no_resize=True, no_title_bar=True, show=False,
                tag="q1") as q1:
    with dpg.group(horizontal=True):
        title_q1 = dpg.add_text(
            default_value="Вопрос 1",
            pos=[window_width//2 - 95, window_height//2 - 260]
        )
        dpg.bind_item_font(title_q1, custom_font)
        q1 = dpg.add_text(
            default_value="Знаешь английский язык?",
            pos=[window_width//2 - 425, window_height//2 - 180]
        )
        dpg.add_separator()
        button_yes = dpg.add_button(label=" Да ", pos = [window_width//2 - 140, window_height//2 + 30],
                                    callback=open_q2)
        dpg.bind_item_font(button_yes, custom_font)
        button_no = dpg.add_button(label=" Нет ", pos = [window_width//2 + 30, window_height//2 + 30],
                                   callback=get_1c)
        dpg.bind_item_font(button_no, custom_font)

# Вопрос 2
with dpg.window(no_resize=True, no_title_bar=True, show=False,
                tag="q2") as q2:
    with dpg.group(horizontal=True):
        title_q1 = dpg.add_text(
            default_value="Вопрос 2",
            pos=[window_width//2 - 95, window_height//2 - 260]
        )
        dpg.bind_item_font(title_q1, custom_font)
        q1 = dpg.add_text(
            default_value="Твоя возрастная категория?",
            pos=[window_width//2 - 425, window_height//2 - 180]
        )
        dpg.add_separator()
        button_1 = dpg.add_button(label=" Школьник ", pos = [window_width//2 - 400, window_height//2 + 30],
                                    callback=open_q31)
        dpg.bind_item_font(button_1, custom_font)
        button_2 = dpg.add_button(label=" В расцвете сил ", pos = [window_width//2 - 150, window_height//2 + 30],
                                   callback=open_q32)
        dpg.bind_item_font(button_2, custom_font)
        button_2 = dpg.add_button(label=" За 50 ", pos=[window_width // 2 + 220, window_height // 2 + 30],
                                  callback=open_q33)
        dpg.bind_item_font(button_2, custom_font)
        
# Вопрос 6(4)
with dpg.window(no_resize=True, no_title_bar=True, show=False,
                tag="q6") as q6:
    with dpg.group(horizontal=True):
        title_q1 = dpg.add_text(
            default_value="Вопрос 4",
            pos=[window_width//2 - 95, window_height//2 - 260]
        )
        dpg.bind_item_font(title_q1, custom_font)
        q1 = dpg.add_text(
            default_value="Хочешь сразу видеть результат работы?",
            pos=[window_width//2 - 425, window_height//2 - 180]
        )
        dpg.add_separator()
        button_yes = dpg.add_button(label=" Да ", pos = [window_width//2 - 140, window_height//2 + 30],
                                    callback=get_javascript)
        dpg.bind_item_font(button_yes, custom_font)
        button_no = dpg.add_button(label=" Нет ", pos = [window_width//2 + 30, window_height//2 + 30],
                                   callback=open_q7)
        dpg.bind_item_font(button_no, custom_font)
        
# Вопрос 7(5)
with dpg.window(no_resize=True, no_title_bar=True, show=False,
                tag="q7") as q7:
    with dpg.group(horizontal=True):
        title_q1 = dpg.add_text(
            default_value="Вопрос 5",
            pos=[window_width//2 - 95, window_height//2 - 260]
        )
        dpg.bind_item_font(title_q1, custom_font)
        q1 = dpg.add_text(
            default_value="У тебя есть друзья?",
            pos=[window_width//2 - 425, window_height//2 - 180]
        )
        dpg.add_separator()
        button_yes = dpg.add_button(label=" Да ", pos = [window_width//2 - 140, window_height//2 + 30],
                                    callback=open_q8)
        dpg.bind_item_font(button_yes, custom_font)
        button_no = dpg.add_button(label=" Нет ", pos = [window_width//2 + 30, window_height//2 + 30],
                                   callback=get_php)
        dpg.bind_item_font(button_no, custom_font)

# Вопрос 8(6)
with dpg.window(no_resize=True, no_title_bar=True, show=False,
                tag="q8") as q8:
    with dpg.group(horizontal=True):
        title_q1 = dpg.add_text(
            default_value="Вопрос 6",
            pos=[window_width//2 - 95, window_height//2 - 260]
        )
        dpg.bind_item_font(title_q1, custom_font)
        q1 = dpg.add_text(
            default_value="Хочешь много зарабатывать?",
            pos=[window_width//2 - 425, window_height//2 - 180]
        )
        dpg.add_separator()
        button_yes = dpg.add_button(label=" Да ", pos = [window_width//2 - 140, window_height//2 + 30],
                                    callback=get_java)
        dpg.bind_item_font(button_yes, custom_font)
        button_no = dpg.add_button(label=" Нет ", pos = [window_width//2 + 30, window_height//2 + 30],
                                   callback=get_who)
        dpg.bind_item_font(button_no, custom_font)        
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
