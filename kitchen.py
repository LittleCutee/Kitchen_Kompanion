import streamlit as st

def home():
    st.title('Kitchen Kompanion')
    st.write('Hello, User!')
    st.write('')
    st.write('Warning:')
    st.write('Milk will expire in 2 days.')
    st.write('No more beef.')
    st.write('')
    st.write("Today's Recommendation:")
    st.write('Curry Shrimp')

def inventory():
    st.title('Inventory')
    st.write('Milk')
    st.write('2')
    st.write('')
    st.write('Bread')
    st.write('3')
    st.write('')
    st.write('Eggs')
    st.write('12')

def recipes():
    st.title('Recipes')
    st.button('Fried Eggs')
    st.button('Curry Shrimp')
    st.button('Teriyaki Chicken')

def shop_list():
    st.title('Shop List')
    if st.checkbox('Beef'):
        st.write('Beef Purchased')
    c2 = st.checkbox('Fish')
    c3 = st.checkbox('Celery')

def sidebar():
    if st.sidebar.button('Home'):
        home()

    if st.sidebar.button('Inventory'):
        inventory()

    if st.sidebar.button('Recipes'):
        recipes()

    if st.sidebar.button('Shop List'):
        shop_list()

sidebar()