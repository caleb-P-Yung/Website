var islogedIN = localStorage.getItem("isSignedIn")
if (islogedIN != "true" || islogedIN == null){
  window.location.href = "/"
}
function createItem(itemId) {
  const checklist = document.getElementById("checklist");

  const li = document.createElement("li");
  li.innerHTML = `
    <input type="checkbox" id="${itemId}">
    <input class="item-text-input" type="text" class="item-text-input" placeholder="Edit item text">
    <button class="delete-btn">❌</button>
  `;
  
  const checkbox = li.querySelector("input[type='checkbox']");
  const textInput = li.querySelector(".item-text-input");

  checkbox.checked = localStorage.getItem(itemId) === "true";
  textInput.value = localStorage.getItem(`${itemId}-text`) || "";
  const deleteBtn = li.querySelector(".delete-btn");

deleteBtn.addEventListener("click", () => {
  // 1. Remove from DOM
  li.remove();

  // 2. Remove from localStorage
  localStorage.removeItem(itemId);
  localStorage.removeItem(`${itemId}-text`);
});

  checkbox.addEventListener("change", () => {
    localStorage.setItem(itemId, checkbox.checked);
  });

  textInput.addEventListener("input", () => {
    localStorage.setItem(`${itemId}-text`, textInput.value);
  });

  checklist.appendChild(li);
}

function restoreChecklist() {
  const keys = Object.keys(localStorage)
    .filter(k => /^item\d+$/.test(k))
    .sort((a, b) =>
      Number(a.replace("item", "")) - Number(b.replace("item", ""))
    );

  keys.forEach(createItem);
}

document.getElementById("add-btn").addEventListener("click", () => {
  let i = 1;
  while (localStorage.getItem(`item${i}`) !== null) i++;

  localStorage.setItem(`item${i}`, false);
  localStorage.setItem(`item${i}-text`, "");

  createItem(`item${i}`);
});

restoreChecklist();
