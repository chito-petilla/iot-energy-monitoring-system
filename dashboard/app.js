async function loadData() {
    const res = await fetch("http://localhost:5000/api/latest");
    const data = await res.json();

    document.getElementById("output").innerText =
        JSON.stringify(data, null, 2);
}
