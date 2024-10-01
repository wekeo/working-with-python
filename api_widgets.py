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
        description='Create eumdac credentials file',
        disabled=False,
        button_style='info',
        tooltip='Click me',
        icon='file',
        layout = widgets.Layout(width = "300px")
    )

    output = widgets.Output()
    display(widgets.VBox([box1, box2, button]), output)

    def on_button_clicked_eumdac(b):
        with output:

            out_string_eumdac = '{consumer_key},{consumer_secret}'
            out_string_eumdac = out_string_eumdac.format(consumer_key = box1.value, consumer_secret = box2.value)

            out_string_thomas = '{{"consumer_key": "{consumer_key}", "consumer_secret": "{consumer_secret}"}}'
            out_string_thomas = out_string_thomas.format(consumer_key = box1.value, consumer_secret = box2.value)
            
            if not os.path.exists(os.path.join(os.path.expanduser("~"), ".eumdac")):
                os.makedirs(os.path.join(os.path.expanduser("~"), ".eumdac"))
            out_file_eumdac = os.path.join(os.path.expanduser("~"), ".eumdac", "credentials")
            out_file_thomas = os.path.join(os.path.expanduser("~"), ".eumdac_credentials.json")

            try:
                os.remove(out_file_eumdac)
            except OSError:
                pass

            with open(out_file_eumdac, "w") as f:
                f.write(out_string_eumdac)
                print(f"{out_file_eumdac} created")
            
            try:
                os.remove(out_file_thomas)
            except OSError:
                pass

            with open(out_file_thomas, "w") as f:
                f.write(out_string_thomas)
                print(f"{out_file_thomas} created")
                
    button.on_click(on_button_clicked_eumdac)

def earthdata_widget():
    layout = widgets.Layout(width='100', height='40px')

    box1 = widgets.Password(
        value='',
        placeholder='Enter your username',
        disabled=False
    )
    box2 = widgets.Password(
        value='',
        placeholder='Enter your password',
        disabled=False
    )
    button = widgets.Button(
        description='Create Earthdata credentials file',
        disabled=False,
        button_style='info',
        tooltip='Click me',
        icon='file',
        layout = widgets.Layout(width = "300px")
    )

    output = widgets.Output()
    display(widgets.VBox([box1, box2, button]), output)

    def on_button_clicked_earthdata(b):
        with output:

            out_string_earthdata = '{{"username": "{username}", "password": "{password}"}}'
            out_string_earthdata = out_string_earthdata.format(username = box1.value, password = box2.value)

            out_file_earthdata = os.path.join(os.path.expanduser("~"), ".obpg_credentials.json")

            try:
                os.remove(out_file_earthdata)
            except OSError:
                pass

            with open(out_file_earthdata, "w") as f:
                f.write(out_string_earthdata)
                print(f"{out_file_earthdata} created")

    button.on_click(on_button_clicked_earthdata)

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
        description='Create HDA credentials file',
        disabled=False,
        button_style='info',
        tooltip='Click me',
        icon='file',
        layout = widgets.Layout(width = "300px")
    )

    output = widgets.Output()
    display(widgets.VBox([box1, box2, button]), output)

    def on_button_clicked_hda(b):
        with output:
            out_string = 'user: {box1}\npassword: {box2}'
            out_string = out_string.format(box1 = box1.value, box2 = box2.value)
            out_file = os.path.join(os.path.expanduser("~"), ".hdarc")

            try:
                os.remove(out_file)
            except OSError:
                pass

            with open(out_file, "w") as f:
                f.write(out_string)
                print(f"{out_file} created")

    button.on_click(on_button_clicked_hda)

def cmems_widget():

    layout = widgets.Layout(width='100', height='40px')

    box1 = widgets.Text(
        value=None,
        placeholder='Enter your CMEMS username',
        disabled=False,
        layout=layout,
        display='flex'
    )
    box2 = widgets.Password(
        value='',
        placeholder='Enter your CMEMS password',
        disabled=False
    )  
    button = widgets.Button(
        description='Create CMEMS API crednentials file',
        disabled=False,
        button_style='info',
        tooltip='Click me',
        icon='file',
        layout = widgets.Layout(width = "300px")
    )

    output = widgets.Output()
    display(widgets.VBox([box1, box2, button]), output)

    def on_button_clicked_cmems(b):
        with output:
            out_string = '{{\n"https://my.cmems-du.eu": ["{box1}", "{box2}"],\n"https://nrt.cmems-du.eu": ["{box1}", "{box2}"]\n}}'
            out_string = out_string.format(box1 = box1.value, box2 = box2.value)
            out_file = os.path.join(os.path.expanduser("~"), ".cmems_opendap")

            try:
                os.remove(out_file)
            except OSError:
                pass

            with open(out_file, "w") as f:
                f.write(out_string)
                print(f"{out_file} created")

    button.on_click(on_button_clicked_cmems)
    
def cds_ads_widget():

    layout = widgets.Layout(width='100', height='40px')

    box1 = widgets.Text(
        value=None,
        placeholder='Enter your CDS API key',
        disabled=False,
        layout=layout,
        display='flex'
    )

    box2 = widgets.Text(
        value=None,
        placeholder='Enter your ADS API key',
        disabled=False,
        layout=layout,
        display='flex'
    )
    
    button = widgets.Button(
        description='Create CDS/ADS credentials files',
        disabled=False,
        button_style='info',
        tooltip='Click me',
        icon='file',
        layout = widgets.Layout(width = "300px")
    )

    output = widgets.Output()
    display(widgets.VBox([box1, box2, button]), output)

    def on_button_clicked_cds_ads(b):
        with output:
            out_string = '[cds]\ncds_url: https://cds.climate.copernicus.eu/api/v2\ncds_key: {box1}\n\n[ads]\nads_url: https://ads.atmosphere.copernicus.eu/api/v2\nads_key: {box2}'
            out_string = out_string.format(box1 = box1.value, box2 = box2.value)
            out_file = os.path.join(os.path.expanduser("~"), ".ecmwf_api_config.txt")
            
            try:
                os.remove(out_file)
            except OSError:
                pass

            with open(out_file, "w") as f:
                f.write(out_string)
                print(f"{out_file} created")

    button.on_click(on_button_clicked_cds_ads)
