

const userList = document.getElementById('userList');
const todoList = document.getElementById('todoList');
const todos = document.getElementById('todos');
const backButton = document.getElementById('backButton');


const API_URL_USERS = 'https://jsonplaceholder.typicode.com/users';
const API_URL_TODOS = 'https://jsonplaceholder.typicode.com/todos?userId=';


const translations = {
    "delectus aut autem": "deletar esse item",
    "quis ut nam": "quem é que vai?",
    "fugiat veniam minus": "descontar o que foi",
    "laboriosam mollitia et enim quasi architecto": "trabalho pesado e um plano",
    "tempore autem: et id qui non": "em breve: e quem não vai?",
    // é muita coisa pra traduzir manualmente
};

async function fetchUsers() {
    const response = await fetch(API_URL_USERS);
    const users = await response.json();
    displayUsers(users);
}
function displayUsers(users) {
    users.forEach(user => {
        const li = document.createElement('li');
        li.textContent = user.name;
        li.onclick = () => fetchTodos(user.id);
        userList.appendChild(li);
    });
}
async function fetchTodos(userId) {
    const response = await fetch(API_URL_TODOS + userId);
    const todosData = await response.json();
    displayTodos(todosData);
}

function displayTodos(todosData) {
    userList.classList.add('hidden');
    todoList.classList.remove('hidden');
    todos.innerHTML = '';

    todosData.forEach(todo => {
        const li = document.createElement('li');
        
        
        const title = translations[todo.title] || todo.title; 
        li.textContent = title + (todo.completed ? ' (Completo)' : ' (Incompleto)');

        
        li.className = todo.completed ? 'completed' : 'incomplete';

        todos.appendChild(li); 
    });
}

backButton.onclick = () => {
    todoList.classList.add('hidden');
    userList.classList.remove('hidden');
};

fetchUsers();
