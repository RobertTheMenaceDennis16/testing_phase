async function loadTodos() {

    const res = await fetch('/todos');
    const todos = await res.json();

    const list = document.getElementById('todoList');
    list.innerHTML = '';

    todos.forEach(todo => {

        const li = document.createElement('li');

        li.className =
            "flex justify-between bg-gray-200 p-2 rounded";

        li.innerHTML = `
            ${todo.title}
            <button onclick="deleteTodo(${todo.id})"
                    class="text-red-500">
                X
            </button>
        `;

        list.appendChild(li);
    });
}

async function addTodo() {

    const input = document.getElementById('todoInput');

    await fetch('/todos', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({title: input.value})
    });

    input.value = '';
    loadTodos();
}
async function deleteTodo(id) {

    await fetch(`/todos/${id}`, {
        method: 'DELETE'
    });

    loadTodos();
}

loadTodos();
