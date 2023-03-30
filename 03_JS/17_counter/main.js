let counter = 0;
// arrow function
let count = () => {
	counter++;
	//document.querySelector("#counter").innerHTML = counter
	$("#counter").text(counter)
	//% modulo atau reminder atau sisa bagi
	if (counter % 10 === 0){
		//alert("Counternya sudah "+counter)
		alert(`Counternya sudah ${counter}`)
	}
}