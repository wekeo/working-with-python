## EUMDAC commands

# get eumdac help and options
eumdac --help

# get eumdac method help and options
eumdac search --help (for example)

# get all information
eumdac describe

# get collection information
eumdac describe -c EO:EUM:DAT:0407

# filter by time
eumdac search -c EO:EUM:DAT:0407 --start 2023-05-26T12:15 --end 2023-05-29T12:45

# filter by time and bbox
eumdac search -c EO:EUM:DAT:0407 --start 2023-05-26T12:15 --end 2023-05-29T12:45 --bbox -6 50 -4 52

# filter by time and polygon
eumdac search -c EO:EUM:DAT:0407 --start 2023-05-26T12:15 --end 2023-05-29T12:45 --geometry 'POLYGON((-6 50,-4 50,-4 52,-6 52,-6 50))'

# dump products to file
eumdac search -c EO:EUM:DAT:0407 --start 2023-05-26T12:15 --end 2023-05-29T12:45 --bbox -6 50 -4 52 > products.txt

# download from file
eumdac download -c EO:EUM:DAT:0407 -p @products.txt

# download directly
eumdac download -c EO:EUM:DAT:0407 --start 2023-05-26T12:15 --end 2023-05-29T12:45 --bbox -6 50 -4 52
