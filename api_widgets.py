import ipywidgets as widgets
import os

def eumdac_widget():
    layout = widgets.Layout(width='100', height='40px')

    box1 = widgets.Password(
        value='',
        placeholder='Enter your consumer key',
        disabled=False
    )
    box2 = widgets.Password(
        value='',
        placeholder='Enter your consumer secret',
        disabled=False
    )
    button = widgets.Button(
        description='Create eumdac file',
        disabled=False,
        button_style='info',
        tooltip='Click me',
        icon='file'
    )

    output = widgets.Output()
    display(widgets.VBox([box1, box2, button]), output)

    def on_button_clicked1(b):
        with output:
            out_string = '{{\n"consumer_key": "{box1}"\n"consumer_secret": "{box2}"\n}}'
            out_string = out_string.format(box1 = box1.value, box2 = box2.value)
            out_file = os.path.join(os.path.expanduser("~"), ".eumdac_credentials")

            try:
                os.remove(out_file)
            except OSError:
                pass

            with open(out_file, "w") as f:
                f.write(out_string)
                print(f"{out_file} created")

    button.on_click(on_button_clicked1)
    
def hda_widget():

    layout = widgets.Layout(width='100', height='40px')

    box1 = widgets.Text(
        value=None,
        placeholder='Enter your WEkEO username',
        disabled=False,
        layout=layout,
        display='flex'
    )
    box2 = widgets.Password(
        value='',
        placeholder='Enter your WEkEO password',
        disabled=False
    )  
    button = widgets.Button(
        description='Create HDA file',
        disabled=False,
        button_style='info',
        tooltip='Click me',
        icon='file'
    )

    output = widgets.Output()
    display(widgets.VBox([box1, box2, button]), output)

    def on_button_clicked2(b):
        with output:
            out_string = 'user:{box1}\npassword:{box2}'
            out_string = out_string.format(box1 = box1.value, box2 = box2.value)
            out_file = os.path.join(os.path.expanduser("~"), ".hdarc")

            try:
                os.remove(out_file)
            except OSError:
                pass

            with open(out_file, "w") as f:
                f.write(out_string)
                print(f"{out_file} created")

    button.on_click(on_button_clicked2)