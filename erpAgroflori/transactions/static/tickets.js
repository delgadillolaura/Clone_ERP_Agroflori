let quantityInputs = document.getElementsByClassName("quantity-class")

Array.from(quantityInputs).forEach(element => {
    element.addEventListener('input', (event) => {
        updateAmount(event);
    });
});

function updateAmount(event) {
    let id = event.target.id;
    let quantity = event.target.value;
    let prefix = id.slice(0, -"-quantity".length);    

    let amount_element_id = prefix + "-amount";
    let category = document.getElementById( prefix + "-ticket-type");
    console.log(category)
    let unitary_price = category.data('unitary_price');
    amount_element_id.value = unitary_price * quantity;

}
