function sample() {
    const x = 3;

    const url = "http://localhost:8000/sample";
    // const url = "http://127.0.0.1:8000/sample";

    const params = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            x: x,
        }),
    };

    fetch(url, params)
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
        })
        .catch((error) => {
            console.log(error);
        });
}
