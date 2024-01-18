import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.title("Todo App")

def create_todo():
    title = st.text_input("Enter Todo Title")
    description = st.text_area("Enter Todo Description")
    if st.button("Add Todo"):
        response = requests.post(f"{BASE_URL}/todos", json={"title": title, "description": description})
        if response.status_code == 200:
            st.success("Todo added successfully")

def delete_todo():
    todo_id = st.text_input("Enter Todo ID to delete")
    if st.button("Delete Todo"):
        response = requests.delete(f"{BASE_URL}/todos/{todo_id}")
        if response.status_code == 200:
            st.success(f"Todo with ID {todo_id} deleted successfully")
        elif response.status_code == 404:
            st.warning(f"Todo with ID {todo_id} not found")
        else:
            st.error(f"Failed to delete Todo with ID {todo_id}")

def update_todo():
    todo_id = st.text_input("Enter Todo ID to update")
    title = st.text_input("Enter updated Todo Title")
    description = st.text_area("Enter updated Todo Description")
    if st.button("Update Todo"):
        response = requests.put(f"{BASE_URL}/todos/{todo_id}", json={"todo_id": todo_id, "title": title, "description": description})
        
        if response.status_code == 200:
            st.success(f"Todo with ID {todo_id} updated successfully")
        elif response.status_code == 404:
            st.warning(f"Todo with ID {todo_id} not found")
        else:
            st.error(f"Failed to update Todo with ID {todo_id}. Status Code: {response.status_code}, Response Text: {response.text}")

            
            
def get_todos():
    response = requests.get(f"{BASE_URL}/todos/")
    if response.status_code == 200:
        todos = response.json()
        st.write("Todo List:")
        for todo in todos:
            st.write(f"ID: {todo['id']}, Title: {todo['title']}, Description: {todo['description']}")

if __name__ == "__main__":
    create_todo()
    update_todo()
    delete_todo()
    get_todos()
