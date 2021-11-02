function copyText() {
	var copyText = document.getElementById("urlShort").innerText;

	navigator.clipboard.writeText(copyText);
}
