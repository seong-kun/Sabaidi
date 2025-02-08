const wrap = document.querySelector(".wrap");
const scrollTable = document.querySelector(".guide");

const toggleButton = () => {
  const button = document.querySelector(".show");
  let toggle = false;
  button.addEventListener("click", () => {
    const dialogs = document.querySelectorAll("dialog");

    if (!toggle) {
      wrap.style.width = "375px";
      wrap.classList.add("mobile");
      button.textContent = "웹보기";
      exam3();
    } else {
      wrap.removeAttribute("style");
      wrap.classList.remove("mobile");
      scrollTable.classList.remove("showScroll");
      exam4();
      button.textContent = "모바일보기";
    }
    if (dialogs.length > 0) {
      dialogs.forEach((item) => item.remove());
    }
    toggle = !toggle;
  });
};

const exam1 = () => {
  // 팝업
  const zoom = document.querySelector(".zoom");
  const table1 = document.querySelector(".type1");

  zoom.addEventListener("click", () => {
    const dialog = document.createElement("dialog");
    const button = document.createElement("button");
    const clone = table1.cloneNode(true);
    dialog.appendChild(clone);
    dialog.appendChild(button);
    button.textContent = "닫기";
    document.body.appendChild(dialog);

    document.querySelector("dialog .zoom").remove();
    dialog.style.width = "90vw";
    dialog.style.height = "90vh";

    dialog.showModal();

    button.addEventListener("click", () => dialog.close());
  });
};

const exam2 = () => {
  scrollTable.addEventListener("click", () => {
    if (wrap.classList.contains("mobile")) {
      scrollTable.classList.add("showScroll");
    }
  });
};

const exam3 = () => {
  const table = document.querySelector(".type3");
  const ThsText = table.querySelectorAll("thead th");
  const Trs = table.querySelectorAll("tr");
  const Tds = table.querySelectorAll("tr td");

  ThsText.forEach((th, thIndex) => {
    const thText = th.textContent;
    Tds.forEach((td, tdIndex) => {
      if (thIndex === tdIndex) {
        const div = document.createElement("div");
        div.textContent = thText;
        div.classList.add("th");
        td.prepend(div);
      }
    });
  });
};

const exam4 = () => {
  const table = document.querySelector(".type3");
  const ths = table.querySelectorAll(".th");
  ths.forEach((th) => {
    th.remove();
  });
};

toggleButton();
exam1();
exam2();
