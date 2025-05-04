import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

# App config
#----------------------------------------------------------------------------------------------------------------------------------#
# Page config
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown(
    """
    <style>
    img[data-testid="stLogo"] {
                height: 6rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App title
st.title("What's new in Streamlit 1.45?")
st.divider()

with st.sidebar:
    st.logo('https://raw.githubusercontent.com/curiositydataanalytics/Integrate-a-PyDeck-map-into-Streamlit-using-Python-Tutorial/refs/heads/main/logo_large.png')
    st.empty()
#
#

def page1():
    st.header(':one: st.user')

    st.code('''
    if not st.user.is_logged_in:
        if st.button("Log in :material/login:"):
            st.login()
    else:
        if st.button("Log out :material/logout:"):
            st.logout()
        st.markdown(
            f"<p style='font-size: 20pt;'>Hello <img src='{st.user.picture}' style='height: 40px; width: 40px; vertical-align: middle;'> <b>{st.user.name}</b>,</p>"
            f"<p style='font-size: 20pt;'>You have successfully logged in with <b>{st.user.email}</b>.</p>",
            unsafe_allow_html=True
        )
    ''')
    if not st.user.is_logged_in:
        if st.button("Log in :material/login:"):
            st.login()
    else:
        if st.button("Log out :material/logout:"):
            st.logout()
        st.markdown(
            f"<p style='font-size: 20pt;'>Hello <img src='{st.user.picture}' style='height: 40px; width: 40px; vertical-align: middle;'> <b>{st.user.name}</b>,</p>"
            f"<p style='font-size: 20pt;'>You have successfully logged in with <b>{st.user.email}</b>.</p>",
            unsafe_allow_html=True
        )



def page2():
    st.header(':two: st.multiselect')

    st.subheader('Streamlit 1.44')
    st.code('''
    options = st.multiselect('Select your favorite colors:', ['Red', 'Green', 'Blue'])
    ''')
    options = st.multiselect('Select your favorite colors:', ['Red', 'Green', 'Blue'])

    st.divider()

    st.subheader('Streamlit 1.45')
    st.code('''
    options = st.multiselect('Select your favorite colors:', ['Red', 'Green', 'Blue'], accept_new_options=True)
    ''')
    options = st.multiselect('Select your favorite colors:', ['Red', 'Green', 'Blue'], accept_new_options=True, key='ts')

def page3():
    st.header(':three: alerts')
    st.subheader('Streamlit 1.44')
    st.code('''
    st.success('Task completed!', icon="✅")
    st.info('Download has started...', icon="ℹ️")
    ''')
    st.success('Task completed!', icon="✅")
    st.info('Download has started...', icon="ℹ️")
    
    st.divider()

    st.subheader('Streamlit 1.45')
    st.code('''
    st.success('Task completed!', icon="✅", width=300)
    st.info('Download has started...', icon="ℹ️", width=300)
    ''')
    st.success('Task completed!', icon="✅", width=300)
    st.info('Download has started...', icon="ℹ️", width=300)



def page4():
    st.header(':four: st.components.v1.html')

    st.code('''
            
    html = """
    <div style="display: flex; gap: 10px; justify-content: center; padding-top: 20px;">
    <button tabindex="3" style="padding: 10px;">Tab Index 3</button>
    <button tabindex="1" style="padding: 10px;">Tab Index 1</button>
    <button tabindex="2" style="padding: 10px;">Tab Index 2</button>
    </div>
    """
            
    st.components.v1.html(html, tab_index=0)
    ''')
    html = """
    <div style="display: flex; gap: 10px; justify-content: center; padding-top: 20px;">
    <button tabindex="3" style="padding: 10px;">Tab Index 3</button>
    <button tabindex="1" style="padding: 10px;">Tab Index 1</button>
    <button tabindex="2" style="padding: 10px;">Tab Index 2</button>
    </div>
    """
    components.html(html, tab_index=0)

def page5():
    st.header(':five: st.text_input')

    st.code('''
    question = st.text_input("Submit your question:", icon="❓")
    st.write("You have submitted the following question:", question)
    ''')
    question = st.text_input("Submit your question:", icon="❓")
    st.write("You have submitted the following question:", question)
    st.divider()
    st.code('''
    price = st.number_input("Submit the price:", icon="💲")
    st.write("You have submitted: ", price)
    ''')
    price = st.number_input("Submit the price:", icon="💲")
    st.write("You have submitted: ", price)


pg = st.navigation([st.Page(page1, title='st.user'),
                    st.Page(page2, title='st.multiselect'),
                    st.Page(page3, title='alerts'),
                    st.Page(page4, title='st.components.v1.html'),
                    st.Page(page5, title='st.text_input')])
pg.run()