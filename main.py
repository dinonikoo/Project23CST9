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



def get_1c():
    dpg.configure_item("q1", show=False)
    dpg.configure_item("1c", show=True)
    dpg.set_primary_window("1c", True)
    
def get_pascal():
    dpg.configure_item("q31", show=False)
    dpg.configure_item("pascal", show=True)
    dpg.set_primary_window("pascal", True)

def get_cpp():
    dpg.configure_item("q33", show=False)
    dpg.configure_item("cpp", show=True)
    dpg.set_primary_window("cpp", True)

def get_swift():
    dpg.configure_item("q4", show=False)
    dpg.configure_item("swift", show=True)
    dpg.set_primary_window("swift", True)

def get_csharp():
    dpg.configure_item("q5", show=False)
    dpg.configure_item("csharp", show=True)
    dpg.set_primary_window("csharp", True)

def get_python():
    dpg.configure_item("q5", show=False)
    dpg.configure_item("python", show=True)
    dpg.set_primary_window("python", True)

def get_javascript():
    dpg.configure_item("q6", show=False)
    dpg.configure_item("javascript", show=True)
    dpg.set_primary_window("javascript", True)

def get_php():
    dpg.configure_item("q7", show=False)
    dpg.configure_item("php", show=True)
    dpg.set_primary_window("php", True)

def get_java():
    dpg.configure_item("q8", show=False)
    dpg.configure_item("java", show=True)
    dpg.set_primary_window("java", True)

def get_who():
    dpg.configure_item("q8", show=False)
    dpg.configure_item("who", show=True)
    dpg.set_primary_window("who", True)



def open_q1():
    dpg.configure_item("main", show=False)
    dpg.configure_item("q1", show=True)
    dpg.set_primary_window("q1",True)


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

# Вопрос 4
with dpg.window(no_resize=True, no_title_bar=True, show=False,
                tag="q4") as q4:
    with dpg.group(horizontal=True):
        title_q1 = dpg.add_text(
            default_value="Вопрос 4",
            pos=[window_width//2 - 95, window_height//2 - 260]
        )
        dpg.bind_item_font(title_q1, custom_font)
        q1 = dpg.add_text(
            default_value="Любишь понты?",
            pos=[window_width//2 - 425, window_height//2 - 180]
        )
        dpg.add_separator()
        button_yes = dpg.add_button(label=" Да ", pos = [window_width//2 - 140, window_height//2 + 30],
                                    callback=get_swift)
        dpg.bind_item_font(button_yes, custom_font)
        button_no = dpg.add_button(label=" Нет ", pos = [window_width//2 + 30, window_height//2 + 30],
                                   callback=open_q5)
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
