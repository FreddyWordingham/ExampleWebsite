function sample() {
    const real = document.getElementById("realInput").value;
    const imag = document.getElementById("imagInput").value;
    console.log(real, imag);

    const url = "http://localhost:8000/sample";

    const params = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            real: real,
            imag: imag,
        }),
    };

    fetch(url, params)
        .then((response) => response.json())
        .then((data) => {
            document.getElementById("result").value = data;
        })
        .catch((error) => {
            console.log(error);
        });
}

function image() {
    const real = document.getElementById("realInput").value;
    const imag = document.getElementById("imagInput").value;

    const width = document.getElementById("widthInput").value;
    const height = document.getElementById("heightInput").value;

    const zoom = document.getElementById("zoomInput").value;
    const maxIter = document.getElementById("maxIterInput").value;

    const url = "http://localhost:8000/image";

    const params = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            real: real,
            imag: imag,
            width: width,
            height: height,
            zoom: zoom,
            max_iter: maxIter,
        }),
    };

    fetch(url, params)
        .then((_response) => {
            document.body.style.backgroundImage = "url(/static/mandy.png?r=" + Math.random() + ")";
        })
        .catch((error) => {
            console.log(error);
        });
}
