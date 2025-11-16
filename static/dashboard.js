function openModal(content) {
    document.getElementById("modal-body").innerHTML = content;
    document.getElementById("modal").style.display = "block";
}

function closeModal() {
    document.getElementById("modal").style.display = "none";
}

async function runWorkflow(id) {
    const res = await fetch(`/run/${id}`, { method: "POST" });
    const data = await res.json();

    let html = `
        <strong>${data.result.workflow}</strong>
        <ul>
            ${data.result.executed.map(step =>
                `<li>${step.step} <span style='color:green'>✔</span></li>`
            ).join("")}
        </ul>
    `;

    openModal(html);
}

// Close when clicking outside modal
window.onclick = function(event) {
    const modal = document.getElementById("modal");
    if (event.target === modal) {
        closeModal();
    }
};

