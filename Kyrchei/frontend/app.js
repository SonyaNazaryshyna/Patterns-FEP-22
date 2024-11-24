async function showData(endpoint) {
    const contentDiv = document.getElementById('content');
    contentDiv.innerHTML = 'Loading...';

    try {
        const response = await fetch(`http://localhost:8000/${endpoint}`);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        contentDiv.innerHTML = '';

        const table = document.createElement('table');
        table.border = 1;
        const headers = Object.keys(data[0]);

        const headerRow = document.createElement('tr');
        headers.forEach(header => {
            const th = document.createElement('th');
            th.textContent = header;
            headerRow.appendChild(th);
        });
        table.appendChild(headerRow);

        data.forEach(item => {
            const row = document.createElement('tr');
            headers.forEach(header => {
                const td = document.createElement('td');
                td.textContent = item[header];
                row.appendChild(td);
            });
            table.appendChild(row);
        });

        contentDiv.appendChild(table);

    } catch (error) {
        contentDiv.innerHTML = 'Error loading data: ' + error.message;
    }
}

async function setActiveTab(button, endpoint){
    const buttons = document.querySelectorAll('.tab-button');
    buttons.forEach(btn => btn.classList.remove('active'));
    button.classList.add('active')

    showData(endpoint)
}