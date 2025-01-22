import streamlit
import streamlit as st
import Functions

todos=Functions.get_todos()

def add_todo():
    todo=st.session_state["new_todo"] + '\n'
    todos.append(todo)
    Functions.write_todos(todos)
    streamlit.session_state['new_todo']=''

st.title("MY TODO APP")
st.subheader("This is my TODO APP")

for todo in todos:
    checkbox_state=st.checkbox(todo,key=todo)
    if checkbox_state:
        index=todos.index(todo)
        todos.pop(index)
        Functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="",placeholder="Add a todo",on_change=add_todo,key='new_todo')
streamlit.session_state

#Herhangi bir button'a basildiginda ya da herhangi bir sekilde sayfa calistirildiginda yazilan tum kodlar
#calistiriliyor.