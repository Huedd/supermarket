// scripts/app.js

// LocalStorage Utils
function getEmployees() {
  return JSON.parse(localStorage.getItem("employees")) || [];
}

function saveEmployees(employees) {
  localStorage.setItem("employees", JSON.stringify(employees));
}

// Add Employee
function addEmployee(name, position, salary) {
  const employees = getEmployees();
  employees.push({ id: Date.now(), name, position, salary });
  saveEmployees(employees);
}

// Populate Employee Table
function populateTable() {
  const table = document.getElementById("employeeTable");
  if (!table) return;
  const employees = getEmployees();
  table.innerHTML = "";
  employees.forEach(emp => {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${emp.name}</td>
      <td>${emp.position}</td>
      <td>${emp.salary}</td>
      <td>
        <button onclick="viewProfile(${emp.id})">View</button>
        <button onclick="deleteEmployee(${emp.id})">Delete</button>
      </td>
    `;
    table.appendChild(row);
  });
}

// Delete Employee
function deleteEmployee(id) {
  const employees = getEmployees().filter(emp => emp.id !== id);
  saveEmployees(employees);
  populateTable();
}

// View Profile
function viewProfile(id) {
  localStorage.setItem("selectedEmployee", id);
  window.location.href = "employee_profile.html";
}

// Show Profile Data
function loadProfile() {
  const id = parseInt(localStorage.getItem("selectedEmployee"));
  const emp = getEmployees().find(emp => emp.id === id);
  if (emp) {
    document.getElementById("empName").textContent = emp.name;
    document.getElementById("empPosition").textContent = emp.position;
    document.getElementById("empSalary").textContent = emp.salary;
  } else {
    window.location.href = "404.html";
  }
}

// Search
function searchEmployee() {
  const search = document.getElementById("search").value.toLowerCase();
  const employees = getEmployees();
  const filtered = employees.filter(e => e.name.toLowerCase().includes(search));
  const table = document.getElementById("employeeTable");
  table.innerHTML = "";
  filtered.forEach(emp => {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${emp.name}</td>
      <td>${emp.position}</td>
      <td>${emp.salary}</td>
      <td>
        <button onclick="viewProfile(${emp.id})">View</button>
        <button onclick="deleteEmployee(${emp.id})">Delete</button>
      </td>
    `;
    table.appendChild(row);
  });
}

// Handle Add Form
document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("employeeForm");
  if (form) {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const name = document.getElementById("name").value;
      const position = document.getElementById("position").value;
      const salary = document.getElementById("salary").value;
      addEmployee(name, position, salary);
      alert("Employee added!");
      form.reset();
    });
  }

  populateTable();
  loadProfile();
});