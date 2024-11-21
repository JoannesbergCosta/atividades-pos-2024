import { displayUsers } from './counter.js';

const userListElement = document.getElementById('userList');
const todoListElement = document.getElementById('todoList');
const todosElement = document.getElementById('todos');
const backButton = document.getElementById('backButton');

displayUsers(userListElement, todoListElement, todosElement);

backButton.addEventListener('click', () => {
    todoListElement.classList.add('hidden');
    userListElement.classList.remove('hidden');
});
