import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    print(todo) 
    todos.append(todo)
    functions.write_todos(todos)

# def complete_todo():
#     todo = st.session_state[todo]

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app ist to increase your <b>productivity</b>.",
         unsafe_allow_html=True)

st.checkbox("Buy grocery")
st.checkbox("THrow the trash")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Enter a todo",
              on_change=add_todo, key="new_todo")

st.session_state