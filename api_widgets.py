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

    def on_button_clicked_eumdac(b):
        with output:
            out_string1 = '{{\n"consumer_key": "{box1}",\n"consumer_secret": "{box2}"\n}}'
            out_string1 = out_string1.format(box1 = box1.value, box2 = box2.value)
            out_string2 = '{box1},{box2}'
            out_string2 = out_string2.format(box1 = box1.value, box2 = box2.value)
            out_file1 = os.path.join(os.path.expanduser("~"), ".eumdac_credentials")
            
            if not os.path.exists(os.path.join(os.path.expanduser("~"), ".eumdac")):
                os.makedirs(os.path.join(os.path.expanduser("~"), ".eumdac"))
            out_file2 = os.path.join(os.path.expanduser("~"), ".eumdac", "credentials")
            out_file3 = os.path.join(os.path.expanduser("~"), ".eumdac", "credentials.txt")            

            try:
                os.remove(out_file1)
            except OSError:
                pass

            with open(out_file1, "w") as f:
                f.write(out_string1)
                print(f"{out_file1} created")
            
            try:
                os.remove(out_file2)
            except OSError:
                pass

            with open(out_file2, "w") as f:
                f.write(out_string2)
                print(f"{out_file2} created")            

            try:
                os.remove(out_file3)
            except OSError:
                pass

            with open(out_file3, "w") as f:
                f.write(out_string2)
                print(f"{out_file3} created")   

    button.on_click(on_button_clicked_eumdac)
    
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

    def on_button_clicked_hda(b):
        with output:
            out_string = 'url: https://wekeo-broker.apps.mercator.dpi.wekeo.eu/databroker\nuser: {box1}\npassword: {box2}'
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
        description='Create OpenDAP file',
        disabled=False,
        button_style='info',
        tooltip='Click me',
        icon='file'
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
        placeholder='Enter your CDS key',
        disabled=False,
        layout=layout,
        display='flex'
    )

    box2 = widgets.Text(
        value=None,
        placeholder='Enter your ADS key',
        disabled=False,
        layout=layout,
        display='flex'
    )

    button = widgets.Button(
        description='Create CDS/ADS file',
        disabled=False,
        button_style='info',
        tooltip='Click me',
        icon='file'
    )

    output = widgets.Output()
    display(widgets.VBox([box1, box2, button]), output)

    def on_button_clicked_cds_ads(b):
        with output:
            out_string = '[cds]\ncds_url: https://cds.climate.copernicus.eu/api/v2\ncds_key: {box1}\n\n[ads]\nads_url: https://ads.atmosphere.copernicus.eu/api/v2\nads_key: {box2}'
            out_string = out_string.format(box1 = box1.value, box2 = box2.value)
            out_file = os.path.join(os.path.expanduser("~"), ".ecmwf_api_config")

            try:
                os.remove(out_file)
            except OSError:
                pass

            with open(out_file, "w") as f:
                f.write(out_string)
                print(f"{out_file} created")

    button.on_click(on_button_clicked_cds_ads)
