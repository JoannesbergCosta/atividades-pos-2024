const API_URL_USERS = 'https://jsonplaceholder.typicode.com/users';
const API_URL_TODOS = 'https://jsonplaceholder.typicode.com/todos?userId=';

const translations = {
    "delectus aut autem": "deletar esse item",
    "quis ut nam": "quem é que vai?",
    "fugiat veniam minus": "descontar o que foi",
    "laboriosam mollitia et enim quasi architecto": "trabalho pesado e um plano",
    "tempore autem: et id qui não": "em breve: e quem não vai?",
};

export async function fetchUsers() {
    const response = await fetch(API_URL_USERS);
    if (!response.ok) {
        throw new Error('Failed to fetch users');
    }
    return await response.json();
}

export async function fetchTodos(userId) {
    const response = await fetch(`${API_URL_TODOS}${userId}`);
    if (!response.ok) {
        throw new Error('Failed to fetch todos');
    }
    return await response.json();
}

export async function displayUsers(userListElement, todoListElement, todosElement) {
    try {
        const users = await fetchUsers();
        userListElement.innerHTML = '';

        users.forEach(user => {
            const li = document.createElement('li');
            li.textContent = user.name;
            li.addEventListener('click', () => displayTodos(user.id, userListElement, todoListElement, todosElement));
            userListElement.appendChild(li);
        });
    } catch (error) {
        console.error('Error fetching users:', error);
    }
}

export async function displayTodos(userId, userListElement, todoListElement, todosElement) {
    try {
        const todos = await fetchTodos(userId);
        userListElement.classList.add('hidden');
        todoListElement.classList.remove('hidden');

        todosElement.innerHTML = '';
        todos.forEach(todo => {
            const li = document.createElement('li');
            const title = translations[todo.title] || todo.title;
            li.textContent = `${title} (${todo.completed ? 'Completo' : 'Incompleto'})`;
            li.className = todo.completed ? 'completed' : 'incomplete';
            todosElement.appendChild(li);
        });
    } catch (error) {
        console.error('Error fetching todos:', error);
    }
}
