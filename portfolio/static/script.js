function toggleExtraProjects(){
    let window = document.getElementById("extra-projects");
    let button = document.getElementById("extra-button");
    if (window.style.display == "block")
    {
        window.style.display = "none";
        button.innerHTML="Expand"
    }
    else{
        window.style.display = "block";
        button.innerHTML="Collapse"
    }
}