function contactMe(checkboxName, fields) {
    let divs = fields.map((x) => "field__" + x);
    let display;
    if (document.getElementsByName(checkboxName)[0].checked) {
        display = "inline";
    } else {
        fields.forEach((x) => document.getElementsByName(x)[0].value = "");
        display = "none";
    }
    divs.forEach((x) => document.getElementsByName(x).forEach((y) => y.style.display=display));
    fields.forEach((x) => document.getElementsByName(x).forEach((y) => y.style.display=display));

}
