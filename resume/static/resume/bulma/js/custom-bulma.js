function openModal(modalID) {
    try {
        var mymodal = Bulma("#" + modalID).modal();
        mymodal.open();
    } catch (e) {
        console.log(e);
    }
}

function expandCard(contentID) {
    var contentChildren = document.getElementById(contentID).children;

    for (let i = 0; i < contentChildren.length; i++) {
        if (!contentChildren[i].classList.contains("card-header")) {
            if (contentChildren[i].classList.contains("is-hidden")) {
                contentChildren[i].classList.remove("is-hidden");
            } else {
                contentChildren[i].classList.add("is-hidden");
            }
        }
    };
};

var typeDelay = function () {
    var timer = 0;
    return function (callback, ms) {
        clearTimeout(timer);
        timer = setTimeout(callback, ms);
    }
}();

function filterTable() {
    var milestoneFilter = document.getElementById("milestone-filter-input").value.toLowerCase();
    var typeFilter = document.getElementById("type-filter-input").value.toLowerCase();
    var tagFilter = document.getElementById("tag-filter-input").value.toLowerCase();

    var filterableRows = document.getElementsByClassName("filterable");

    for (let i = 0; i < filterableRows.length; i++) {
        milestoneText = filterableRows[i].childNodes[1].textContent.toLowerCase();
        milestoneMatch = null;

        typeText = filterableRows[i].childNodes[3].textContent.toLowerCase();
        typeMatch = null;

        tagText = filterableRows[i].childNodes[9].textContent.toLowerCase();
        tagMatch = null;

        if ((milestoneFilter === null) || (milestoneText.includes(milestoneFilter))) {
            milestoneMatch = 1;
        }
        if ((typeFilter === null) || (typeText.includes(typeFilter))) {
            typeMatch = 1;
        }
        if ((tagFilter === null) || (tagText.includes(tagFilter))) {
            tagMatch = 1;
        }

        if ((!!milestoneMatch) && (!!typeMatch) && (!!tagMatch)) {
            filterableRows[i].classList.remove("is-hidden");
        } else {
            filterableRows[i].classList.add("is-hidden");
        }
    };

};

function clearFilters() {
    var filterInputs = document.getElementsByClassName("filter-input");

    for (let i = 0; i < filterInputs.length; i++) {
        filterInputs[i].value = null;
    };
}

window.onload = function () {
    clearFilters();
};
