const form = document.getElementById("foodForm");
const tableBody = document.querySelector("#foodTable tbody");
let foodItems = [];

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const item = {
    name: form.name.value.trim(),
    price: parseFloat(form.price.value),
    category: form.category.value,
    description: form.description.value.trim()
  };

  if (item.price <= 0 || !item.name || !item.category) {
    alert("Please enter valid details.");
    return;
  }

  foodItems.push(item);
  renderTable();
  form.reset();
});

function renderTable() {
  tableBody.innerHTML = "";
  foodItems.forEach((item, index) => {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${item.name}</td>
      <td>₹${item.price.toFixed(2)}</td>
      <td>${item.category}</td>
      <td>${item.description}</td>
      <td>
        <button class="btn btn-sm btn-warning" onclick="editItem(${index})">Edit</button>
        <button class="btn btn-sm btn-danger" onclick="deleteItem(${index})">Delete</button>
      </td>`;
    tableBody.appendChild(row);
  });
}

function deleteItem(index) {
  foodItems.splice(index, 1);
  renderTable();
}

function editItem(index) {
  const item = foodItems[index];
  form.name.value = item.name;
  form.price.value = item.price;
  form.category.value = item.category;
  form.description.value = item.description;
  foodItems.splice(index, 1);
}