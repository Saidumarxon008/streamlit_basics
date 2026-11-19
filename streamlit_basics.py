# from datetime import datetime
import streamlit as st

# #basic text
# st.write('Hello World!')
# st.title('Title')
# st.header('Header')
# st.subheader('Subheader')
# st.markdown('_Markdown_')
# st.caption('Caption')
# st.code("print('hello:', name)", language='python')
# st.divider()

# form_values = {
#     'name': None,
#     'dob': None,
#     'gender': None, 
# }
# min_date = datetime(1990, 1, 1)
# max_date = datetime.now()
# #with st.form() it only reruns once submit is pressed
# with st.form(key='user_info'):
#     form_values['name'] = st.text_input('Enter your name:')
#     form_values['dob'] = st.date_input('Enter your date of birth:', max_value=max_date, min_value=min_date)
#     form_values['gender'] = st.selectbox('Gender', ['Male', 'Female'])
#     submit_button = st.form_submit_button()
#     if submit_button:
#         if not all(form_values.values()):
#             st.warning('Please fill in all of the fields')
#         else:
#             st.balloons()
#             st.write('### Info')
#             for (key, value) in form_values.items():
#                 st.write(f"{key}: {value}")
                
# if 'counter' not in st.session_state:
#     st.session_state.counter = 0
# if st.button('Increment counter'):
#     st.session_state.counter += 1
#     st.write(f'Counter incremented to {st.session_state.counter}')
# if st.button('Reset'):
#     st.session_state.counter = 0
# st.write(f'Counter Value: {st.session_state.counter}')

# #callback
# if 'step' not in st.session_state:
#     st.session_state.step = 1
# if 'info' not in st.session_state:
#     st.session_state.info = {}
    
# def go_to_step_1():
#     st.session_state.step = 1
    
# def go_to_step_2(name):
#     st.session_state.info['name'] = name
#     st.session_state.step = 2
    
# if st.session_state.step == 1:
#     st.header('Part 1: Info')
#     name = st.text_input('Name', value=st.session_state.info.get('name', ''))
#     st.button('Next', on_click=go_to_step_2, args=(name,))
# elif st.session_state.step == 2:
#     st.header('Part 2: Review')
#     st.subheader('Please review this:')
#     st.write(f'**Name**: {st.session_state.info.get('name', '')}')
#     if st.button('Submit'):
#         st.success('Great!')
#         st.balloons()
#         st.session_state.info = {}
#     st.button('Back', on_click=go_to_step_1, )
    
# #layouts
# #sidebar
# st.sidebar.title('This is the Sidebar')
# st.sidebar.write('You can put something here')
# sidebar_input = st.sidebar.text_input('Enter something')

# #tabs
# tab1, tab2, tab3 = st.tabs(['Tab1', 'Tab2', 'Tab3'])

# with tab1:
#     st.write('This is Tab1')

# with tab2:
#     st.write('This is Tab2')

# with tab3:
#     st.write('This is Tab3')
    
# #columns
# col1, col2 = st.columns(2)

# with col1:
#     st.header('Column 1')
#     st.write('Content for Column 1')

# with col2:
#     st.header('Column 2')
#     st.write('Content for Column 2')
    
# with st.container(border=True):
#     st.write('This is inside a container')
   
# #placeholder 
# placeholder = st.empty()
# placeholder.write('This is an empty placeholder, useful for dynamic content')

# if st.button('Update Placeholder'):
#     placeholder.write('The Placeholder has been updated')

# #expander
# with st.expander('Expand for more details'):
#     st.write('This is additional information that is hidden by default.')

# #Popover (Tooltip)
# st.write('Hover over this button for a tooltip')
# st.button('Button with tooltip', help='This is a tooltip or popover on hover.')

# #advanced widgets
# if "slider" not in st.session_state:
#     st.session_state.slider = 25

# min_value = st.slider("Set min value", 0, 50, 25)

# st.session_state.slider = st.slider("Slider", min_value, 100, st.session_state.slider)

#store values

if 'checkbox' not in st.session_state:
    st.session_state.checkbox = False

if 'user_input' not in st.session_state:
    st.session_state.user_input = ''

def toggle_input():
    st.session_state.checkbox = not st.session_state.checkbox

st.checkbox(
    'Show Input Field',
    value=st.session_state.checkbox,
    on_change=toggle_input
)

if st.session_state.checkbox:
    user_input = st.text_input(
        'Enter something:',
        value=st.session_state.user_input
    )
    st.session_state.user_input = user_input
else:
    user_input = st.session_state.get('user_input', '')

st.write(f'User Input: {user_input}')
