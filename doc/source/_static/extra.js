// constants
const maxScroll = 500;

let back_button = document.getElementById("back-to-top-btn");

window.onload = function() { createCopyBtn() };

window.onscroll = function() { scrollFunction() };

function scrollFunction() {
  if (document.body.scrollTop > maxScroll ||
      document.documentElement.scrollTop > maxScroll) {
    back_button.style.display = "block";
  } else {
    back_button.style.display = "none";
  }
}

function gotoTop() {
  window.scrollTo({top: 0, behavior: 'smooth'});
}

function btnToggleActive(button) {
  button.classList.add("cubic-smooth");
  button.classList.remove("inactive-btn");
  button.classList.add("active-btn");
 }

function btnToggleInactive(button, delayMs = 200) {
  button.classList.remove("active-btn");
  button.classList.add("inactive-btn");
  setTimeout(() => {
    button.classList.remove("cubic-smooth");
  }, delayMs);
}

function createCopyBtn(btnStillText = "Copy", btnActivatedText = "Copied",
    btnActivatedTimeMs = 2000, selector = `[class="highlight"]`) {
  document.querySelectorAll(selector).forEach(
    node => {
      let copyBtn = document.createElement("button");
      copyBtn.setAttribute("type", "button");
      copyBtn.setAttribute("class", "copy-btn btn inactive-btn");
      copyBtn.innerText = btnStillText;
      node.appendChild(copyBtn);

      copyBtn.addEventListener("click", async () => {
        contents = []
        if (navigator.clipboard) {
          const pre = node.getElementsByTagName("pre")[0]
          const items = pre.childNodes;
          let i = 0;
          while (i < items.length) {
            let item = items[i];
            if (item.nodeName == "#text") {
              contents.push(item.nodeValue);
            } else {
              contents.push(item.innerText);
            }
            i++;
          }
          await navigator.clipboard.writeText(contents.join(""));
        }

        btnToggleActive(copyBtn);

        copyBtn.innerText = btnActivatedText;

        setTimeout(() => {
          copyBtn.innerText = btnStillText;
          btnToggleInactive(copyBtn);
        }, btnActivatedTimeMs);
      })
    }
  )
}
