    let now = new Date();
    let dateTime = now.toLocaleString();

    document.getElementById("Today").innerHTML = ` ${now.getMonth()+1}/${now.getDate()}/${now.getFullYear()}`