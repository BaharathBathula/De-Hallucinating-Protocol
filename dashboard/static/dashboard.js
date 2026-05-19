async function loadMetrics() {

    const response = await fetch("/trust/metrics");
    const metrics = await response.json();

    document.getElementById("total-events").innerText =
        metrics.total_events;

    document.getElementById("escalated-events").innerText =
        metrics.escalated_events;

    document.getElementById("blocked-events").innerText =
        metrics.blocked_events;

    document.getElementById("restricted-events").innerText =
        metrics.restricted_events;
}


async function loadEvents() {

    const response = await fetch("/trust/events");
    const events = await response.json();

    const tableBody =
        document.getElementById("events-table-body");

    tableBody.innerHTML = "";

    events.reverse().forEach(event => {

        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${event.event_type}</td>
            <td>${event.runtime_state}</td>
            <td>${event.trust_score}</td>
            <td>${event.escalation_required}</td>
            <td>${event.timestamp}</td>
        `;

        tableBody.appendChild(row);
    });
}


async function refreshDashboard() {
    await loadMetrics();
    await loadEvents();
}


refreshDashboard();

setInterval(refreshDashboard, 5000);
