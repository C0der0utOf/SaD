async function runWorkflow(id) {
    const res = await fetch(`/run/${id}`, {
        method: "POST"
    });

    const data = await res.json();
    document.getElementById("output").innerText =
        JSON.stringify(data, null, 2);
}

