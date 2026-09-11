import streamlit as st # type: ignore
import time as t

st.set_page_config(

    page_title = 'To-do App',
    page_icon = '⚒️',
    layout = 'centered'

)

st.title("⚒️ To-do App")

st.toast("Welcome to Our To-do App")
t.sleep(1)

option = st.selectbox('Select:', ['-select-', '1. Add Task','2. Remove Task','3. Delete All Tasks'])

tasks= []


submit = st.button('Submit')


if submit and option != '-select-':

    if option == '1. Add Task':
       
       no_of_tasks = st.number_input(
           
            label="How many tasks you have today?",
            min_value=0,    
            max_value=6,    
            value=0,         
            step=1
            
            )
       ok = st.button('submit')
       if no_of_tasks > 0 and ok:
         with st.form(key="tasks_form"):

            for i in range(no_of_tasks):
                task = st.text_input(f"Enter task {i + 1}:", key=f"task_{i}")
                tasks.append(task)
            
            submitted = st.form_submit_button("Submit Tasks")

    #    ok = st.button('submit')

    #    if ok and no_of_tasks:

    #     for task in range(no_of_tasks):
    #             task = st.text_input(f"Enter task {task + 1}: ")
    #             tasks.append(task)

    #     st.header("\nYour To-Do List:")
    #     st.write("",tasks, "\n") 


else: 
    st.toast("Select an Operation first!")

