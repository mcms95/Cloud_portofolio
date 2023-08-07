async function fetchVisitCount() {
    try {
        const response = await fetch('https://coqh2vx627.execute-api.us-east-1.amazonaws.com/try1/counter');
        const data = await response.json();
        const visitCount = JSON.parse(data.body).total_visits;

        const viewsElement = document.getElementById('views');
        viewsElement.textContent = `Views: ${visitCount}`;
    } catch (error) {
        console.error('Error fetching visit count:', error);
    }
}

fetchVisitCount();
