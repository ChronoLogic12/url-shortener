function copyText() {
	let copyText = document.getElementById("urlShort").innerText;

	navigator.clipboard.writeText(copyText);
}

function redirect() {
	let destination = document.getElementById("urlShort").innerText;

	window.open(destination, "_blank");
}
