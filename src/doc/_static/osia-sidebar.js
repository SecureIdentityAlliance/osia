document.addEventListener("DOMContentLoaded", function () {
  const localToc = document.getElementById("osia-localtoc");
  if (!localToc) return;

  const tocTree = localToc.querySelector(".osia-sidebar-localtoc-tree");
  if (!tocTree || tocTree.textContent.trim() === "") {
    localToc.remove();
    return;
  }

  // Sphinx often wraps the real section TOC inside the current page title.
  // If so, keep only the nested <ul>.
  const firstNestedList = tocTree.querySelector(":scope > ul > li > ul");
  if (firstNestedList) {
    tocTree.innerHTML = "";
    tocTree.appendChild(firstNestedList);
  }

  const currentItems = document.querySelectorAll("li.current");
  if (!currentItems.length) {
    localToc.remove();
    return;
  }

  const currentItem = currentItems[currentItems.length - 1];
  currentItem.appendChild(localToc);

  const currentLink = currentItem.querySelector("a");
  if (!currentLink) return;

  currentLink.addEventListener("click", function () {
    const isVisible = localToc.style.display !== "none";
    localToc.style.display = isVisible ? "none" : "block";
  });

  //this is to control the submenu built by OSIA
const localTocLinks = localToc.querySelectorAll(
  ".osia-sidebar-localtoc-tree a"
);

localTocLinks.forEach(function (link) {

  link.addEventListener("click", function () {

    // Remove active state from all subsection links
    localTocLinks.forEach(function (otherLink) {
        otherLink.classList.remove("current");
    });

    // Remove dimming from all sidebar links first
    const sidebarCurrentLinks = document.querySelectorAll(
      ".sidebar-drawer li.current > a"
    );

    sidebarCurrentLinks.forEach(function (sidebarLink) {
      sidebarLink.classList.remove("osia-parent-dimmed");
    });

    // Highlight clicked subsection
    link.classList.add("current");

    // Dim all parent/current sidebar links
    sidebarCurrentLinks.forEach(function (sidebarLink) {
      sidebarLink.classList.add("osia-parent-dimmed");
    });

  });

});



// If a Furo level-2 item is current after page reload,
// dim its level-1 parent chapter link.
const currentLevel2Items = document.querySelectorAll(
  ".sidebar-tree .toctree-l1.has-children > ul > li.toctree-l2.current"
);

currentLevel2Items.forEach(function (currentLevel2) {
  const parentChapter = currentLevel2.closest(".toctree-l1.has-children");
  if (!parentChapter) return;

  const parentLink = parentChapter.querySelector(":scope > a");
  if (!parentLink) return;

  parentLink.classList.add("osia-parent-dimmed");
});





// Parent page item: toctree-l1 but NOT has-children
const simpleCurrentPageItems = document.querySelectorAll(
  ".sidebar-tree li.toctree-l1.current:not(.has-children)"
);

simpleCurrentPageItems.forEach(function (item) {
  const parentLink = item.querySelector(":scope > a");
  if (!parentLink) return;

  parentLink.addEventListener("click", function () {
    const localTocLinks = item.querySelectorAll(
      ".osia-sidebar-localtoc-tree a"
    );

    // Parent selected: local TOC children become muted
    localTocLinks.forEach(function (tocLink) {
      tocLink.classList.remove("current");
      tocLink.classList.add("osia-toc-dimmed");
    });

    // Parent becomes active again
    parentLink.classList.remove("osia-parent-dimmed");
    parentLink.classList.add("osia-furo-submenu-current");
  });
});








});
