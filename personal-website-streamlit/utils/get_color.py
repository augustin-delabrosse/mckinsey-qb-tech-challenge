import toml
def primaryColor():
    dict_color = (toml.load(".streamlit/config.toml")["theme"])
    return dict_color["primaryColor"]
def secondaryColor():
    dict_color = (toml.load(".streamlit/config.toml")["theme"])
    return dict_color["secondaryBackgroundColor"]

def backgroundColor():
    dict_color = (toml.load(".streamlit/config.toml")["theme"])
    return dict_color["backgroundColor"]
def black():
    return "00000"
